#!/usr/bin/python3

import os
from map import myMap
from models.ground import StaticGrounds
from defaults import InitialData
import tkinter
import json
from tkinter import messagebox, BOTH
from functools import partial
import subprocess
import json

###############################################################################
# Define window object
###############################################################################
window = tkinter.Tk()
window.title("GUI tools Nikola Lukic")

f1 = tkinter.Frame(window, background="blue")
f2 = tkinter.Frame(window, background="pink")
# f1.pack(side="left", fill="both", expand=True)
# f2.pack(side="right", fill="both", expand=True)

# Define myMap object
initValues = InitialData()
MyDefaultMap = myMap("MyDefaultMap")

print("Default values:", initValues.ELEMENT_WIDTH)

# View UI tool
widthPlus = tkinter.Button(window, text="+", fg="red", bg="black")
widthPlus.place(x=480, y=1, height=25, width=25, in_=window)

widthMinus = tkinter.Button(window, text="-", fg="red", bg="black")
widthMinus.place(x=460, y=1, height=25, width=25, in_=window)
#startButton.bind("<Button 1>", partial(getOrigin))

labelWidth = tkinter.Label(window, text="W:100")
labelWidth.place(x=500, y=0, width=99, height=20, in_=window)
# labelWidth.pack()

labelHeight = tkinter.Label(window, text="H:50")
labelHeight.place(x=600, y=0, width=99, height=20, in_=window)
# labelHeight.pack()

########################################
# button = tkinter.Button(window, text="click me!")
# button.place(x=500, y=0, in_=window)
########################################

# Collect mouse data [x,y]
def collectMouseEventData(event):
    print("clicked at", event.x, event.y)
    local = "x:" + str(event.x) + ", y:" + str(event.y)
    appCoordinate.configure(text=local)
    localModel = StaticGrounds(event.x, event.y, initValues.ELEMENT_WIDTH, initValues.ELEMENT_HEIGHT)
    MyDefaultMap.add(localModel)
    drawMap()

window.bind("<Button-1>", collectMouseEventData)

# Setup dimension for window
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.geometry(str(screen_width) + "x" + str(screen_height))

###############################################################################
# Menu Events
###############################################################################
root_menu = tkinter.Menu(window)
window.config(menu=root_menu)

def myEvent():
  print("Menu tab pressed...")

def menuEventClearMap():
  if messagebox.askokcancel("Clear map", "Do you really wish to clear map?"):
    MyDefaultMap.clear()
    canvas.delete("all")
    drawMap()
    print("<Clear map>")

# Quic terminate event
def terminate_app():
  if messagebox.askokcancel("Quit", "Do you really wish to quit?"):
    window.destroy()

# creating sub menus in the root menu
# it intializes a new su menu in the root menu
file_menu = tkinter.Menu(root_menu)
# it creates the name of the sub menu
root_menu.add_cascade(label="File", menu=file_menu)
# it adds a option to the sub menu 'command' parameter is used to do some action
file_menu.add_command(label="Clear map", command=menuEventClearMap)
file_menu.add_command(label="Open files", command=myEvent)
file_menu.add_separator()  # it adds a line after the 'Open files' option
file_menu.add_command(label="Exit", command=terminate_app)

# creting another sub menu
edit_menu = tkinter.Menu(root_menu)
root_menu.add_cascade(label="Edit", menu=myEvent)
edit_menu.add_command(label="Undo", command=myEvent)
edit_menu.add_command(label="Redo", command=myEvent)

# GUI Labels
appCoordinate = tkinter.Label(window, text="Coordinator")
appCoordinate.place(x=screen_width-150, y=0, height=30, width=150)
appCoordinate.pack()

# Canvas
# canvas = tkinter.Canvas(window, width=screen_width/2, height=screen_height/2)
canvas = tkinter.Canvas(window, width=screen_width, height=screen_height)
canvas.pack()
# canvas.create_rectangle(300, 300, 20, 20, fill="blue")
print("Screen size: ", screen_width , screen_height, sep="---")

# Parameters:- (starting x-point, starting y-point, ending x-point, ending y-point)
for x in range(0, screen_width, 100):
  line1 = canvas.create_line(0, x, screen_width, x, fill="blue")
  line2 = canvas.create_line(x, 0, x, screen_width, fill="red")

# starting x-point, starting y-point, width, height, fill
# starting point the coordinates of top-left point of rectangle
# rect = canvas.create_rectangle(0, 0, 1000, 1000, stroke="black")

# you 'delete' shapes using delete method passing the name of the variable as parameter.
# canvas.delete(line1)

# you 'delete' all
# canvas.delete(tkinter.ALL)

###############################################################################
# Re Draw map element's
###############################################################################
def drawMap():
  print("Draw Map")
  for element in MyDefaultMap.map:
    canvas.create_rectangle(element.x, element.y,
                            element.x2, element.y2, fill="blue")


###############################################################################
# Files operation
###############################################################################

data = {
    "president": {
        "name": "Nikola",
        "species": "test"
    }
}

def print_my_path():
    print(data['president'])
    #print('__file__:{}'.format(__file__))
    #print('abspath: {}'.format(os.path.abspath(__file__)))
    print(os.getcwd())

print_my_path()

with open("data_file.json", "w") as write_file:
    json.dump(data, write_file)

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

# quitButton = tkinter.Button(window,
#                   text="QUIT",
#                   fg="red",
#                   command=terminate_app)
# quitButton.pack()
# quitButton.place(x=50, y=0, height=30, width=200)

window.mainloop()
