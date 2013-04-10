class Tile:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.bomb = False
    self.mines_touching = 0
