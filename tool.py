#!/usr/bin/python3

#################################################################################
#  creator2dmap is python3 application for creating visuat-ts game engine 2d maps
#  LICENCE: GNU LESSER GENERAL PUBLIC LICENSE Version 3
#  https://github.com/zlatnaspirala/creator-2dmap
#  Code style ~camel
#  Version: 0.4
#  - Types of game object : [ground, collectItem]
#  - Show/Hide grids
#  - Sticklers enable disable
#  - defaults.py - general config
#  - Save/Load direct (template map) it is : map2d.creator file in the root of
#     project. If you have already manualy added and than load default map it will
#     be append together in current map.
#    Save/Load dialog for custom maps. Default folder `saved-maps/`
#   Clear map - Force clear without warning
#   Reset input - for reset left box input values to the minimum.
#  - Relocate last added game object
#  - Remove last added element
#   Scroll vertical & horizontal canvas, help to create large maps.
#################################################################################

#################################################################################
#  Imports
#################################################################################

import os
from map import myMap
from models.ground import StaticGrounds
from models.collectitems import CollectingItems
from models.enemies import Enemies
from defaults import InitialData
import tkinter
import json
from tkinter import BOTH, StringVar, messagebox, ttk
from functools import partial
import subprocess
import PIL
from PIL import ImageTk, Image
from common.stickler import Stickler
from common.sprites import Sprite
import time
from tkinter import filedialog

###############################################################################
# Define window object, Map instance, general screen w/h
###############################################################################

window = tkinter.Tk()
window.title("GUI tool creator-2dmap for visual-ts game engine FREEWARE")

# Global currentInsertType = "grounds" | "collectItems" | "enemies"
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
varLabelTextW.set("width:25")
varLabelTextH = StringVar()
varLabelTextH.set("height:25")

# View UI tool setup width
def wplus():
  initValues.ELEMENT_WIDTH = initValues.ELEMENT_WIDTH + initValues.incDecWidth
  varLabelTextW.set("width:"+ str(initValues.ELEMENT_WIDTH))
  if initValues.autoTile == 1:
    tileXplus()

widthPlus = tkinter.Button(window, text="+", command=wplus)
widthPlus.place(x=0, y=20, height=25, width=50, in_=topFrame)

def wminus():
  if initValues.ELEMENT_WIDTH > initValues.baseElementValue:
    initValues.ELEMENT_WIDTH = initValues.ELEMENT_WIDTH - initValues.incDecWidth
    varLabelTextW.set("Width:" + str(initValues.ELEMENT_WIDTH))
    if initValues.autoTile == 1:
      tileXminus()

widthMinus = tkinter.Button(window, text="-", command=wminus)
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
  if initValues.ELEMENT_HEIGHT > initValues.baseElementValue:
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
selectedTexLabel.place(x=110, y=0, height=20, width=850)

######################################################
# Resource list - Texture staff
######################################################

def selectedImageChanged(what):
  localw = what.widget
  index = int(localw.curselection()[0])
  value = localw.get(index)
  global varSelLabelTex
  varSelLabelTex.set(value)
  localImgItems = Image.open(value).resize((100,100), Image.ANTIALIAS)
  defaultTextureItems = ImageTk.PhotoImage(localImgItems)
  global selectedTex
  selectedTex = value
  previewImg = tkinter.Label(resourcePreview, image=defaultTextureItems)
  previewImg.image = defaultTextureItems
  previewImg.place(x=0, y=0)

labelRes = tkinter.Label(topFrame, text="Textures list:")
labelRes.place(x=0, y=340, height=25, width=100, in_=topFrame)

resListbox = tkinter.Listbox(window)
resListbox.place(x=0, y=345, height=150, width=100, in_=topFrame)
resListbox.bind('<<ListboxSelect>>', selectedImageChanged)

scrollbar = tkinter.Scrollbar(resListbox, orient="vertical")
scrollbar.config(command=resListbox.yview)
scrollbar.pack(side=tkinter.RIGHT, fill = tkinter.Y)

