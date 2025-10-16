import xarray as xr
import datetime
import numpy as np
import pandas as pd

def read_latest_sst(file):
    sst_ds = xr.load_dataset(file)
    sst_latest = sst_ds["sst"].isel(time=-1).values
    sst_ds.close()
    return sst_latest


def get_time_series_at_coordinate_latest_sst(latitude, longitude, dataset_path):
    sst_ds = xr.load_dataset(dataset_path)
    sst = sst_ds['sst']
    time = sst_ds['time']
    return time, sst[:, latitude, longitude]


def load_time(dataset_path):
    sst_ds = xr.load_dataset(dataset_path)
    time_raw = sst_ds["time"].values
    
    if np.issubdtype(time_raw.dtype, np.datetime64):
        datetime_vector = [pd.to_datetime(t).to_pydatetime() for t in time_raw]
    else:
        base_date = datetime.datetime(1891, 1, 1)
        datetime_vector = [base_date + datetime.timedelta(days=float(t)) for t in time_raw]
        
    sst_ds.close()
    return datetime_vector


