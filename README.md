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

# Main functions

1. get_time_index(nc_file, target_date)

Gets the time index closest to a specific date from a NetCDF file.

### Parameters

- **`nc_file`**: Path to the NetCDF file.
- **`target_date`**: Target date in "YYYY-MM-DD" format.

### Returns:

    The time index as an integer.

### Example:

```python
time_index = get_time_index("data.nc", "1993-02-14")
```

---

2. `process_multiple_years(start_year, end_year, depth, base_input_path, base_output_path)`

Processes multiple years of CSV data and saves the results as yearly NetCDF files.

### Parameters:
- **`input_dir`**: Directory containing the input CSV files.
- **`output_dir`**: Directory for the output NetCDF files.
- **`depth`**: Depth = [763., 910., 1062.44].
- **`start_year`**: Starting year.
- **`end_year`**: Ending year.

### Example:
```python
base_input_path = "/DATASETS/TEDACS/inputs"
base_output_path = "/DATASETS/TEDACS/outputs"

process_multiple_years(1993, 2019, 1062.44, base_input_path, base_output_path)
```

---

3. 