resListbox.config(yscrollcommand=scrollbar.set)

def setCurTexture():
  index = 0
  value = resListbox.get(index)
  global varSelLabelTex
  varSelLabelTex.set(value)
  localImgItems = Image.open(value).resize((100,100), Image.ANTIALIAS)
  defaultTextureItems = ImageTk.PhotoImage(localImgItems)
  global selectedTex
  selectedTex = value
  previewImg = tkinter.Label(resourcePreview, image=defaultTextureItems)
  previewImg.image = defaultTextureItems
  previewImg.place(x=0, y=0)

def getImagesFrom(subPath):
  resourceTexPath = initValues.absolutePacksPath + initValues.relativeTexturesPath + subPath
  for entry in os.scandir(resourceTexPath):
    if entry.is_file():
      # collect all imgs data

      localFullPath = resourceTexPath + entry.name
      RESOURCE_INDENTITY.insert(len(RESOURCE_INDENTITY), localFullPath)
      resListbox.insert(len(RESOURCE_INDENTITY), localFullPath)

      localImgItems = Image.open(localFullPath).resize(
      (initValues.baseElementValue,
      initValues.baseElementValue), Image.ANTIALIAS)
      cTextureItems = ImageTk.PhotoImage(localImgItems)

      # Origin value is enemies\  \\ is escape...
      if subPath == "enemies\\":
        test = Sprite(localFullPath)
        cTextureItems = test.images[0]
        print("sprites test")

      # cTextureItems = ImageTk.PhotoImage(localImgItems)
      RESOURCE_IMAGES_OBJ.insert(len(RESOURCE_INDENTITY), cTextureItems)
      global PREVENT_ADDING
      if PREVENT_ADDING == 0:
        RESOURCE_INDENTITY_READONLY.insert(len(RESOURCE_INDENTITY), localFullPath)
        # print("Res READ ONLY.") need to check for improve
  # print("Res list refreshed make first item selected...")
  setCurTexture()

def on_field_change(index, value, op):
  global PREVENT_ADDING
  # print("combobox updated to ", varLabelInsertBox.get())
  if varLabelInsertBox.get() == "collectItem":
    # print("Setup input vars fot item strict.")
    resetInputValuesToMin()
    resListbox.delete(0,tkinter.END)
    RESOURCE_INDENTITY.clear()
    # RESOURCE_IMAGES_OBJ.clear()
    # refresrList()
    getImagesFrom(initValues.relativeTexCollectItemsPath)
  elif (varLabelInsertBox.get() == "ground"):
    resListbox.delete(0,tkinter.END)
    RESOURCE_INDENTITY.clear()
    # RESOURCE_IMAGES_OBJ.clear()
    # refresrList()
    getImagesFrom(initValues.relativeTexGroundsPath)
  elif (varLabelInsertBox.get() == "enemies"):
    resListbox.delete(0,tkinter.END)
    RESOURCE_INDENTITY.clear()
    # RESOURCE_IMAGES_OBJ.clear()
    # refresrList()
    getImagesFrom(initValues.relativeTexEnemiesPath)


varLabelInsertBox = StringVar()
varLabelInsertBox.set(" ")
varLabelInsertBox.trace('w',on_field_change)
insertBox = ttk.Combobox(window,
                         font="none 12 bold",
                         width=100,
                         textvariable=varLabelInsertBox,
                         values=["ground",
                                 "collectItem",
                                 "enemies"])

insertBox.current(0)
insertBox.place(x=0, y=290, height=25, width=100, in_=topFrame)

#######################################################################
# autoTiles CheckBox
#######################################################################

varAutoTile = tkinter.IntVar(value=1)
def autoTileChanged():
  initValues.autoTile = varAutoTile.get()

autoTiles = tkinter.Checkbutton(window, text="Autotiles", variable=varAutoTile, command=autoTileChanged)
autoTiles.place(x=0, y=180, height=25, width=100, in_=topFrame)

######################################################
# left box subPuth - Show all
######################################################

