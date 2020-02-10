#Name Sam Parker
#Date 1/19/20
#File user.py
#Desc This is the user that will be affected by the obstacles/terrain on the current tile

#Implementation Changes: Austin Brown
#Date 2/2/20

class user:
  #Status   Note(Sam): these numbers were arbitrarily chosen and should be adjusted relative to how the game feels to play
  energy= 20
  money= 100

  x = 0
  y = 0

  # Note(Jesse): An array of integers, the index is the index in the items array from item.py
  inv = []

  def set_position(self, x, y):
    self.x = x
    self.y = y

  # Note(Austin): This now returns if the user is able to move
  def move(self, dx, dy, delta_energy):
    if delta_energy > self.energy:
      return False
    self.x += dx
    self.y += dy
    self.energy -= delta_energy # Note(Jesse): This is negative just because it's probably more convenient
    return True

  # Note(Austin): This is just simple selection structure. We could maybe store what satisfies what in either the item class or the obstacle class?
  def dealWith(self, obstacle):
    # there is no obstacle
    if obstacle.name == "null":
      return True

    '''
    if obstacle.name == "bush" and self.inv[2] > 0: # Note(Austin): Player inventory index is based on the order that items were added in main,
      obstacle.reset()                              # so if the order is changed, this breaks
    if obstacle.name == "tree" and self.inv[4] > 0: # Note(Jesse): What we will probably do and might be easiest is each obstacle will have an item ID
      obstacle.reset()                              # such that if the player has an amount of that item ID, it will be easier to deal with.
    if obstacle.name == "rock" and self.inv[3] > 0:
      obstacle.reset()
    '''
    return False

  def reveal_surroundings(self, map):
    radius = 1
    if self.inv[1] > 0: # Note(Jesse): If has Binoculars
      radius = 2

    for row in range(self.y - radius, self.y + radius + 1):
      for col in range(self.x - radius, self.x + radius + 1): # Note(Jesse): Iterating through a radius appron around the player
        if row >= 0 and row < map.height and col >= 0 and col < map.width:
          map.set_visible(col, row) # Note(Jesse): Yes, we are setting the tile visible whether it's visible or not, redundantly

  # Todo(Jesse): Edge of map detection
  def move_north(self, terrain, obstacle):
    if user.dealWith(self, obstacle):
      cost = terrain.energy
    else:
      cost = obstacle.energy
    return self.move(0, 1, cost)
    
  def move_south(self, terrain, obstacle):
    if user.dealWith(self, obstacle):
      cost = terrain.energy
    else:
      cost = obstacle.energy
    return self.move(0, -1, cost)

  def move_east(self, terrain, obstacle):
    if user.dealWith(self, obstacle):
      cost = terrain.energy
    else:
      cost = obstacle.energy
    return self.move(1, 0, cost)

  def move_west(self, terrain, obstacle):
    if user.dealWith(self, obstacle):
      cost = terrain.energy
    else:
      cost = obstacle.energy
    return self.move(-1, 0, cost)


###testing###
def main():
  testee= user()
  
  tiles.add_terrain("grass", '.', 1)  # id = 1
  tiles.add_terrain("bog", '_', 2)    # id = 2
  tiles.add_terrain("forest", 'f', 3) # id = 3
  tiles.add_terrain("water", '~', 1)  # id = 4 ... We'll need to special case this on the character side
  
  tiles.add_obstacle("bush", '#', 2)  # id = 1
  tiles.add_obstacle("tree", '♣', 3)  # id = 2
  tiles.add_obstacle("rock", '*', 2)  # id = 3
  
  print('Current money: ', testee.money, '\n')
  print('Current energy: ', testee.energy, '\n')

  cool_map = [[1, 2], [1, 3]]
  
  testee.move(0, 1, tiles.terrain[cool_map[testee.x][testee.y]].energy)
  testee.move(1, 0, tiles.terrain[cool_map[testee.x][testee.y]].energy)
  testee.move(0, -1, tiles.terrain[cool_map[testee.x][testee.y]].energy)

  print('Current money: ', testee.money, '\n')
  print('Current energy: ', testee.energy, '\n')


# main()
