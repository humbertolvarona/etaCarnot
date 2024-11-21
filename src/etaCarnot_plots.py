import pandas as pd
import numpy as np
import xarray as xr
from scipy.io import loadmat
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter

def read_eta_at_time_and_depth(nc_file, time_index, depth_index):
    ds = xr.open_dataset(nc_file)
    eta_2d = ds["eta"].isel(time=time_index, depth=depth_index)
    longitude = ds["longitude"]
    latitude = ds["latitude"]
    return eta_2d, longitude, latitude


def plot_eta_map(eta_2d, longitude, latitude, title="Map of Eta", colormap="viridis", cb_orientation="horizontal", font_sizes=None, value_range=None, save_path=None):
    font_sizes = font_sizes or {"title": 14, "labels": 12, "colorbar": 12}
    fig, ax = plt.subplots(figsize=(12, 8), subplot_kw={"projection": ccrs.PlateCarree()})
    if value_range:
        levels = np.linspace(value_range[0], value_range[1], value_range[2])
    else:
        levels = 15
    mesh = ax.contourf(longitude, latitude, eta_2d, levels=levels, cmap=colormap, transform=ccrs.PlateCarree())
    cbar = plt.colorbar(mesh, ax=ax, orientation=cb_orientation, pad=0.05, shrink=0.8)
    cbar.set_label(r"$\eta_{\mathrm{Carnot}}$", fontsize=font_sizes["colorbar"])
    cbar.ax.tick_params(labelsize=font_sizes["colorbar"])
    if cbar.get_ticks().size > 0:
        cbar.set_ticks(cbar.get_ticks())
        cbar.set_ticklabels([f"{tick:.3f}" for tick in cbar.get_ticks()])
    else:
        print("Advertencia: La barra de color no tiene ticks definidos automáticamente.")
    ax.coastlines(resolution="10m", color="black", linewidth=1)
    ax.add_feature(cfeature.LAND, facecolor="lightgray")
    ax.add_feature(cfeature.BORDERS, linestyle=":")
    gl = ax.gridlines(draw_labels=True, color="gray", alpha=0.5, linestyle="--")
    gl.top_labels = False
    gl.right_labels = False
    gl.xformatter = LongitudeFormatter(degree_symbol="°", number_format=".0f")
    gl.yformatter = LatitudeFormatter(degree_symbol="°", number_format=".0f")
    gl.xlabel_style = {"size": font_sizes["labels"], "color": "black"}
    gl.ylabel_style = {"size": font_sizes["labels"], "color": "black"}
    ax.set_title(title, fontsize=font_sizes["title"])
    ax.set_xlabel("Longitude", fontsize=font_sizes["labels"])
    ax.set_ylabel("Latitude", fontsize=font_sizes["labels"])
    if save_path:
        plt.savefig(save_path, dpi=500, bbox_inches="tight")
    plt.show()


def get_time_index(nc_file, target_date):
    ds = xr.open_dataset(nc_file)
    if "time" not in ds.variables:
        raise KeyError("La variable 'time' no está presente en el archivo NetCDF.")
    time_var = ds["time"]
    if np.issubdtype(time_var.values.dtype, np.datetime64):
        times = pd.to_datetime(time_var.values)
    else:
        origin = pd.Timestamp("1900-01-01 00:00:00")
        times = origin + pd.to_timedelta(time_var.values, unit="D")
    target_date = pd.Timestamp(target_date)
    time_deltas = (times - target_date).total_seconds()
    time_index = np.abs(time_deltas).argmin()
    return int(time_index)
