from os import path
import ezdxf
from openpyxl import Workbook, load_workbook
import datetime

import tkinter
import tkinter.filedialog



def GetDXFData():

    DXFFile = tkinter.filedialog.askopenfilename(title = 'Select DXF files containing points', filetypes = [('DXF files', '*.dxf')])

    Dir = path.dirname(DXFFile)

    doc = ezdxf.readfile(DXFFile)

    msp = doc.modelspace()
    Mleaders = msp.query("MULTILEADER")
    
    Point = 12 # FIRST POINT NUMBER
    PointText = ""

    for i in Mleaders:
        ws.cell(row = Row, column = Column + 2).value = i.context.plane_origin[1]
    
    
        if Point < 10:
            PointText = "00" + str(Point)
            
        elif Point < 100:
            PointText = "" + str(Point)
            
        else:
            PointText = str(Point)
    
        i.context.mtext.default_content = "SP-22C-10" + PointText
        
        Point += 1
        
    # zoom.extents(msp)

    doc.saveas(Dir + "/" + "Teste" + str(datetime.datetime.now()).replace(":", "-") + ".dxf")
    
GetDXFData()