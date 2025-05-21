import tkinter
import tkinter.filedialog
from tkinter import ttk
# from PIL import Image, ImageTk

import DXFToExcel_JS
import DXFToKML_JS
import ExcelToDXF_JS
import ExcelToKML_JS
# import KMLToExcel_JS


# ============================================================================================================

#DEPENDENCIES

#EZDXF
#OPENPYXL
#PYPROJ
#PYKML

#TODO

# Recognize and deal with empty lines

# KML

# Add UTM zone selection and south or north hemmisphere
# Add map to select UTM zone or find zone by address

# EXCEL TO KML OR DXF

# Add option to skip lines (heading)
# Add option to choose columns containing data
# Add spreadsheet preview

# Add palitos de sondagem DXF from Excel
# Add borehole PDF automated reading to Excel
# Add rocks and soils parameters and data, with citation (like RocData)
# Add stereonet and kinematic analysis
# In the RENAME DXF POINTS, add option of number to start counting

# https://matplotlib.org/stable/gallery/mplot3d/rotate_axes3d_sgskip.html
# https://github.com/joferkington/mplstereonet
# https://plotly.com/graphing-libraries/
# https://github.com/rodreras/geopy_minicurso
# https://github.com/kevinalexandr19/manual-python-geologia

# CREATE EXE FILE

# Pyinstaller
# Auto py to exe

# create exe file and run it from inside Godot?

# ============================================================================================================

root = tkinter.Tk()
root.title('JS Open Geo')

# root.iconbitmap("JS_PlotarPonto_256.ico")
#root.iconbitmap(r"C:\Users\msait\OneDrive\ProjetosJS\JSOpenGeo\JS_OpenGeo.ico")
root.iconbitmap("E:\On-Line\ProjetosJS\JSOpenGeo")

#JS_logo = tkinter.PhotoImage(file = r"C:\Users\msait\OneDrive\ProjetosJS\JSOpenGeo\JS_Logo_horiz_small_white_outline.png")
JS_logo = tkinter.PhotoImage(file = r"E:\On-Line\ProjetosJS\JSOpenGeo\JS_Logo_horiz_small_white_outline.png")

def DXFToExcel():

    DXFFile = tkinter.filedialog.askopenfilename(title = 'Select DXF files containing points', filetypes = [('DXF files', '*.dxf')])

    if not DXFFile:
        pass
        
    else:
        DXFToExcel_JS.GetDXFData(DXFFile)
        
        tkinter.messagebox.showinfo(title = "Excel file created", message = "The Excel file is saved in the same directory of your DXF file, with date and time in the name of the file")    
        
def DXFToKML():
    DXFFile = tkinter.filedialog.askopenfilename(title = 'Select DXF files containing points', filetypes = [('DXF files', '*.dxf')])

    if not DXFFile:
        pass
        
    else:
        DXFToKML_JS.MakeKML(23, True, DXFFile) 

        tkinter.messagebox.showinfo(title = "KML file created", message = "The KML file is saved in the same directory of your DXF file, with date and time in the name of the file")    
        
def ExcelToDXF():

    ExcelFile = tkinter.filedialog.askopenfilename(title = 'Select Excel files containing points data', filetypes = [('Excel files', '*.xlsx'), ('Excel files', '*.xls')])

    if not ExcelFile:
        pass
        
    else:
        ExcelToDXF_JS.GetExcelData(ExcelFile)
        
        tkinter.messagebox.showinfo(title = "DXF file created", message = "The DXF file is saved in the same directory of your Excel file, with date and time in the name of the file")    
            
def ExcelToKML():
    ExcelFile = tkinter.filedialog.askopenfilename(title = 'Select Excel files containing points data', filetypes = [('Excel files', '*.xlsx'), ('Excel files', '*.xls')])
        
    if not ExcelFile:
        pass
        
    else:
        ExcelToKML_JS.MakeKML(33, True, ExcelFile) 

        tkinter.messagebox.showinfo(title = "KML file created", message = "The KML file is saved in the same directory of your Excel file, with date and time in the name of the file")    
        
def KMLToExcel():

    KMLFile = tkinter.filedialog.askopenfilename(title = 'Select KML file containing points', filetypes = [('KML files', '*.kml')])

    if not KMLFile:
        pass
        
    else:
        KMLToExcel_JS.GetKMLData(KMLFile)
        
        tkinter.messagebox.showinfo(title = "Excel file created", message = "The Excel file is saved in the same directory of your DXF file, with date and time in the name of the file")    
      

DXFToExcelText = """Extract coordinates from a DXF file and creates an Excel file with the data.
Look at the DXFPointsExample.dxf file (that comes together with JS Open Geo) for reference of how to format the drawing.
The points must use MULTILEADER objects."""

