import os
import pandas as pd
import numpy as np

def read_csv_file(file_path):
    data = pd.read_csv(
        file_path,
        header=None,
        names=["date", "depth", "longitude", "latitude", "eta"],
        parse_dates=["date"]
    )
    data["eta"] = data["eta"].replace(-32767, np.nan)
    return data


def calculate_monthly_mean(data):
    data["year_month"] = data["date"].dt.to_period("M")
    monthly_mean = data.groupby(
        ["year_month", "depth", "longitude", "latitude"], as_index=False
    )["eta"].mean()
    return monthly_mean


def calculate_middle_of_month(year_month):
    first_day = year_month.to_timestamp()
    last_day = (year_month + 1).to_timestamp() - pd.Timedelta(days=1)
    middle_day = first_day + (last_day - first_day) / 2
    return middle_day


def reshape_to_xarray(data):
    # Ajustar `time` al día medio de cada mes
    data["time"] = data["year_month"].apply(calculate_middle_of_month)
    ref_time = pd.Timestamp("1900-01-01 00:00:00")
    data["time"] = (data["time"] - ref_time).dt.total_seconds() / 86400  # Convertir a días
    data = data.drop(columns=["year_month"])
    ds = data.set_index(["time", "depth", "latitude", "longitude"]).to_xarray()
    return ds


def save_to_netcdf(data, output_file):
    data["time"].attrs["units"] = "days since 1900-01-01 00:00:00"
    data["time"].attrs["calendar"] = "gregorian"
    data.to_netcdf(output_file)


def process_csv_to_netcdf(input_file, output_file):
    data = read_csv_file(input_file)
    monthly_mean = calculate_monthly_mean(data)
    xarray_data = reshape_to_xarray(monthly_mean)
    save_to_netcdf(xarray_data, output_file)


def process_multiple_years(start_year, end_year, depth, base_input_path, base_output_path):
    for year in range(start_year, end_year + 1):
        input_file = os.path.join(base_input_path, f"{year}_{depth}_MaxEficiency.txt")
        output_file = os.path.join(base_output_path, f"{year}_{depth}_MeanMaxEficiency.nc")
        if os.path.exists(input_file):
            print(f"Processing {input_file} -> {output_file}")
            process_csv_to_netcdf(input_file, output_file)
        else:
            print(f"File not found: {input_file}. Skipping...")
