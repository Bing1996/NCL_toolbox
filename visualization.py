import Ngl
import numpy as np
import shapefile as shp

def zoomToDomain(res , data , newlon , newlat):
    res.nglFrame            = False
    res.nglDraw             = False

    res.vpXF      = 0.1    # Change the size and location of the
    res.vpYF      = 0.9    # plot on the viewport.
    res.vpWidthF  = 0.7
    res.vpHeightF = 0.7

    res.cnFillOn          = True          # turn on contour fill
    res.cnLinesOn         = False         # turn off contour lines
    res.cnLineLabelsOn    = False         # turn off line labels
    #res.cnLevelSpacingF   = 2.5           # NCL chose 5.0
    #res.cnFillPalette     = "WhiteBlueGreenYellowRed"

    res.cnLevelSelectionMode = 'ManualLevels'
    print(int(data.min()) , int(data.max()))
    res.cnMinLevelValF = int(data.min())
    res.cnMaxLevelValF = int(data.max())
    res.cnLevelSpacingF = 1

    res.mpLimitMode         = "Corners"   # limit map via two opposite corners
    res.mpLeftCornerLatF    = np.min(newlat)          # left corner
    res.mpLeftCornerLonF    = np.min(newlon)       # left corner
    res.mpRightCornerLatF   = np.max(newlat)          # right corner
    res.mpRightCornerLonF   = np.max(newlon)

    res.sfXArray = newlon
    res.sfYArray = newlat

    #res.pmLabelBarDisplayMode = "Never"

    #print(np.min(lat),np.min(lon),np.max(lat),np.max(lon))

    return res

def polyline(wks , map , shape_lon , shape_lat):
    lnres = Ngl.Resources()
    lnres.gsLineColor = "black"
    lnres.gsLineThicknessF = 3.0
    lnid = Ngl.add_polyline(wks , map , shape_lon , shape_lat , lnres)

def drawCity(filenameArea , Index_area , area , wks , map):
    file = shp.Reader(filenameArea)
    shapes = file.shapes()
    records = file.records()
    for i in range(len(records)):
        if area in records[i][Index_area]:
            cityInfo = np.array(shapes[i].points)
            shape_lon = cityInfo[:,0]
            shape_lat = cityInfo[:,1]
            polyline(wks , map , shape_lon , shape_lat)
