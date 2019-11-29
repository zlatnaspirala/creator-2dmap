
class StaticGrounds:
  def __init__(self, x, y, w, h, tex):
    self.x = x
    self.y = y
    self.w = w
    self.h = h
    self.x2 = self.w + self.x
    self.y2 = self.h + self.y
    self.texture = tex
