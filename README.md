# etaCarnot

Processing and Visualization of TEDACS Data

# Description

This project provides functions for processing, transforming, and visualizing ocean thermal efficiency data ηCarnotηCarnot​ in NetCDF and CSV formats. It includes tools to handle multiple years of data, perform monthly calculations, and plot maps.

# Data availability

**Data name**: Thermal Efficiency Dataset Around Cuban Seas (TEDACS).

**Version**: v1.0

**Repository name**: Science Data Bank.

**Dataset DOI**:  10.57760/sciencedb.10037

**Link to access the data**: https://www.scidb.cn/en/detail?dataSetId=c36d48ae4d5444e69458e9c80fea84dc

**Publication date**: 2023-08-10

**Access link to the certificate**: https://cert.scichain.cn/scidb/2023/08/11/1078085787.en.v1.pdf

# Cite this data as

Rodriguez, A., Abreu, M., Dailin Reyes, Abreu, M., Calzada, A. E., Varona, H. L., Noriega, C., & Moacyr Araujo. (2023). Thermal Efficiency Dataset Around Cuban Seas (TEDACS) (Version V1) [Dataset]. Science Data Bank. https://doi.org/10.57760/SCIENCEDB.10037 

These data Data and this software are made available under the terms of the Creative Commons Attribution 4.0 International License (CC-BY 4.0).

Software for the creation of the ocean thermal efficiency database:



# Dependencies

Ensure you have the following libraries installed:

- **Pandas**
- **NumPy**
- **Xarray**
- **Matplotlib**
- **Cartopy**
- **SciPy** 

Install them with:

```sh
pip install pandas numpy xarray matplotlib cartopy scipy
```

# Main functions

## 1. get_time_index(nc_file, target_date)

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

## 2. `process_multiple_years(start_year, end_year, depth, base_input_path, base_output_path)`

Processes multiple years of CSV data and saves the results as yearly NetCDF files.

### Parameters:

- **`input_dir`**: Directory containing the input CSV files.
- **`output_dir`**: Directory for the output NetCDF files.
- **`depth`**: Depth = [763.33, 910.33, 1062.44].
- **`start_year`**: Starting year.
- **`end_year`**: Ending year.

### Returns:

    None

### Example:

```python
base_input_path = "/DATASETS/TEDACS/inputs"
base_output_path = "/DATASETS/TEDACS/outputs"

process_multiple_years(1993, 2019, 1062.44, base_input_path, base_output_path)
```

---

## 3. `process_and_save_all_years(start_year, end_year, depth, base_input_path, output_file)`

Processes and saves data from multiple years as a NetCDF file.

#### Parameters:

- **`input_dir`**: Directory containing the input CSV files.
- **`output_dir`**: Directory for the output NetCDF files.
- **`depth`**: Depth = [763.33, 910.33, 1062.44].
- **`start_year`**: Starting year.
- **`end_year`**: Ending year.

### Returns:

    None
    
### Example:

```python
base_input_path = "/DATASETS/TEDACS/inputs"
output_file = "/DATASETS/TEDACS/outputs"

process_and_save_all_years(1993, 2019, 763.333, base_input_path, output_file) 
```

---

## 4. `read_eta_at_time_and_depth(file_path, time_index, depth_index)`

Reads a NetCDF file and extracts `eta` at a specific time and depth.

### Parameters:

- **`file_path`**: Path to the NetCDF file.
- **`time_index`**: Time index to read.
- **`depth_index`**: Depth index to read.

### Returns:

- **`eta`**: 2D data (latitude, longitude).
- **`longitude`**: Longitude coordinates. 
- **`latitude`**: Latitude coordinates.

### Example:

```python
nc_file = "/DATASETS/TEDACS/inputs/763m.nc"
target_date = "1993-02-14"
time_index = get_time_index(nc_file, target_date)
depth_index = 0

eta, lon, lat = read_eta_at_time_and_depth(nc_file, time_index, depth_index)
```

---   

## 5. `plot_eta_map(eta_2d, longitude, latitude, title="Map of Eta", colormap="viridis", cb_orientation="vertical", font_sizes=None, value_range=None, save_path=None)`

Plots a map of $\eta_{\mathrm{Carnot}}$ with customizable features.

#### Parameters:

- **`eta_2d`**: 2D data (latitude, longitude).
- **`longitude`**: Longitude coordinates.
- **`latitude`**: Latitude coordinates.
- **`title`**: Map title.
- **`colormap`**: Colormap to use.
- **`cb_orientation`**: Colorbar orientation.
- **`font_sizes`**: Dictionary for customized font sizes.
- **`value_range`**: Value range for the plot.
- **`save_path`**: Path to save the image.

### Returns:

    None
    
#### Example:

```python
nc_file = "/DATASETS/TEDACS/inputs/763m.nc"
target_date = "1993-02-14"
time_index = get_time_index(nc_file, target_date)
depth_index = 0

eta, lon, lat = read_eta_at_time_and_depth(nc_file, time_index, depth_index)

sp = "/DATASETS/TEDACS/outputs/figures/01_763m_1993-02.png"

plot_eta_map(eta, lon, lat, title="Date: Feb-1993, Depth: 763m", colormap="viridis", cb_orientation="horizontal",
    font_sizes={"title": 14, "labels": 12, "colorbar": 12}, value_range=(0.55, 0.85, 15), save_path=sp)
```

---  

## Author

This project was developed by **Humberto L. Varona**. For questions or inquiries, contact **humberto.varona@ufpe.br**.

---

### Thank you for using this project! 😊 



