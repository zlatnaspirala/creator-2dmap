
# export interface ICollectionItem extends IStaticItem {
#   colectionLabel: string;
#   points: number;
# }
from models.ground import StaticGrounds

class Enemies(StaticGrounds):
  def __init__(self, x, y, w, h, tex, tilesX, tilesY, enemyLabel, enemyOptions=1):
    super().__init__(x, y, w, h, tex, tilesX, tilesY)
    self.enemyLabel = enemyLabel
    self.enemyOptions = enemyOptions
    print("Created model for enemy", enemyLabel)
