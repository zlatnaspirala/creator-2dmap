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
    # print("New element added to the current map also created image: " + self.name)

  def prepareForSave(self):
    for (element,pythonImageObjectMemo) in zip(self.map, self.pythonImageObjectMemory):

      if hasattr(element, 'text'):
        # print("DETECTED TEXT LABEL")
        myObject = {
                  "x": str(element.x),
                  "y": str(element.y),
                  "text": str(element.text),
                  "textColor": str(element.textColor),
                  "textSize": element.textSize,
                  "pythonImgPath": pythonImageObjectMemo
                }
      else:
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
          # print("It is a collection item ...")
        if hasattr(element, 'enemyLabel'):
          myObject["enemyLabel"] = element.enemyLabel
          myObject["enemyOptions"] = element.enemyOptions
          # print("It is a enemy item ...")

      self.exportMap.append(myObject)

  def prepareForExport(self):
    self.exportMap2.clear()
    for element in self.map:

      if hasattr(element, 'text'):
        # print("DETECTED TEXT LABEL")
        myObject = {
                  "x": str(element.x),
                  "y": str(element.y),
                  "text": str(element.text),
                  "textColor": str(element.textColor),
                  "textSize": element.textSize
                }
      else:
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
        if hasattr(element, 'enemyLabel'):
          myObject["enemyLabel"] = element.enemyLabel
          myObject["enemyOptions"] = element.enemyOptions
          print("It is a enemy item ...")
      self.exportMap2.append(myObject)

  def clear(self):
    self.map.clear()
    self.pythonImageObjectMemory.clear()
    self.exportMap.clear()
    self.exportMap2.clear()

  def removeLast(self):
    self.clipboardElementMemo = self.map.pop()
    self.pythonImageObjectMemory.pop()
    if len(self.exportMap) != 0:
      self.exportMap.pop()
    if len(self.exportMap2) != 0:
      self.exportMap2.pop()

