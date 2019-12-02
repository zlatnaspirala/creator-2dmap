
class myMap:
  def __init__(self, name):
    self.name = name
    self.map = []
    self.exportMap = []
    self.clipboardElementMemo = 0

  def add(self, x):
    self.map.append(x)
    print("New element", x)
    print("New element added to the current map: " + self.name)

  def prepareForExport(self):
    for element in self.map:
      myObject = { "x": element.x, "y": element.y, "w": element.w, "h": element.h, "tex": element.texture, "tiles": { "tilesX": element.tilesX, "tilesY": element.tilesY } }
      self.exportMap.append(myObject)

  def clear(self):
    self.map.clear()
    self.exportMap.clear()

  def removeLast(self):
    self.clipboardElementMemo = self.map.pop()
