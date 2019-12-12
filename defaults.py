
class InitialData:
  def __init__(self):
    self.exportInOneLine = False
    self.absolutePacksPathEnabled = True
    self.absolutePacksPath = "E:\\web_server\\xampp\htdocs\\PRIVATE_SERVER\\visual-ts\\project\\visual-ts\\src\\examples\\platformer\\scripts\\packs\\"
    self.stickler = {}
    self.stickler["enabledX"] = True
    self.stickler["enabledY"] = True
    self.stickler["mod"] = 30
    self.gridWidth = 50
    self.exportScale = 2
    self.ELEMENT_WIDTH=20
    self.ELEMENT_HEIGHT=20
    self.incDecWidth = 5
    self.incDecHeight = 5
    self.windowBackgroundColor = "#000000"
    self.topFrameBackgroundColor = "#010233"
    self.canvasGridVisible = True
    self.tilesX = 5
    self.tilesY = 1
    self.rotateValues = False
  def redefineExportScale(self, newExportScale):
    self.exportScale = newExportScale
    print("Redefine init value for exportScale = ", newExportScale)
  def setSticklerEnabledX(self):
    self.stickler["enabledX"] = not self.stickler["enabledX"]
    print("stickler[enabledX]: ", self.stickler["enabledX"])
  def setSticklerEnabledY(self):
    self.stickler["enabledY"] = not self.stickler["enabledY"]
    print("stickler[enabledY]: ", self.stickler["enabledY"])
