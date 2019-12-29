#!/usr/bin/python3
#################################################################################
#  creator2dmap is python3 application for creating visuat-ts game engine 2d maps
#  LICENCE: GNU LESSER GENERAL PUBLIC LICENSE Version 3
#  https://github.com/zlatnaspirala/creator-2dmap
#  Code style ~camel
#  Version: 0.2
#  Imports
#################################################################################

import os
from map import myMap
from models.ground import StaticGrounds
from models.collectitems import CollectingItems
from defaults import InitialData
import tkinter
import json
from tkinter import BOTH, StringVar, messagebox, ttk
from functools import partial
import subprocess
import PIL
from PIL import ImageTk, Image
from common.stickler import Stickler
import time
from tkinter import filedialog

###############################################################################
# Define window object, Map instance, general screen w/h
###############################################################################

window = tkinter.Tk()
window.title("GUI tool creator-2dmap for visual-ts game engine")

# Global currentInsertType = "grounds" | "collectItems"
INSERT_TYPE = "grounds"
RESOURCE_INDENTITY = []
RESOURCE_INDENTITY_READONLY = []
RESOURCE_IMAGES_OBJ = []
PREVENT_ADDING = 0

###############################################################################
# Setup dimension for window
###############################################################################

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.geometry(str(screen_width) + "x" + str(screen_height))

###############################################################################
# Define myMap object and instance initial data object
# Also defined frames box's.
###############################################################################

initValues = InitialData()
MyDefaultMap = myMap("MyDefaultMap", initValues)
editorStickler = Stickler(initValues)

topFrame = tkinter.Frame(window,
                         background=initValues.topFrameBColor,
                         height=screen_height,
                         width=110)
topFrame.pack(side="left", in_=window)
topFrame.lift()

resourcePreview = tkinter.Frame(window,
                         background=initValues.resourcePreviewFrameBColor,
                         height=100,
                         width=100)

resourcePreview.place(x=1, y=500, in_=topFrame)

###############################################################################
# UI left box - Width Height
###############################################################################

# Width & Height
varLabelTextW = StringVar()
varLabelTextW.set("width:20")
varLabelTextH = StringVar()
varLabelTextH.set("height:20")

# View UI tool setup width
def wplus():
  initValues.ELEMENT_WIDTH = initValues.ELEMENT_WIDTH + initValues.incDecWidth
  varLabelTextW.set("width:"+ str(initValues.ELEMENT_WIDTH))
  if initValues.autoTile == 1:
    tileXplus()

widthPlus = tkinter.Button(
    window, text="+", command=wplus)
widthPlus.place(x=0, y=20, height=25, width=50, in_=topFrame)

def wminus():
  if initValues.ELEMENT_WIDTH > 20:
    initValues.ELEMENT_WIDTH = initValues.ELEMENT_WIDTH - initValues.incDecWidth
    varLabelTextW.set("Width:" + str(initValues.ELEMENT_WIDTH))
    if initValues.autoTile == 1:
      tileXminus()

widthMinus = tkinter.Button(
    window, text="-", command=wminus)
widthMinus.place(x=50, y=20, height=25, width=50, in_=topFrame)

labelWidth = tkinter.Label(window, textvariable=varLabelTextW)
labelWidth.place(x=0, y=0, width=100, height=20, in_=topFrame)

# for height
labelHeight = tkinter.Label(window, textvariable=varLabelTextH)
labelHeight.place(x=0, y=45, width=100, height=20, in_=topFrame)

def hplus():
  initValues.ELEMENT_HEIGHT = initValues.ELEMENT_HEIGHT + initValues.incDecHeight
  varLabelTextH.set("Height:" + str(initValues.ELEMENT_HEIGHT))
  if initValues.autoTile == 1:
    tileYplus()

heightPlus = tkinter.Button(
    window, text="+", command=hplus)
heightPlus.place(x=0, y=63, height=25, width=50, in_=topFrame)

def hminus():
  if initValues.ELEMENT_HEIGHT > 20:
    initValues.ELEMENT_HEIGHT = initValues.ELEMENT_HEIGHT - initValues.incDecHeight
    varLabelTextH.set("Height:" + str(initValues.ELEMENT_HEIGHT))
    if initValues.autoTile == 1:
      tileYminus()

