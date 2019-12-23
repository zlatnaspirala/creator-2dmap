import PIL
from PIL import ImageTk, Image

class myMap:
  def __init__(self, name, initValues_instance):
    self.initValues = initValues_instance
    self.name = name
    self.map = []
    self.exportMap = []
    self.exportMap2 = []
    self.clipboardElementMemo = 0
    self.pythonImageObjectMemory = []

  def add(self, x, pythonImgAbsPath):
    self.map.append(x)
    self.pythonImageObjectMemory.append(pythonImgAbsPath)
    print("New element added to the current map also created image: " + self.name)

  def prepareForSave(self):
    for (element,pythonImageObjectMemo) in zip(self.map, self.pythonImageObjectMemory):
      myObject = {  "x": str(element.x),
                    "y": str(element.y),
                    "w": str(element.w),
                    "h": str(element.h),
                    "tex": element.texture,
                    "tiles":
                      {
                        "tilesX": str(element.tilesX),
                        "tilesY": str(element.tilesY)
                      },
                    "pythonImgPath": pythonImageObjectMemo
                 }
      if hasattr(element, 'colectionLabel'):
        myObject["colectionLabel"] = element.colectionLabel
        myObject["points"] = element.points
        print("It is a collection item ...")

      self.exportMap.append(myObject)

  def prepareForExport(self):
    self.exportMap2.clear()
    for element in self.map:
      myObject = { "x": element.x * self.initValues.exportScale,
                   "y": element.y * self.initValues.exportScale,
                   "w": element.w * self.initValues.exportScale,
                   "h": element.h * self.initValues.exportScale,
                   "tex": element.texture,
                   "tiles":
                     {
                       "tilesX": element.tilesX,
                       "tilesY": element.tilesY
                     }
                  }
      if hasattr(element, 'colectionLabel'):
        myObject["colectionLabel"] = element.colectionLabel
        myObject["points"] = element.points
        print("It is a collection item ...")
      self.exportMap2.append(myObject)

  def clear(self):
    self.map.clear()
    self.pythonImageObjectMemory.clear()
    self.exportMap.clear()
    self.exportMap2.clear()

  def removeLast(self):
    self.clipboardElementMemo = self.map.pop()
