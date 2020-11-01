import dataInitial as dil
import visualization as vis
import dataDownload as ddl
import dataProcess as dps
import numpy as np
import Ngl , os
import Nio


filename = 'download.nc'
data_dir  = Ngl.pynglpath("data")
file = Nio.open_file(os.path.join(data_dir , filename),"r")
print(file)

miss , scale , add = dil.getInfo(file , "t2m")
print(miss , scale , add)
