import cdsapi
from ecmwfapi import ECMWFDataServer
import os

def download(type , variable ,  year , month , day , time):
    c = cdsapi.Client()
    c.retrieve(type,
    {
    "variable": variable,
    #"pressure_level": "1000",
    #"product_type": "reanalysis",
    "year": year,
    "month": month,
    "day": day,
    "time": time,
    "format": "netcdf"
    },
    "/home/bing/miniconda3/envs/pyn_env/lib/python3.8/site-packages/ngl/ncarg/data/download.nc")

def areaDownload(type , variable , year , month , day , time , lon, lat):
    print(lon.min() , lon.max())
    c = cdsapi.Client()
    c.retrieve(type,
    {
    "variable": variable,
    #"pressure_level": "1000",
    "product_type": "reanalysis",
    "year": year,
    "month": month,
    "day": day,
    "time": time,
    "format": "netcdf",
    "area": [lat.max() + 2.5 , lon.min() - 2.5 , lat.min() - 2.5 , lon.max() + 2.5],
    },
    "/home/bing/miniconda3/envs/pyn_env/lib/python3.8/site-packages/ngl/ncarg/data/download.nc")
