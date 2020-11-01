#!/usr/bin/env python
import cdsapi
import os
import Nio
import Ngl
import shapefile as shp
import numpy as np

def getInfo(file , variable):
    miss = file.variables[variable]._FillValue[0]
    scale = file.variables[variable].scale_factor[0]
    add = file.variables[variable].add_offset[0]
    return miss , scale , add

def accessData(filename , variable):
    data_dir  = Ngl.pynglpath("data")
    file = Nio.open_file(os.path.join(data_dir,filename),"r")
    print(file)
    data = file.variables[variable][:]
    data = data[0,:,:]
    data_lon = file.variables['longitude'][:]
    data_lat = file.variables['latitude'][:]
    return file , data , data_lon , data_lat

def download(year , month , day , time):
    c = cdsapi.Client()
    c.retrieve("reanalysis-era5-pressure-levels",
    {
    "variable": "temperature",
    "pressure_level": "1000",
    "product_type": "reanalysis",
    "year": str(year),
    "month": str(month),
    "day": str(day),
    "time": time,
    "format": "netcdf"
    },
    "/home/bing/miniconda3/envs/pyn_env/lib/python3.8/site-packages/ngl/ncarg/data/download.nc")

def accessShp_2(filenameArea , Index_area , area):
    print(filenameArea)
    file = shp.Reader(filenameArea)
    shapes = file.shapes()
    records = file.records()
    shape_city = np.zeros((1,2))
    for i in range(len(records)):
        if area in records[i][Index_area]: #Fliter the Area
            print(records[i])
            shape_city = np.vstack((shape_city , np.array(shapes[i].points)))
    shape_city = np.delete(shape_city , 0 ,0)

    shape_lon = shape_city[:,0]
    shape_lat = shape_city[:,1]
    for i in range(len(shape_lon)):
        if shape_lon[i] < 0: shape_lon[i] = shape_lon[i] + 360


    print(np.shape(shape_city))
    return shape_lon , shape_lat
