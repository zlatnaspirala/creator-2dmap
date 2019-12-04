
class InitialData:
  def __init__(self):
    self.exportInOneLine = false;
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
