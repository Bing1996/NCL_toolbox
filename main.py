import dataInitial as dil
import visualization as vis
import dataProcess as dps
import numpy as np
import Ngl , os

os.system('clear')

#dil.download(2020 , 10 , 26 , "12:00")

workDir = '/home/bing/code/NCL_toolbox'

StatesFile = workDir + '/us_shapefile/cb_2018_us_state_5m.shp'
CountyFile = workDir + '/us_shapefile/cb_2018_us_county_5m.shp'
filename = 'download.nc'
output = '/home/bing/code/draft.png'
State = 'TX'

temp , lon , lat = dil.accessData(filename)
temp = np.array(temp , dtype = 'int32') * 0.0012
State_lon , State_lat = dil.accessShp_2(StatesFile , 4 , State)

temp, newlon, newlat = dps.dataMatch(temp , lon , lat , State_lon, State_lat , 0.25)
wks_type = 'png'
wks = Ngl.open_wks(wks_type , output)
res = Ngl.Resources()

res = vis.zoomToDomain(res , temp ,newlon , newlat)
temp , res = dps.mask(temp , res, newlon , newlat , State_lon , State_lat)
map = Ngl.contour_map(wks,temp,res)
vis.polyline(wks , map , State_lon , State_lat)
vis.drawCity(CountyFile , 0, '48' , wks , map)

Ngl.draw(map)
Ngl.frame(wks)
del map
del res
Ngl.end()
