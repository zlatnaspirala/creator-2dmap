
class StaticGrounds:
  def __init__(self, x, y, w, h, tex, tilesX, tilesY):
    self.x = float(x)
    self.y = float(y)
    self.w = float(w)
    self.h = float(h)
    self.x2 = float(self.w) + float(self.x)
    self.y2 = float(self.h) + float(self.y)
    self.texture = tex
    self.tilesX = float(tilesX)
    self.tilesY = float(tilesY)
