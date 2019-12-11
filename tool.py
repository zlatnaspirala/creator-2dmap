#!/usr/bin/python3
###############################################################################
# Imports
###############################################################################
import os
from map import myMap
from models.ground import StaticGrounds
from defaults import InitialData
import tkinter
import json
from tkinter import BOTH, StringVar, messagebox
from functools import partial
import subprocess
import json
import PIL
from PIL import ImageTk, Image
from common.stickler import Stickler

###############################################################################
# Define window object, Map instance, general screen w/h
###############################################################################
window = tkinter.Tk()
window.title("GUI tool creator-2dmap for vtge")

defaultTexture = "imgs/texx.png"
# virtual path
# defaultTextureTool = ImageTk.PhotoImage(file='resource/texx.png')
# anchor="nw"
# img = Image.open("resource/texx.png")
# img.resize((100,22), Image.ANTIALIAS)
# defaultTextureTool = ImageTk.PhotoImage(img)

# ImageTk.PhotoImage(Image.open("resource/nik.jpg"))
# panel = tkinter.Label(window, image=defaultTexture)
# panel.pack(side="bottom", fill="both", expand="yes")

###############################################################################
# Setup dimension for window
###############################################################################
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.geometry(str(screen_width) + "x" + str(screen_height))

###############################################################################
# Define myMap object and instance initial data object
###############################################################################
initValues = InitialData()
MyDefaultMap = myMap("MyDefaultMap", initValues)
editorStickler = Stickler(initValues)

topFrame = tkinter.Frame(window,
                         background=initValues.topFrameBackgroundColor,
                         height=screen_height,
                         width=110)
topFrame.pack(side="left", in_=window)

###############################################################################
# UI left box - Width Height
###############################################################################
# Width & Height
varLabelTextW = StringVar()
varLabelTextW.set("width:20")

varLabelTextH = StringVar()
varLabelTextH.set("height:20")

# View UI tool
# setup width
def wplus():
  initValues.ELEMENT_WIDTH = initValues.ELEMENT_WIDTH + initValues.incDecWidth
  varLabelTextW.set("width:"+ str(initValues.ELEMENT_WIDTH))

widthPlus = tkinter.Button(
    window, text="+", fg="red", bg="black", command=wplus)
widthPlus.place(x=0, y=20, height=25, width=50, in_=topFrame)

def wminus():
  initValues.ELEMENT_WIDTH = initValues.ELEMENT_WIDTH - initValues.incDecWidth
  varLabelTextW.set("Width:" + str(initValues.ELEMENT_WIDTH))

widthMinus = tkinter.Button(
    window, text="-", fg="red", bg="black", command=wminus)
widthMinus.place(x=50, y=20, height=25, width=50, in_=topFrame)

labelWidth = tkinter.Label(window, textvariable=varLabelTextW)
labelWidth.place(x=0, y=0, width=100, height=20, in_=topFrame)

# for height
labelHeight = tkinter.Label(window, textvariable=varLabelTextH)
labelHeight.place(x=0, y=45, width=100, height=20, in_=topFrame)

def hplus():
  initValues.ELEMENT_HEIGHT = initValues.ELEMENT_HEIGHT + initValues.incDecHeight
  varLabelTextH.set("Height:" + str(initValues.ELEMENT_HEIGHT))

heightPlus = tkinter.Button(
    window, text="+", fg="red", bg="black", command=hplus)
heightPlus.place(x=0, y=63, height=25, width=50, in_=topFrame)

def hminus():
  initValues.ELEMENT_HEIGHT = initValues.ELEMENT_HEIGHT - initValues.incDecHeight
  varLabelTextH.set("Height:" + str(initValues.ELEMENT_HEIGHT))

heightMinus = tkinter.Button(
    window, text="-", fg="red", bg="black", command=hminus)
heightMinus.place(x=50, y=63, height=25, width=50, in_=topFrame)

###############################################################################
# Left box - tiles
###############################################################################
varLabelTextTileX = StringVar()
varLabelTextTileX.set("tileX:" + str(initValues.tilesX))

varLabelTextTileY = StringVar()
varLabelTextTileY.set("tileY:" + str(initValues.tilesY))

# View UI tool
# For tilesX
def tileXplus():
  initValues.tilesX = initValues.tilesX + 1
  varLabelTextTileX.set("tileX:"+ str(initValues.tilesX))

tileXPlus_ = tkinter.Button(window, text="+", command=tileXplus)
tileXPlus_.place(x=0, y=110, height=25, width=50, in_=topFrame)

def tileXminus():
  if initValues.tilesX > 1:
    initValues.tilesX = initValues.tilesX - 1
  varLabelTextTileX.set("tileX:" + str(initValues.tilesX))

tileXMinus_ = tkinter.Button(window, text="-", command=tileXminus)
tileXMinus_.place(x=50, y=110, height=25, width=50, in_=topFrame)

