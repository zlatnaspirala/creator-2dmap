
import array

class Stickler:

  def __init__(self, initValue, initGrid):
    self.mod = initValue["mod"]
    self.gridWidth = initGrid
    print(self.mod)

  def setMargin(self, newMargin):
    self.mod = newMargin

  def recalculateX(self, x):

    print("recal", x)
    localSample = []
    LocalSampleValue = []

    for locGrid in range(100, 2000, self.gridWidth):
      # print(x)
      # sample
      localSample.append(abs(locGrid - x))
      LocalSampleValue.append(locGrid)

    res_min = min(float(sub) for sub in localSample)

    if res_min < self.mod:
      lookAT = localSample.index(res_min)
      print("min ", res_min)
      fixPoint = LocalSampleValue[lookAT]
      print("FP ", fixPoint)
      x = fixPoint
    print("outcall x", x)
    return x

  def recalculateY(self, y):
    print("recal y")
    return y
