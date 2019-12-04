
class myMap:
  def __init__(self, name, initValues_instance):
    self.initValues = initValues_instance
    self.name = name
    self.map = []
    self.exportMap = []
    self.exportMap2 = []
    self.clipboardElementMemo = 0

  def add(self, x):
    self.map.append(x)
    print("New element added to the current map: " + self.name)

  def prepareForSave(self):
    for element in self.map:
      myObject = { "x": str(element.x),
                   "y": str(element.y),
                   "w": str(element.w),
                   "h": str(element.h),
                   "tex": element.texture,
                   "tiles":
                     {
                       "tilesX": str(element.tilesX),
                       "tilesY": str(element.tilesY)
                     }
                  }
      self.exportMap.append(myObject)

  def prepareForExport(self):
    for element in self.map:
      myObject = { "x": str(element.x *  self.initValues.exportScale),
                   "y": str(element.y *  self.initValues.exportScale),
                   "w": str(element.w *  self.initValues.exportScale),
                   "h": str(element.h *  self.initValues.exportScale),
                   "tex": element.texture,
                   "tiles":
                     {
                       "tilesX": str(element.tilesX),
                       "tilesY": str(element.tilesY)
                     }
                  }
      self.exportMap2.append(myObject)

  def clear(self):
    self.map.clear()
    self.exportMap.clear()
    self.exportMap2.clear()

  def removeLast(self):
    self.clipboardElementMemo = self.map.pop()
