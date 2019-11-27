#!/usr/bin/python3
import tkinter
import json
from tkinter import messagebox
from functools import partial

###############################################################################
# Define window object
###############################################################################
window = tkinter.Tk()
window.title("GUI tools Nikola Lukic")

# Collect mouse data [x,y]
def collectMouseEventData(event):
    print("clicked at", event.x, event.y)

# Quic terminate event
def terminate_app():
    if messagebox.askokcancel("Quit", "Do you really wish to quit?"):
        window.destroy()

window.bind("<Button-1>", collectMouseEventData)

# Setup dimension for window
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.geometry(str(screen_width) + "x" + str(screen_height))

# GUI Labels
appCoordinate = tkinter.Label(window, text="x y")
appCoordinate.place(x=screen_width-200, y=0, height=30, width=150)
appCoordinate.pack()

# Canvas
# canvas = tkinter.Canvas(window, width=screen_width/2, height=screen_height/2)
canvas = tkinter.Canvas(window, width=screen_width, height=screen_height)
canvas.pack()
print("Screen size: ", screen_width , screen_height, sep="---")

# Parameters:- (starting x-point, starting y-point, ending x-point, ending y-point)
for x in range(0, screen_width, 10):
  line1 = canvas.create_line(0, x, screen_width, x, fill="blue")
  line2 = canvas.create_line(x, 0, x, screen_width, fill="red")

# starting x-point, starting y-point, width, height, fill
# starting point the coordinates of top-left point of rectangle
# rect = canvas.create_rectangle(0, 0, 1000, 1000, stroke="black")

# you 'delete' shapes using delete method passing the name of the variable as parameter.
# canvas.delete(line1)

# you 'delete' all
# canvas.delete(tkinter.ALL)


def getOrigin(event):
    global x0, y0
    x0 = event.x
    y0 = event.y
    print("getOrigin: ", x0, y0)
    # startButton.bind("<Button 1>", getextentx)

startButton = tkinter.Button(window,
                            text="START",
                            fg="red",
                            bg="black")
startButton.pack()
startButton.place(x=50, y=50, height=30, width=200)
startButton.bind("<Button 1>", partial(getOrigin))

window.bind("<Button 2>", getOrigin)

quitButton = tkinter.Button(window,
                   text="QUIT",
                   fg="red",
                   command=terminate_app)
quitButton.pack()
quitButton.place(x=50, y=0, height=30, width=200)

window.mainloop()