heightMinus = tkinter.Button(window, text="-", command=hminus)
heightMinus.place(x=50, y=63, height=25, width=50, in_=topFrame)

###############################################################################
# Left box - tiles
###############################################################################

varLabelTextTileX = StringVar()
varLabelTextTileX.set("tileX:" + str(initValues.tilesX))

varLabelTextTileY = StringVar()
varLabelTextTileY.set("tileY:" + str(initValues.tilesY))

# View UI tool for tilesX
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
# Left box - ExportScale
###############################################################################

# for tilesY
varLabelTextexportScale = StringVar()
varLabelTextexportScale.set("exportScale:" + str(initValues.exportScale))

labelExportScale = tkinter.Label(window, textvariable=varLabelTextexportScale)
labelExportScale.place(x=0, y=235, width=100, height=20, in_=topFrame)

def exportScaleplus():
  initValues.exportScale = initValues.exportScale + 1
  varLabelTextexportScale.set("exportScale:" + str(initValues.exportScale))

exportScalePlus = tkinter.Button(window, text="+", command=exportScaleplus)
exportScalePlus.place(x=0, y=255, height=25, width=50, in_=topFrame)

def exportScaleminus():
  if initValues.exportScale > 1:
    initValues.exportScale = initValues.exportScale - 1
    varLabelTextexportScale.set("exportScale:" + str(initValues.exportScale))

exportScaleMinus = tkinter.Button(window, text="-", command=exportScaleminus)
exportScaleMinus.place(x=50, y=255, height=25, width=50, in_=topFrame)

###############################################################################
# Left box - Rotate values
###############################################################################

def rotatedValuesMethod():
  # print("Rotate values.")
  localH = initValues.ELEMENT_HEIGHT
  initValues.ELEMENT_HEIGHT = initValues.ELEMENT_WIDTH
  initValues.ELEMENT_WIDTH = localH
  varLabelTextW.set("Width:" + str(initValues.ELEMENT_WIDTH))
  varLabelTextH.set("Height:" + str(initValues.ELEMENT_HEIGHT))
  localT = initValues.tilesX
  initValues.tilesX = initValues.tilesY
  initValues.tilesY = localT
  varLabelTextTileX.set("tileX:" + str(initValues.tilesX))
  varLabelTextTileY.set("tileY:" + str(initValues.tilesY))

rotatedValuesControl = tkinter.Button(window, text="Rotate values", command=rotatedValuesMethod)
rotatedValuesControl.place(x=0, y=207, height=25, width=100, in_=topFrame)

######################################################
# left box INSERTTYPE
######################################################

varSelLabelTex = StringVar()
varSelLabelTex.set("Selected texture filename")
selectedTexLabel = tkinter.Label(window, textvariable=varSelLabelTex, font=("Helvetica", 10))
# appCoordinate.configure(background="#000000")
selectedTexLabel.place(x=110, y=0, height=20, width=850)

def on_field_change(index, value, op):
  # print("combobox updated to ", varLabelInsertBox.get())
  if varLabelInsertBox.get() == "collectItem":
    # print("Setup input vars fot item strict.")
    resetInputValuesToMin()
    resListbox.delete(0,tkinter.END)
    RESOURCE_INDENTITY.clear()
    # RESOURCE_IMAGES_OBJ.clear()
    #refresrList()
    getImagesFrom(initValues.relativeTexCollectItemsPath)
  elif (varLabelInsertBox.get() == "ground"):
    resListbox.delete(0,tkinter.END)
    RESOURCE_INDENTITY.clear()
    # RESOURCE_IMAGES_OBJ.clear()
    #refresrList()
    getImagesFrom(initValues.relativeTexGroundsPath)


varLabelInsertBox = StringVar()
varLabelInsertBox.set(" ")
varLabelInsertBox.trace('w',on_field_change)
insertBox = ttk.Combobox(window,
                         font="none 12 bold",
                         width=100,
                         textvariable=varLabelInsertBox,
                         values=["ground", "collectItem"])

# insertBox['values'] = [x for x in ["ground", "collectItem"]]
insertBox.current(0)
insertBox.place(x=0, y=290, height=25, width=100, in_=topFrame)
# print(insertBox.get())