DXFToKMLText = """Extract coordinates from a DXF file and creates a KML (Google Earth) file with the data.
Look at the DXFPointsExample.dxf file (that comes together with JS Open Geo) for reference of how to format the drawing.
The points must use MULTILEADER objects."""

ExcelToDXFText = """Take points data from an Excel file and creates a DXF file. 
Look at the ExcelPointsExample.xlsx file (that comes together with JS Open Geo) for reference of how to format the data.
The data must have this pattern:
COLUMN A - point name
COLUMN B - X coordinate
COLUMN C - Y coordinate"""

ExcelToKMLText = """Take points data from an Excel file and creates a KML (Google Earth) file. 
Look at the ExcelPointsExample.xlsx file (that comes together with JS Open Geo) for reference of how to format the data.
The data must have this pattern:
COLUMN A - point name
COLUMN B - X coordinate
COLUMN C - Y coordinate"""

KMLToExcelText = """Extract coordinates from a KML file (only from points) and creates an Excel file with the data."""

JSTextString = """JS Open Geo is a free and open source software provided by JS Geologia Aplicada | São Paulo | SP | Brazil.
Feedback, opinions and sugestions are welcome.
www.jsgeo.com.br
contato@jsgeo.com.br
"""


s = ttk.Style()
s.theme_use('alt')
s.configure('TFrame', background = '#262c3b')
s.configure('TButton', background = '#262c3b', foreground = 'white', font = ('Noto Sans', 12))
s.configure('TLabel', background = '#262c3b', foreground = 'white', font = ('Noto Sans', 10))
s.map('TButton', background=[('active','#333b4f')])

frm = ttk.Frame(root, padding = (10, 10, 10, 10), style = 'TFrame')
frm.grid()

ttk.Label(frm, image = JS_logo, padding = 10, justify = 'left').grid(row = 0, column = 0)

ttk.Separator(frm, orient = 'horizontal').grid(row = 1, columnspan = 2, sticky = "ew")

# ============================================================================================================

ttk.Button(frm, text = "DXF to Excel", width = 25, command = DXFToExcel, padding = 10).grid(row = 2, column = 0)
ttk.Label(frm, text = DXFToExcelText, padding = 10).grid(row = 2, column = 1, sticky = "w")

ttk.Separator(frm, orient = 'horizontal').grid(row = 3, columnspan = 2, sticky = "ew")

# ============================================================================================================

ttk.Button(frm, text = "DXF to KML", width = 25, command = DXFToKML, padding = 10).grid(row = 4, column = 0)
ttk.Label(frm, text = DXFToKMLText, padding = 10).grid(row = 4, column = 1, sticky = "w")

ttk.Separator(frm, orient = 'horizontal').grid(row = 5, columnspan = 2, sticky = "ew")

# ============================================================================================================

ttk.Button(frm, text = "Excel to DXF", width = 25, command = ExcelToDXF, padding = 10, style = 'TButton').grid(row = 6, column = 0)
ttk.Label(frm, text = ExcelToDXFText, padding = 10, style = 'TLabel').grid(row = 6, column = 1, sticky = "w")

ttk.Separator(frm, orient = 'horizontal').grid(row = 7, columnspan = 2, sticky = "ew")

# ============================================================================================================

ttk.Button(frm, text = "Excel to KML", width = 25, command = ExcelToKML, padding = 10).grid(row = 8, column = 0)
ttk.Label(frm, text = ExcelToKMLText, padding = 10).grid(row = 8, column = 1, sticky = "w")

ttk.Separator(frm, orient = 'horizontal').grid(row = 9, columnspan = 2, sticky = "ew")

# ============================================================================================================

ttk.Button(frm, text = "KML to Excel", width = 25, command = KMLToExcel, padding = 10).grid(row = 10, column = 0)
ttk.Label(frm, text = KMLToExcelText, padding = 10).grid(row = 10, column = 1, sticky = "w")

ttk.Separator(frm, orient = 'horizontal').grid(row = 11, columnspan = 2, sticky = "ew")

# ============================================================================================================

JSText = tkinter.Text(frm, height = 5, borderwidth = 0, font = ('Noto Sans', 10), bg = '#262c3b', fg = 'white')
JSText.tag_configure("center", justify = 'center')
JSText.grid(row = 12, columnspan = 2, sticky = "ew", pady = 10)
JSText.insert(1.0, JSTextString, 'center')
JSText.configure(state = "disabled")
JSText.configure(inactiveselectbackground = JSText.cget("selectbackground"))

root.mainloop()