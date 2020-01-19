import tkinter
from tkinter import simpledialog
from tkinter import Entry

#########################################################
# Dialog for Labels text component
#########################################################

class DialogLabelsBox(simpledialog.Dialog):

  def body(self, master):

    tkinter.Label(master, text="Text : ").grid(row=0)
    tkinter.Label(master, text="Text color : ").grid(row=1)
    tkinter.Label(master, text="Text size : ").grid(row=2)

    self.e1 = Entry(master, text="1")
    self.e2 = Entry(master, text="2")
    self.e3 = Entry(master, text="n")

    self.e1.grid(row=0, column=1)
    self.e2.grid(row=1, column=1)
    self.e3.grid(row=2, column=1)
    return self.e1 # initial focus

  def apply(self):
    arg1 = self.e1.get()
    arg2 = self.e2.get()
    arg3 = self.e3.get()
    self.result = arg1, arg2, arg3
    print (arg1, arg2, arg3)

  def myGet():
    result = {
      "text": str(self.e1.get()),
      "textColor": str(self.e2.get()),
      "textSize": str(self.e2.get()),
    }
    return result

#########################################################
# Dialog for nextLevel itel colletions
#########################################################

class DialogNextLevelBox(simpledialog.Dialog):

  def body(self, master):

    tkinter.Label(master, text="Level name : ").grid(row=0)
    self.e1 = Entry(master, text="1")
    self.e1.grid(row=0, column=1)
    return self.e1

  def apply(self):
    arg1 = self.e1.get()
    self.result = arg1
    print (arg1)

#########################################################
# Dialog for export as
#########################################################

class DialogExportAsBox(simpledialog.Dialog):

  def body(self, master):

    tkinter.Label(master, text="Export level name : ").grid(row=0)
    self.e1 = Entry(master, text="1")
    self.e1.grid(row=0, column=1)
    return self.e1

  def apply(self):
    arg1 = self.e1.get()
    self.result = arg1
    print (arg1)
