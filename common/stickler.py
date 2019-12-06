
import array

class Stickler:
  def __init__(self, initValue):
    self.mod = initValue["mod"]
    print(self.mod)

  def recalculateX(self, x):

    print("recal", x)
    localSample = []
    LocalSampleValue = []

    for locGrid in range(100, 2000, 100):
      # print(x)
      # sample
      localSample.append(abs(locGrid - x))
      LocalSampleValue.append(locGrid)
      print(localSample[0])

    res_min = min(float(sub) for sub in localSample)

    if res_min < self.mod:
      lookAT = localSample.index(res_min)
      print("min ", res_min)
      fixPoint = LocalSampleValue[lookAT]
      print("FP ", fixPoint)
      x = fixPoint

    return x

  def recalculateY(y):
    print("recal y")
    return y
