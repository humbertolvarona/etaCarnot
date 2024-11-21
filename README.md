# etaCarnot

Processing and Visualization of TEDACS Data

# Description

This project provides functions for processing, transforming, and visualizing ocean thermal efficiency data ηCarnotηCarnot​ in NetCDF and CSV formats. It includes tools to handle multiple years of data, perform monthly calculations, and plot maps.

# Dependencies

Ensure you have the following libraries installed:

    Pandas
    NumPy
    Xarray
    Matplotlib
    Cartopy
    SciPy

Install them with:

```sh
pip install pandas numpy xarray matplotlib cartopy scipy
```

# Main function

1. get_time_index(nc_file, target_date)

Gets the time index closest to a specific date from a NetCDF file.
Parameters:

    nc_file: Path to the NetCDF file.
    target_date: Target date in "YYYY-MM-DD" format.

Returns:

    The time index as an integer.

Example:

```python
time_index = get_time_index("data.nc", "1993-02-14")
```
2. 