labelTileX = tkinter.Label(window, textvariable=varLabelTextTileX)
labelTileX.place(x=0, y=90, width=100, height=20, in_=topFrame)

# for tilesY
labelTileY = tkinter.Label(window, textvariable=varLabelTextTileY)
labelTileY.place(x=0, y=135, width=100, height=20, in_=topFrame)

def tileYplus():
  initValues.tilesY = initValues.tilesY + 1
  varLabelTextTileY.set("tileY:" + str(initValues.tilesY))

tileYPlus = tkinter.Button(window, text="+", command=tileYplus)
tileYPlus.place(x=0, y=155, height=25, width=50, in_=topFrame)

def tileYminus():
  if initValues.tilesY > 1:
    initValues.tilesY = initValues.tilesY - 1
  varLabelTextTileY.set("tileY:" + str(initValues.tilesY))

tileYMinus = tkinter.Button(window, text="-", command=tileYminus)
tileYMinus.place(x=50, y=155, height=25, width=50, in_=topFrame)

###############################################################################
# Left box - Rotate values
###############################################################################
varLabelRotatedValues = StringVar()
varLabelRotatedValues.set("Rotated values:" + str(initValues.rotateValues))

def rotatedValuesMethod():
  print("Rotated values")
  localH = initValues.ELEMENT_HEIGHT
  initValues.ELEMENT_HEIGHT = initValues.ELEMENT_WIDTH
  initValues.ELEMENT_WIDTH = localH

rotatedValuesControl = tkinter.Button(window, textvariable=varLabelRotatedValues, command=tileYminus)
rotatedValuesControl.place(x=0, y=180, height=25, width=100, in_=topFrame)



# Add new element method
def addNewElements(loadedMap):
  for element in loadedMap:
    localModel = StaticGrounds(element['x'],
                               element['y'],
                               element['w'],
                               element['h'],
                               element['tex'],
                               element['tiles']['tilesX'],
                               element['tiles']['tilesY'])
    MyDefaultMap.add(localModel)
  drawMap()

# Collect mouse & other data [x,y,w,h,tex]
def collectMouseEventData(event):
  if event.y > 0 and event.x > 70:
    print("clicked at", event.x, event.y)
    x = event.x
    y = event.y
    local = "x:" + str(event.x) + ", y:" + str(event.y)
    appCoordinate.configure(text=local)

    if initValues.stickler["enabledX"] == True:
      x = editorStickler.recalculateX(x)
      print("Enabled X stickler.")

    if initValues.stickler["enabledY"] == True:
      y = editorStickler.recalculateY(y)
      print(" Y ")

    localModel = StaticGrounds(x,
                               y,
                               initValues.ELEMENT_WIDTH,
                               initValues.ELEMENT_HEIGHT,
                               defaultTexture,
                               initValues.tilesX,
                               initValues.tilesY)
    MyDefaultMap.add(localModel)
    drawMap()

window.bind("<Button-1>", collectMouseEventData)

###############################################################################
# Menu Events
###############################################################################
root_menu = tkinter.Menu(window)
window.config(menu=root_menu)

def myEvent():
  print("Menu tab pressed...")

def undoRemoveLast():
  MyDefaultMap.removeLast()
  canvas.delete("all")
  drawMap()
  print("undo")

def menuEventClearMap():
  if messagebox.askokcancel("Clear map", "Do you really wish to clear map?"):
    MyDefaultMap.clear()
    canvas.delete("all")
    drawMap()
    print("Clear map")

def menuEventSaveMap():
  print(MyDefaultMap.map)
  MyDefaultMap.prepareForSave()
  json_string = json.dumps(MyDefaultMap.exportMap)
  print(os.getcwd(), os.path.abspath(__file__))
  with open("map2d.creator", "w", newline='\r\n') as write_file:
    json.dump(json.loads(json_string), write_file , indent=2)
    print("Map saved.")

def menuEventExportMap():
  print(MyDefaultMap.map)
  MyDefaultMap.prepareForExport()
  json_string = json.dumps(MyDefaultMap.exportMap2)
  print(os.getcwd(), os.path.abspath(__file__))
  exportPathName = "map2d.ts"
  # absolutePacksPath
  if initValues.absolutePacksPathEnabled == True:
    exportPathName = initValues.absolutePacksPath + exportPathName
    print("Save export intro absolute path.")
  with open(str(exportPathName), "w", newline='\r\n', ) as write_file:
    json_string = json_string.replace("[", "let grounds_generated = [")
    json_string = json_string.replace("]", "]; export default grounds_generated;")
    if initValues.exportInOneLine == False:
      json_string = json_string.replace("," , ", \n ")
    write_file.write(json_string)
    # json.dump(json.loads(json_string), write_file , indent=2)
    print("Map saved.")

