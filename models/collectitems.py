
# export interface ICollectionItem extends IStaticItem {
#   colectionLabel: string;
#   points: number;
# }
from models.ground import StaticGrounds

class CollectingItems(StaticGrounds):
  def __init__(self, x, y, w, h, tex, tilesX, tilesY, colectionLabel, points):
    super().__init__(x, y, w, h, tex, tilesX, tilesY)
    self.colectionLabel = colectionLabel
    self.points = points
    print("Created model for collect item", colectionLabel)