varAutoSubPath = tkinter.IntVar(value=0)
def autoSubPathChanged():
  print(" Show all images " + str( varAutoSubPath.get() ) )
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
selectedTex = ""

def hideResPreview():
  resourcePreview.place_forget()

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

def refresrList():
  if initValues.includeAllImages == 1:
    getImagesFrom(initValues.relativeTexGroundsPath)
    getImagesFrom(initValues.relativeTexCollectItemsPath)
    getImagesFrom(initValues.relativeTexEnemiesPath)
    #PREVENT_ADDING = 1
    initValues.includeAllImages = 0
  else:
    # print(insertBox.get())
    if insertBox.get() == "ground":
      getImagesFrom(initValues.relativeTexGroundsPath)
    elif insertBox.get() == "collectItem":
      getImagesFrom(initValues.relativeTexCollectItemsPath)
    elif insertBox.get() == "enemies":
      getImagesFrom(initValues.relativeTexEnemiesPath)
  global selectedTex
  selectedTex = RESOURCE_INDENTITY[0]

refresrList()

#    im = Image.open(jpeg)
#    im.thumbnail((96, 170), Image.ANTIALIAS)
#    photo = ImageTk.PhotoImage(im)
#    label = tk.Label(root, image=photo)

#######################################################################
# Reset to minimum input values
#######################################################################

def resetInputValuesToMin():
  initValues.ELEMENT_WIDTH = initValues.baseElementValue
  varLabelTextW.set("Width:" + str(initValues.baseElementValue))
  initValues.ELEMENT_HEIGHT = initValues.baseElementValue
  varLabelTextH.set("Height:" + str(initValues.baseElementValue))
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

###########################################################################
# Collect mouse & other data [x,y,w,h,tex]
###########################################################################

