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

###############################################################################
# Define window object, Map instance, general screen w/h
###############################################################################
window = tkinter.Tk()
window.title("GUI tool creator-2dmap for vtge")

defaultTexture = "./imgs/grounds/texx.png"
# virtual path
# defaultTextureTool = ImageTk.PhotoImage(file='resource/texx.png')
# anchor="nw"
# img = Image.open("resource/texx.png")
# img.resize((100,22), Image.ANTIALIAS)
# defaultTextureTool = ImageTk.PhotoImage(img)

# ImageTk.PhotoImage(Image.open("resource/nik.jpg"))
# panel = tkinter.Label(window, image=defaultTexture)
# panel.pack(side="bottom", fill="both", expand="yes")

# Setup dimension for window
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.geometry(str(screen_width) + "x" + str(screen_height))

# Define myMap object and instance initial data object
initValues = InitialData()
MyDefaultMap = myMap("MyDefaultMap", initValues)

topFrame = tkinter.Frame(window,
                         background=initValues.topFrameBackgroundColor,
                         height=screen_height,
                         width=110)
topFrame.pack(side="left", in_=window)

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
  if event.y > 20 and event.x > 100:
    print("clicked at", event.x, event.y)
    local = "x:" + str(event.x) + ", y:" + str(event.y)
    appCoordinate.configure(text=local)
    localModel = StaticGrounds(event.x,
                               event.y,
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
    print("<Clear map>")

data = []

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
  with open("map2d.ppack", "w", newline='\r\n') as write_file:
    json.dump(json.loads(json_string), write_file , indent=2)
    print("Map saved.")

def menuEventLoadMap():
  with open('map2d.creator', 'r') as loadedMap:
    rawString = loadedMap.read()
    rawString = rawString.replace('[', '{ "root" : [')
    rawString = rawString.replace("]", "]}")
    json_data = json.loads(rawString)
    json_data = json_data['root']
    addNewElements(json_data)


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
canvas.place(x=100, y=20, width=screen_width - 120, height=screen_height-130)
print("Screen size: ", screen_width , screen_height, sep="-")
# canvas.delete(line1)
# canvas.delete(tkinter.ALL)

###############################################################################
# Re Draw map element's
###############################################################################
def drawMap():
  print("Draw Map")
  if initValues.canvasGridVisible == True:
    # Grid for canvas
    for x in range(0, screen_width, 100):
      line1 = canvas.create_line(0, x, screen_width, x, fill="orange")
      line2 = canvas.create_line(x, 0, x, screen_width, fill="red")

  for element in MyDefaultMap.map:
    canvas.create_rectangle(element.x, element.y, element.x2, element.y2, fill="blue")
      # ttt = canvas.create_image(element.x, element.y, anchor="nw", image=defaultTextureTool, height = 20, width = 200)
      # canvas.itemconfig(ttt, image=defaultTextureTool) ?

###############################################################################
# Files operation && map model
###############################################################################

#command = 'echo "$(pwd)"'
#process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
#output, error = process.communicate()

#print("Output", output)

# path = '/users/sammy/days.txt'
# days_file = open(path, 'r')
# days = days_file.read()

# new_path = '/users/sammy/new_days.txt'
# new_days = open(new_path, 'w')

# title = 'Days of the Week\n'
# new_days.write(title)
# print(title)

# new_days.write(days)
# print(days)

# days_file.close()
# new_days.close()

window.mainloop()
