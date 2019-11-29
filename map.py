
class myMap:
  def __init__(self, name):
    self.name = name
    self.map = []
    self.clipboardElementMemo = 0

  def add(self, x):
    self.map.append(x)
    print("New element", x)
    print("New element added to the current map: " + self.name)

  def clear(self):
    self.map.clear()

  def removeLast(self):
    self.clipboardElementMemo = self.map.pop()
