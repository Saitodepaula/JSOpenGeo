from os import path
import ezdxf
from ezdxf import zoom
import datetime

import tkinter
import tkinter.filedialog

'''

Generates Kilometers markers along a line

'''

def GenerateKms():

    DXFFile = tkinter.filedialog.askopenfilename(title = 'Select DXF files containing points', filetypes = [('DXF files', '*.dxf')])

    Dir = path.dirname(DXFFile)

    # Create a new DXF R2010 drawing, official DXF version name: "AC1024"
    doc = ezdxf.new('R2010')

    # Add new entities to the modelspace:
    msp = doc.modelspace()
    
    FinalKm = 160
    
    ATTRIBS = {
    "char_height": 100.0,
    }

    for number in range(0, FinalKm):
        Text = str(number)
        Text = Text + "+000"
        
        X = number * 1000
       
        attribs = dict(ATTRIBS)
        location = (X,0)
        
        MText = msp.add_mtext(Text, attribs).set_location(insert = location, attachment_point = 2)
     
    zoom.extents(msp)

    doc.saveas(Dir + "/" + "KmsPlot" + str(datetime.datetime.now()).replace(":", "-") + ".dxf")
    
GenerateKms()