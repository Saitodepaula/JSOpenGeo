from os import path
import ezdxf
from pyproj import Proj
from pykml.factory import KML_ElementMaker as KML
from lxml import etree
import datetime

def MakeKML(Zone, isSouth, DXFFile):

    Dir = path.dirname(DXFFile)

    doc = ezdxf.readfile(DXFFile)

    msp = doc.modelspace()
    Mleaders = msp.query("MULTILEADER")

    p = Proj(proj = 'utm', zone = Zone, south = isSouth, ellps = 'WGS84', preserve_units = False)
    
    folder = KML.Folder()

    # READ DXF DATA AND WRITE TO KML FILE
    for i in Mleaders:
        Name = i.context.mtext.default_content
        X1 = i.context.plane_origin[0]
        Y1 = i.context.plane_origin[1]
        
        X2, Y2 = p(X1, Y1, inverse = True)
    
        coordinates = str(X2) + "," + str(Y2)
    
        NewPoint = KML.Placemark(
             KML.name(Name),
             KML.Point(
                KML.coordinates(coordinates)
                )
            )
            
        folder.append(NewPoint)
        
    # convert the object tree into a string and write it into an output file
    with open(Dir + "/" + str(datetime.datetime.now()).replace(":", "-") + '.kml', 'wb') as file:
        file.write(etree.tostring(folder, pretty_print = True))