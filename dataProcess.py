import Ngl
import os
import numpy as np
import math

def dataMatch(data , lon , lat , shape_lon , shape_lat , resolution):
    for i in range(len(lat)):
        if lat[i] < np.max(shape_lat):
            latStart = i - 1
            break
    for i in range(len(lon)):
        if lon[i] > np.min(shape_lon):
            lonStart = i - 1
            break
    latLength = math.ceil(np.max(shape_lat) - np.min(shape_lat)) / resolution + 2
    lonLength = math.ceil(np.max(shape_lon) - np.min(shape_lon)) / resolution + 2
    data = data[latStart:latStart+int(latLength) , lonStart:lonStart+int(lonLength)]
    newlon = lon[lonStart:lonStart+int(lonLength)]
    newlat = lat[latStart:latStart+int(latLength)]
    return data , newlon , newlat

def mask(data , res ,  lon , lat , shape_lon , shape_lat):
    MissValue = -99999
    for i in range(len(lon)):
        for j in range(len(lat)):
            #print(Ngl.gc_inout(lat[j] , lon[i] , shape_lat , shape_lon))
            if Ngl.gc_inout(lat[j] , lon[i] , shape_lat , shape_lon)[0] == 0:
                data[j][i] = MissValue
    res.sfMissingValueV = MissValue
    return data , res
