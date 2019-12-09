
import array

class Stickler:

  def __init__(self, initValue):
    self.initValue = initValue
    self.mod = initValue.stickler["mod"]
    self.gridWidth = initValue.gridWidth
    print(self.mod)

  def setMargin(self, newMargin):
    self.mod = newMargin

  def recalculateX(self, x):

    print("recal", x)
    localSample = []
    LocalSampleValue = []

    # just default
    localRightOrLeft = "right"

    for locGrid in range(100, 2000, self.gridWidth):
      # print(x)
      # sample
      localSample.append(abs(locGrid - x))
      LocalSampleValue.append(locGrid)

    res_min = min(float(sub) for sub in localSample)

    if res_min < self.mod:
      lookAT = localSample.index(res_min)
      print("min ", res_min)
      if LocalSampleValue[lookAT] - x > 0:
        fixPoint = LocalSampleValue[lookAT] - self.initValue.ELEMENT_WIDTH
        x = fixPoint
        print("LEFT")
      else:
        fixPoint = LocalSampleValue[lookAT]
        print("FP ", fixPoint)
        x = fixPoint
    print("outcall x", x)
    return x

  def recalculateY(self, y):
    print("recal y")
    return y
