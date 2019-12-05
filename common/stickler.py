
class Stickler:
  def __init__(self, initValue):
    self.mod = initValue["mod"]
    print(self.mod)

  def recalculateX(self, x):
    print("recal", x)
    calcX = x % self.mod
    # short line
    if calcX <= (self.mod / 2):
      x = x - calcX
    else:
      x = x + calcX
    print("recaXl", calcX)
    # 9 - 1 ...
    return x

  def recalculateY(y):
    print("recal y")
    return y