#######################################################################
# autoTiles CheckBox
#######################################################################

varAutoTile = tkinter.IntVar(value=1)
def autoTileChanged():
  # print(" >>>>>>>>>>>>" + str( varAutoTile.get() ) )
  initValues.autoTile = varAutoTile.get()

autoTiles = tkinter.Checkbutton(window, text="Autotiles", variable=varAutoTile, command=autoTileChanged)
autoTiles.place(x=0, y=180, height=25, width=100, in_=topFrame)

######################################################
# left box subPuth - Show all
######################################################

varAutoSubPath = tkinter.IntVar(value=1)
def autoSubPathChanged():
  # print(" Show all images " + str( varAutoSubPath.get() ) )
  initValues.includeAllImages = varAutoSubPath.get()
  resListbox.delete(0,tkinter.END)
  RESOURCE_INDENTITY.clear()
  refresrList()

autoSubPath = tkinter.Checkbutton(window, text="Show all", variable=varAutoSubPath, command=autoSubPathChanged)
autoSubPath.place(x=0, y=310, height=25, width=100, in_=topFrame)

#######################################################################
# Resource - image list
# Path is relatiove but autoconfigured from absolute map path.
# Keep visual-ts-game-engine project folder structure.
#######################################################################

# make it global , DEFAULT VALUES
localImgItems = Image.open(initValues.absolutePacksPath +
  initValues.relativeTexturesPath +
  initValues.relativeTexGroundsPath + 'choco.png').resize((initValues.ELEMENT_WIDTH, initValues.ELEMENT_HEIGHT), Image.ANTIALIAS)

defaultTextureItems = ImageTk.PhotoImage(localImgItems)
previewImg = tkinter.Label(resourcePreview, image=defaultTextureItems)
previewImg.image = defaultTextureItems

# GLOBAL
selectedTex = "" # initValues.absolutePacksPath + initValues.relativeTexturesPath + initValues.relativeTexGroundsPath + 'choco.png'

def setCurTexture():
  index = 0
  value = resListbox.get(index)
  global varSelLabelTex
  varSelLabelTex.set(value)
  # print("DEFAULT DATA: ", RESOURCE_INDENTITY[index])
  localImgItems = Image.open(value).resize((100,100), Image.ANTIALIAS)
  defaultTextureItems = ImageTk.PhotoImage(localImgItems)
  global selectedTex
  selectedTex = value
  previewImg = tkinter.Label(resourcePreview, image=defaultTextureItems)
  # config
  previewImg.image = defaultTextureItems
  previewImg.place(x=0, y=0)


def selectedImageChanged(what):
  localw = what.widget
  index = int(localw.curselection()[0])
  value = localw.get(index)
  global varSelLabelTex
  varSelLabelTex.set(value)
  # selection=widget.curselection()
  #value = widget.get(selection[0])
  # print("GET V: ", RESOURCE_INDENTITY.index(value))
  # print("GET DATA : ", RESOURCE_INDENTITY[index])
  localImgItems = Image.open(value).resize((100,100), Image.ANTIALIAS)
  defaultTextureItems = ImageTk.PhotoImage(localImgItems)
  global selectedTex
  selectedTex = value
  previewImg = tkinter.Label(resourcePreview, image=defaultTextureItems)
  previewImg.image = defaultTextureItems
  previewImg.place(x=0, y=0)

def hideResPreview():
  resourcePreview.place_forget()

# resourcePreview.place_forget()

labelRes = tkinter.Label(topFrame, text="Textures list:")
labelRes.place(x=0, y=340, height=25, width=100, in_=topFrame)

resListbox = tkinter.Listbox(window)
resListbox.place(x=0, y=345, height=150, width=100, in_=topFrame)
resListbox.bind('<<ListboxSelect>>', selectedImageChanged)

scrollbar = tkinter.Scrollbar(resListbox, orient="vertical")
scrollbar.config(command=resListbox.yview)
# scrollbar.place(in_=resListbox, x=80)
scrollbar.pack(side=tkinter.RIGHT, fill = tkinter.Y)

resListbox.config(yscrollcommand=scrollbar.set)

