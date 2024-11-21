import os
import pandas as pd
import numpy as np
import matplotlib.colors as mcolors


def read_and_concatenate_files(start_year, end_year, depth, base_input_path):
    data_list = []

    for year in range(start_year, end_year + 1):
        input_file = os.path.join(base_input_path, f"{year}_{depth}_MaxEficiency.txt")
        if os.path.exists(input_file):
            print(f"Reading files: {input_file}")
            data = pd.read_csv(
                input_file,
                header=None,
                names=["date", "depth", "longitude", "latitude", "eta"],
                parse_dates=["date"]
            )
            data["eta"] = data["eta"].replace(-32767, np.nan)
            data_list.append(data)
        else:
            print(f"File nor found: {input_file}. Skipping...")

    if data_list:
        return pd.concat(data_list, ignore_index=True)
    else:
        raise FileNotFoundError("Empty directory.")


def reshape_to_xarray_direct(data):
    ref_time = pd.Timestamp("1900-01-01 00:00:00")
    data["time"] = (data["date"] - ref_time).dt.total_seconds() / 86400  # Convertir a días
    data = data.drop(columns=["date"])
    ds = data.set_index(["time", "depth", "latitude", "longitude"]).to_xarray()
    return ds


def save_combined_netcdf(data, output_file):
    data["time"].attrs["units"] = "days since 1900-01-01 00:00:00"
    data["time"].attrs["calendar"] = "gregorian"
    data.to_netcdf(output_file)
    print(f"Data saved in NetCDF file: {output_file}")


def process_and_save_all_years(start_year, end_year, depth, base_input_path, output_file):
    data = read_and_concatenate_files(start_year, end_year, depth, base_input_path)
    xarray_data = reshape_to_xarray_direct(data)
    save_combined_netcdf(xarray_data, output_file)

