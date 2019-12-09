
class InitialData:
  def __init__(self):
    self.exportInOneLine = False # next feature
    self.stickler = {}
    self.stickler["enabledX"] = True
    self.stickler["enabledY"] = True
    self.stickler["mod"] = 30
    self.gridWidth = 50
    self.exportScale = 5
    self.ELEMENT_WIDTH=20
    self.ELEMENT_HEIGHT=20
    self.incDecWidth = 10
    self.incDecHeight = 10
    self.windowBackgroundColor = "#000000"
    self.topFrameBackgroundColor = "#010233"
    self.canvasGridVisible = True
    self.tilesX = 5
    self.tilesY = 1
  def redefine():
    print("Redefine init values...")
  def setSticklerEnabledX(self):
    self.stickler["enabledX"] = not self.stickler["enabledX"]
    print("stickler[enabledX]: ", self.stickler["enabledX"])
  def setSticklerEnabledY(self):
    self.stickler["enabledY"] = not self.stickler["enabledY"]
    print("stickler[enabledY]: ", self.stickler["enabledY"])