# src\examples\platformer\imgs\collect-items

# Res path
def getImagesFromImgsRoot():
  resourceTexPath = initValues.absolutePacksPath + initValues.relativeTexturesPath
  for entry in os.scandir(resourceTexPath):
    localC = 1
    if entry.is_file():
      localFullPath = resourceTexPath + entry.name
      RESOURCE_INDENTITY.insert(len(RESOURCE_INDENTITY) + 1, localFullPath)
      resListbox.insert(len(RESOURCE_INDENTITY), entry.name)
      localC = localC + 1
      # print(entry.name)



def getImagesFrom(subPath):
  resourceTexPath = initValues.absolutePacksPath + initValues.relativeTexturesPath + subPath
  for entry in os.scandir(resourceTexPath):
    if entry.is_file():
      # collect all imgs data
      localFullPath = resourceTexPath + entry.name
      RESOURCE_INDENTITY.insert(len(RESOURCE_INDENTITY), localFullPath)
      resListbox.insert(len(RESOURCE_INDENTITY), localFullPath)
      localImgItems = Image.open(localFullPath).resize((initValues.ELEMENT_WIDTH, initValues.ELEMENT_HEIGHT), Image.ANTIALIAS)
      cTextureItems = ImageTk.PhotoImage(localImgItems)
      RESOURCE_IMAGES_OBJ.insert(len(RESOURCE_INDENTITY), cTextureItems)
      global PREVENT_ADDING
      if PREVENT_ADDING == 0:
        RESOURCE_INDENTITY_READONLY.insert(len(RESOURCE_INDENTITY), localFullPath)
        # print("Res READ ONLY.") need to check for improve
  # print("Res list refreshed make first item selected...")
  setCurTexture()


def refresrList():
  if initValues.includeAllImages == 1:
    getImagesFrom(initValues.relativeTexGroundsPath)
    getImagesFrom(initValues.relativeTexCollectItemsPath)

  else:
    print(insertBox.get())
    if insertBox.get() == "ground":
      getImagesFrom(initValues.relativeTexGroundsPath)
    elif insertBox.get() == "collectItem":
      getImagesFrom(initValues.relativeTexCollectItemsPath)
  global selectedTex
  selectedTex = RESOURCE_INDENTITY[0]

refresrList()

#    im = Image.open(jpeg)
#    im.thumbnail((96, 170), Image.ANTIALIAS)
#    photo = ImageTk.PhotoImage(im)
#    label = tk.Label(root, image=photo)

#######################################################################
# Reset to minimum Minimum predefinited value (harccode) is 20 for
# w and h and 1 for tiles.
#######################################################################

def resetInputValuesToMin():
  initValues.ELEMENT_WIDTH = 20
  varLabelTextW.set("Width:" + str(20))
  initValues.ELEMENT_HEIGHT = 20
  varLabelTextH.set("Height:" + str(20))
  initValues.tilesX = 1
  varLabelTextTileX.set("tileX:" + str(1))
  initValues.tilesY = 1
  varLabelTextTileY.set("tileY:" + str(1))


#######################################################################
# Add new element method
#######################################################################

def addNewElements(loadedMap):
  for element in loadedMap:
    localModel = StaticGrounds(element['x'],
                               element['y'],
                               element['w'],
                               element['h'],
                               element['tex'],
                               element['tiles']['tilesX'],
                               element['tiles']['tilesY'])
    print(element['pythonImgPath'])
    MyDefaultMap.add(localModel, element['pythonImgPath'])
  drawMap()