def collectMouseEventData(event):

  localcanvas = event.widget

  if event.y > 0 and event.x > 50:
    # print("clicked at", event.x, event.y)
    x = canvas.canvasx(event.x)
    y = canvas.canvasy(event.y)
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
    # Enemies
    elif insertBox.get() == "enemies":
      # Hardcoded for now: increment Dimension
      localName =  filename[len(filename) -1]
      localName = localName.replace(".png", "");
      localModel = Enemies(
                            x,
                            y,
                            initValues.ELEMENT_WIDTH * 1.5,
                            initValues.ELEMENT_HEIGHT * 1.5,
                            filenameStr,
                            initValues.tilesX,
                            initValues.tilesY,
                            localName,
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

def relocateLast():
  MyDefaultMap.removeLast()
  time.sleep(0.1)
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
  # print(MyDefaultMap.map)
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
    Original source project `creator-2dmap` ver 0.4 \n
    2019/2020 Copyright Nikola Lukic                \n
    created by Nikola Lukic zlatnaspirala@gmail.com \n \n
    LICENCE:                                        \n
    GNU LESSER GENERAL PUBLIC LICENSE Version 3     \n
    https://github.com/zlatnaspirala/creator-2dmap  \n
    maximumroulette.com 2020 \n
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
edit_menu.add_command(label="Relocate last added item", command=relocateLast)
edit_menu.add_command(label="Remove last", command=undoRemoveLast)
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
appCoordinate.place(x=screen_width-150, y=0, height=30, width=150)

################################################################################
# canvasFrame - Canvas container
# Canvas element - Visual draw
# Scrollbars V H for canvas
################################################################################
canvasFrame = tkinter.Frame(window,
                            width=screen_width - 110,
                            height=screen_height - 110,
                            background="#f3ffff")
canvasFrame.place(x=105, y=20, width=screen_width - 115, height=screen_height - 130)

canvas = tkinter.Canvas(
    canvasFrame,
    width=screen_width * initValues.canvasScreenCoeficientW,
    height=screen_height * initValues.canvasScreenCoeficientH,
    background=initValues.windowBackgroundColor,
    scrollregion=(0,0,
                  screen_width * initValues.canvasScreenCoeficientW,
                  screen_height * initValues.canvasScreenCoeficientH)
  )
# canvas.place(x=0, y=0, width= 2 *screen_width - 120, height=screen_height - 130)

canvas.configure(scrollregion=canvas.bbox("all"))

canvas.bind("<Button-1>", collectMouseEventData)

def testHorScrollEvent(*args):
  print("GOOOOOOD")

# Scroll bars for canvas
hCanvasBar = tkinter.Scrollbar(canvasFrame,orient=tkinter.HORIZONTAL, command=testHorScrollEvent)
hCanvasBar.pack(side=tkinter.BOTTOM,fill=tkinter.X)
hCanvasBar.config(command=canvas.xview)
vCanvasBar = tkinter.Scrollbar(canvasFrame,orient=tkinter.VERTICAL)
vCanvasBar.pack(side=tkinter.RIGHT,fill=tkinter.Y)
vCanvasBar.config(command=canvas.yview)

canvas.config(xscrollcommand=hCanvasBar.set, yscrollcommand=vCanvasBar.set)

canvas.pack(side=tkinter.LEFT,expand=True,fill=tkinter.BOTH)
# canvas.place(x=0, y=0, width= initValues.canvasScreenCoeficientW * screen_width - 120, height=screen_height - 130)

# canvas.delete(line1)
# canvas.delete(tkinter.ALL)


# Scroll fix

def ScrolledCanvas(master, _mode='xy', **options):
    return Scrolled(Canvas, master, _mode, **options)


###############################################################################
# Re Draw map element's
###############################################################################

# Symbolic img param
# img = Image.open("resource/floor2.png")
# defaultTextureGrounds= ImageTk.PhotoImage(img)
# imgItems = Image.open("resource/bitcoin.png").resize((20,20), Image.ANTIALIAS)
# defaultTextureItems = ImageTk.PhotoImage(imgItems)

imgs = []
defaultTexture_ = []
canvasImgElement = []

def drawMap():
  canvas.delete("all")
  if initValues.canvasGridVisible == True:
    print("Draw Map Grid.")
    for x in range(100, screen_width * initValues.canvasScreenCoeficientW, initValues.gridWidth):
      line1 = canvas.create_line(0, x, screen_width* initValues.canvasScreenCoeficientW, x, fill="orange")
      line2 = canvas.create_line(x, 0, x, screen_width* initValues.canvasScreenCoeficientW, fill="red")

  for (element, texpath) in zip(MyDefaultMap.map, MyDefaultMap.pythonImageObjectMemory):

    test2 = RESOURCE_INDENTITY_READONLY.index(texpath)
    dTex = RESOURCE_IMAGES_OBJ[test2]

    if "enemies" in texpath:
      canvas.create_rectangle(element.x, element.y, element.x2, element.y2, fill="red")
    else:
      pass
      # canvas.create_rectangle(element.x, element.y, element.x2, element.y2, fill="blue")

    # TEST

    if element.tilesX == 0:
      draws = canvas.create_image(element.x, element.y, anchor="nw", image=dTex)
      canvasImgElement.append(draws)

    for i in range(int(element.tilesX)):

      correctDelta = int(element.tilesX)
      X = element.x + i * initValues.baseElementValue
      X = X - correctDelta * initValues.baseElementValue / 2
      draws = canvas.create_image(
        X,
        element.y,
        anchor="nw",
        image=dTex)
      canvasImgElement.append(draws)
      for y in range(int(element.tilesY)):

        correctDelta = int(element.tilesY - 1)
        Y = element.y + y * initValues.baseElementValue
        Y = Y - correctDelta * initValues.baseElementValue / 2

        canvasImgElement.append(canvas.create_image(
          X,
          Y,
          anchor="nw",
          image=dTex)
        )
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

# fix show all to nor show all
varAutoSubPath.set(value=0)
initValues.includeAllImages = varAutoSubPath.get()
resListbox.delete(0,tkinter.END)
RESOURCE_INDENTITY.clear()
refresrList()

# Running
window.mainloop()
