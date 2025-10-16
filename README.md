Overview:
This repository contains a set of python functions called "Cobe_functions" meant to process sea surface temperature (sst) data. The functions use xarray, pandas, and numpy libraries.

Requirements: 
The code assumes that you are working with NetCDF files that contain a sst variable and a time coordinate.

Functions Included: 
read_latest_sst(file)
  This function loads a specified dataset and extracts the sst data for the most recent time step.
  Inputs:
    file, the path to the dataset file.
  Returns:
    A numpy.ndarray containing the SST values for the latest time step.

get_time_series_at_coordinate_latest_sst(latitude, longitude, dataset_path)
  This function extracts the entire time series of SST data for a specified latitude and longitude.
  Inputs:
    latitude, the integer index of the latitude for the desired location.
    longitude, the integer index of the longitude for the desired location.
    dataset_path, the path to the dataset file.
  Returns:
    A tuple containing, an xarray.DataArray of the time coordinate, an xarray.DataArray of the SST time series at the specified coordinate.

load_time(dataset_path)
  This function loads the time coordinate data from a dataset and converts it into a list of standard Python datetime.datetime objects. 
  Parameters:
    dataset_path (str), the path to the dataset file.
  Returns:
    A list of datetime.datetime objects representing the time steps in the dataset.

Usage examples are also included in the repository for user reference. 