# Collect mouse & other data [x,y,w,h,tex]
def collectMouseEventData(event):
  if event.y > 0 and event.x > 50:
    # print("clicked at", event.x, event.y)
    x = event.x
    y = event.y
    local = "x:" + str(event.x) + ", y:" + str(event.y)
    appCoordinate.configure(text=local)

    if initValues.stickler["enabledX"] == True:
      x = editorStickler.recalculateX(x)
      # print("Enabled X stickler.")

    if initValues.stickler["enabledY"] == True:
      y = editorStickler.recalculateY(y)
      # print(" Y ")

    localModel = 0
    #RESOURCE_INDENTITY
    filename = selectedTex.split('\\')
    filenameStr = "require('../../imgs/" + filename[len(filename) -2] + "/" +  filename[len(filename) -1] + "')"
    if insertBox.get() == "ground":
      localModel = StaticGrounds(x,
                                y,
                                initValues.ELEMENT_WIDTH,
                                initValues.ELEMENT_HEIGHT,
                                filenameStr,
                                initValues.tilesX,
                                initValues.tilesY)
    elif insertBox.get() == "collectItem":
      # Hardcoded for now: collectItemPoint
      localModel = CollectingItems(
                                x,
                                y,
                                initValues.ELEMENT_WIDTH,
                                initValues.ELEMENT_HEIGHT,
                                filenameStr,
                                initValues.tilesX,
                                initValues.tilesY,
                                "collectItemPoint",
                                10)
    MyDefaultMap.add(localModel, selectedTex)
    drawMap()

# window.bind("<Button-1>", collectMouseEventData)

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
  # print("undo")

def menuEventClearMap():
  if messagebox.askokcancel("Clear map", "Do you really wish to clear map?"):
    MyDefaultMap.clear()
    canvas.delete("all")
    drawMap()
    print("Clear map")

def menuEventClearMapForce():
  MyDefaultMap.clear()
  canvas.delete("all")
  drawMap()
  print("Clear map")

def menuEventSaveMap():
  # print(MyDefaultMap.map)
  MyDefaultMap.prepareForSave()
  json_string = json.dumps(MyDefaultMap.exportMap)
  # print(os.getcwd(), os.path.abspath(__file__))
  with open("map2d.creator", "w", newline='\r\n') as write_file:
    json.dump(json.loads(json_string), write_file , indent=2)
    print("Map saved.")

def menuEventSaveAsMap():
  MyDefaultMap.prepareForSave()
  json_string = json.dumps(MyDefaultMap.exportMap)
  f = filedialog.asksaveasfile(
    mode='w',
    initialdir = "saved-maps/",
    defaultextension=".creator",
    title="Save as your map")
  if f is None:
    return
  f.write(json_string)
  f.close()

def menuEventExportMap():
  print(MyDefaultMap.map)
  MyDefaultMap.prepareForExport()
  json_string = json.dumps(MyDefaultMap.exportMap2)
  print(os.getcwd(), os.path.abspath(__file__))
  exportPathName = "map2d.ts"
  # absolutePacksPath
  if initValues.absolutePacksPathEnabled == True:
    exportPathName = initValues.absolutePacksPath + initValues.relativeMapPath + exportPathName
    print("Save export intro absolute path.")
  with open(str(exportPathName), "w", newline='\r\n', ) as write_file:
    json_string = json_string.replace("[", "let generatedMap = [")
    json_string = json_string.replace("]", "]; export default generatedMap;")
    json_string = json_string.replace('"require', 'require')
    json_string = json_string.replace(')"', ')')

    if initValues.exportInOneLine == False:
      json_string = json_string.replace("," , ", \n ")
    write_file.write(json_string)
    print("Map saved.")

def menuEventLoadMap():
  with open('map2d.creator', 'r') as loadedMap:
    rawString = loadedMap.read()
    rawString = rawString.replace('[', '{ "root" : [')
    rawString = rawString.replace("]", "]}")
    json_data = json.loads(rawString)
    json_data = json_data['root']
    addNewElements(json_data)

def menuEventLoadCustomMap():
  filename = filedialog.askopenfilename(
    initialdir="saved-maps/",
    title="Select map",
    filetypes=[("Visual ts game engine tool Creator-2dMap Filetype ", "creator")])
  # print(filename)
  with open(filename, 'r') as loadedMap:
    rawString = loadedMap.read()
    rawString = rawString.replace('[', '{ "root" : [')
    rawString = rawString.replace("]", "]}")
    json_data = json.loads(rawString)
    json_data = json_data['root']
    addNewElements(json_data)