def menuEventLoadMap():
  with open('map2d.creator', 'r') as loadedMap:
    rawString = loadedMap.read()
    rawString = rawString.replace('[', '{ "root" : [')
    rawString = rawString.replace("]", "]}")
    json_data = json.loads(rawString)
    json_data = json_data['root']
    addNewElements(json_data)

# About
def showAbout():
  messagebox.showinfo("About", """
    Original source project `creator-2dmap` ver 0.1 \n
    2019/2020 Copyright Nikola Lukic \n
    created by Nikola Lukic zlatnaspirala@gmail.com \n \n
    LICENCE: \n
    GNU LESSER GENERAL PUBLIC LICENSE Version 3 \n
    https://github.com/zlatnaspirala/creator-2dmap \n
  """)

def showGrid():
  print("showGrid")
  if initValues.canvasGridVisible == True:
    initValues.canvasGridVisible = not initValues.canvasGridVisible
    options_menu.entryconfigure(1, label="Show Grid's")
    drawMap()
  else:
    initValues.canvasGridVisible = not initValues.canvasGridVisible
    options_menu.entryconfigure(1, label="Hide Grid's")
    drawMap()

# Quic terminate event
def terminate_app():
  if messagebox.askokcancel("Quit", "Do you really wish to quit?"):
    window.destroy()

# creating sub menus in the root menu
file_menu = tkinter.Menu(root_menu)
# it creates the name of the sub menu
root_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Load map", command=menuEventLoadMap)
file_menu.add_command(label="Save map", command=menuEventSaveMap)
file_menu.add_command(label="Export map", command=menuEventExportMap)
file_menu.add_separator()
file_menu.add_command(label="Clear map", command=menuEventClearMap)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=terminate_app)
# sub menu
edit_menu = tkinter.Menu(root_menu)
root_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Undo last added", command=undoRemoveLast)
edit_menu.add_command(label="Redo last added", command=myEvent)

# Options menu
options_names = {}
options_names["showGrid"] = "Show Grid"
options_names["DSticklerX"] = "Disable stick by X"
options_names["DSticklerY"] = "Disable stick by Y"

def DSticklerX():
  if options_names["DSticklerX"] == "Enable stick by X":
    options_names["DSticklerX"] = "Disable stick by X"
  else:
    options_names["DSticklerX"] = "Enable stick by X"

  initValues.setSticklerEnabledX()
  stickler_menu.entryconfigure(1, label=options_names["DSticklerX"])

def DSticklerY():
  if options_names["DSticklerY"] == "Enable stick by Y":
    options_names["DSticklerY"] = "Disable stick by Y"
  else:
    options_names["DSticklerY"] = "Enable stick by Y"

  initValues.setSticklerEnabledY()
  stickler_menu.entryconfigure(2, label=options_names["DSticklerY"])

options_menu = tkinter.Menu(root_menu)
root_menu.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label=options_names["showGrid"], command=showGrid)
stickler_menu = tkinter.Menu(options_menu)
options_menu.add_cascade(label="Sticklers", menu=stickler_menu)
stickler_menu.add_command(label=options_names["DSticklerX"], command=DSticklerX)
stickler_menu.add_command(label=options_names["DSticklerY"], command=DSticklerY)

# about
about_menu = tkinter.Menu(root_menu)
root_menu.add_cascade(label="About", menu=about_menu)
about_menu.add_command(label="creator-map2d", command=showAbout)

# GUI Labels
appCoordinate = tkinter.Label(window, text="Coordinator")
# appCoordinate.configure(background="#000000")
appCoordinate.place(x=screen_width-150, y=0, height=30, width=150)
# appCoordinate.pack()

# Canvas element
canvas = tkinter.Canvas(
    window,
    width=screen_width - 110,
    height=screen_height - 110,
    background=initValues.windowBackgroundColor
  )
canvas.place(x=100, y=20, width=screen_width - 115, height=screen_height - 130)
print("Screen size: ", screen_width , screen_height, sep="-")
# canvas.delete(line1)
# canvas.delete(tkinter.ALL)

###############################################################################
# Re Draw map element's
###############################################################################
def drawMap():
  print("Clear canvas.")
  canvas.delete("all")
  if initValues.canvasGridVisible == True:
    print("Draw Map Grid.")
    for x in range(100, screen_width, initValues.gridWidth):
      line1 = canvas.create_line(0, x, screen_width, x, fill="orange")
      line2 = canvas.create_line(x, 0, x, screen_width, fill="red")

  for element in MyDefaultMap.map:
    canvas.create_rectangle(element.x, element.y, element.x2, element.y2, fill="blue")
    # ttt = canvas.create_image(element.x, element.y, anchor="nw", image=defaultTextureTool, height = 20, width = 200)
    # canvas.itemconfig(ttt, image=defaultTextureTool) ?

drawMap()

###############################################################################
# Files operation test
###############################################################################

#command = 'echo "$(pwd)"'
#process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
#output, error = process.communicate()
#print("Output", output)

window.mainloop()
