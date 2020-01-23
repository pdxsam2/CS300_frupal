#Name Sam Parker
#Date 1/19/20
#File user.py
#Desc This is the user that will be affected by the obstacles/terrain on the current tile

class user:
  #Status   Note(Sam): these numbers were arbitrarily chosen and should be adjusted relative to how the game feels to play
  energy= 20
  money= 100

  x = 0
  y = 0

  # Note(Jesse): An array of integers, the index is the index in the items array from items.py
  inv = []
  
  # Note(Jesse): Woah! Setters! Probably just going to be using these in the movement code, 
  #              in which case we probably won't even use these
  def decrement_energy(self, val):
    self.energy -= val

  def increment_energy(self, val):
    self.energy += val
	
  def set_position(self, x, y):
    self.x = x
    self.y = y

  def move(self, dx, dy, delta_energy):
    self.x += dx
    self.y += dy
    self.energy -= delta_energy # Note(Jesse): This is negative just because it's probably more convenient
	

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