# About
def showAbout():
  messagebox.showinfo("About", """
    Original source project `creator-2dmap` ver 0.2 \n
    2019/2020 Copyright Nikola Lukic                \n
    created by Nikola Lukic zlatnaspirala@gmail.com \n \n
    LICENCE:                                        \n
    GNU LESSER GENERAL PUBLIC LICENSE Version 3     \n
    https://github.com/zlatnaspirala/creator-2dmap  \n
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
file_menu.add_command(label="Load default map", command=menuEventLoadMap)
file_menu.add_command(label="Save default map", command=menuEventSaveMap)
file_menu.add_separator()
file_menu.add_command(label="Load custom map", command=menuEventLoadCustomMap)
file_menu.add_command(label="Save as", command=menuEventSaveAsMap)
file_menu.add_separator()
file_menu.add_command(label="Export map", command=menuEventExportMap)
file_menu.add_separator()
file_menu.add_command(label="Clear map", command=menuEventClearMap)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=terminate_app)
file_menu.add_separator()
file_menu.add_command(label="Force clear map", command=menuEventClearMapForce)

# sub menu EDIT
edit_menu = tkinter.Menu(root_menu)
root_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Relocate last added item", command=undoRemoveLast)
# edit_menu.add_command(label="Redo last added", command=myEvent) # NOT DONE !
file_menu.add_separator()
edit_menu.add_command(label="Reset input", command=resetInputValuesToMin)
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

################################################################################
# Canvas element
################################################################################

canvas = tkinter.Canvas(
    window,
    width=screen_width - 110,
    height=screen_height - 110,
    background=initValues.windowBackgroundColor
  )
canvas.place(x=100, y=20, width=screen_width - 115, height=screen_height - 130)
print("Screen size: ", screen_width , screen_height, sep="-")

canvas.bind("<Button-1>", collectMouseEventData)

# canvas.delete(line1)
# canvas.delete(tkinter.ALL)

###############################################################################
# Re Draw map element's
###############################################################################

# Symbolic img param
img = Image.open("resource/floor2.png")
defaultTextureGrounds= ImageTk.PhotoImage(img)
imgItems = Image.open("resource/bitcoin.png").resize((20,20), Image.ANTIALIAS)
defaultTextureItems = ImageTk.PhotoImage(imgItems)

imgs = []
defaultTexture_ = []
canvasImgElement = []

def drawMap():
  print("Clear canvas.")
  canvas.delete("all")
  if initValues.canvasGridVisible == True:
    print("Draw Map Grid.")
    for x in range(100, screen_width, initValues.gridWidth):
      line1 = canvas.create_line(0, x, screen_width, x, fill="orange")
      line2 = canvas.create_line(x, 0, x, screen_width, fill="red")

  for (element, texpath) in zip(MyDefaultMap.map, MyDefaultMap.pythonImageObjectMemory):
    #if texpath == "":
    #  print("CATCH")
    #  global defaultTextureItems
    #  dTex = defaultTextureItems
    # else:
    test2 = RESOURCE_INDENTITY_READONLY.index(texpath)
    # test2 = RESOURCE_INDENTITY.index(texpath)
    dTex = RESOURCE_IMAGES_OBJ[test2]
    canvas.create_rectangle(element.x, element.y, element.x2, element.y2, fill="blue")
    # error on 'infly img creation with resize' ?!
    # Fixed with preload buffered all tex images.
    # Best for now
    # print(texpath + "<<<<<")

    if element.tilesX == 0:
      draws = canvas.create_image(element.x, element.y, anchor="nw", image=dTex)
      canvasImgElement.append(draws)
    for i in range(int(element.tilesX)):
      draws = canvas.create_image(element.x + i * 20 , element.y, anchor="nw", image=dTex)
      canvasImgElement.append(draws)
      for y in range(int(element.tilesY)):
        canvasImgElement.append(canvas.create_image(element.x  + i * 20, element.y + y * 20, anchor="nw", image=dTex))
    if hasattr(element, 'colectionLabel'):
      canvasImgElement.append(canvas.create_image(element.x, element.y, anchor="nw", image=dTex))
      # print("Draw collection item.")

###############################################################################
# initial draw
###############################################################################

drawMap()

###############################################################################
# Files operation test
###############################################################################
#command = 'echo "$(pwd)"'
#process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
#output, error = process.communicate()
#print("Output", output)

# Fix layout
resourcePreview.lift()


# Running
window.mainloop()
