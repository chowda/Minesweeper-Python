from tile import Tile
from random import randint
from itertools import chain

class Board:
  def __init__(self, height, width, mines):
    self.height = height
    self.width = width
    self.mines = mines
    self.tiles = []
    self.__setup_board()
    self.__randomize_mines()
    self.__assign_mines_touching()

  def print_board(self):
    print "Board size: %s x %s | Mines: %s" % (self.height, self.width, self.mines)
    for y in range(0, self.height, 1):
      line = ''
      for x in range(0, self.width, 1):
        if self.tiles[x][y].bomb == True:
          line += " * "
        else:
          line += " %s " % str(self.tiles[x][y].mines_touching)
      print line

  ### PRIVATE

  def __setup_board(self):
    for x in range(0, self.width, 1):
      self.tiles.append( [] )
      for y in range(0, self.height, 1):
        self.tiles[x].append( Tile(x, y) )

  def __randomize_mines(self):
    assigned = 0

    while assigned < self.mines:
      x = randint(0, self.width - 1)
      y = randint(0, self.height - 1)
      tile = self.tiles[x][y]
      if tile.bomb == False:
        tile.bomb = True
        assigned += 1

  # Find how many neighboring tiles have a bomb and assign the count.
  def __assign_mines_touching(self):
    for tile in list(chain(*self.tiles)):
      neighbors = self.__get_neighbors(tile)
      tile.mines_touching = self.__count_mines_from_neighbors(neighbors)

  # This is a little tricky, and there is probably a better way to do this. Here is what I'm doing.
  # Look for tiles whose position is +/- 1 in every direction from the current tile.
  # Don't collect the current tile.
  def __get_neighbors(self, tile):
    holder = []
    for t in list(chain(*self.tiles)):
      if (tile.x - 1 <= t.x <= tile.x + 1) and (tile.y - 1 <= t.y <= tile.y + 1) and (tile != t):
        holder.append(t)

    return holder

  # From the neighboring tiles count the number that have a bomb.
  def __count_mines_from_neighbors(self, neighbors):
    count = 0
    for n in neighbors:
      if n.bomb == True:
        count += 1

    return count
