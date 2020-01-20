#Name: Sam Parker
#Date 1/19/20
#File user.py
#Desc This is the user that will be affected by the obstacles/terrain on the current tile

class user:
  #Terrain types


  grass= 1
  bog= 2
  forest= 2
  water= 2
  #Obstacles
  bush= 2
  tree= 2
  rock= 2
  #Status   Note(Sam): these numbers were arbitrarily chosen and should be adjusted relative to how the game feels to play
  energy= 20
  money= 100

  #Inventory
  ####this will end up being an array of inventory items which will adjust the "damage" accordingly

  def Affect(self,terrain, obstacle):
    #these values should be compared with those from the tiles struct from tiles.py
    if terrain == 1:
      self.energy -= self.grass;
    elif terrain == 2:
      self.energy -= self.bog
    elif terrain == 3:
      self.energy -= self.forest
    elif terrain == 4:
      self.energy -= self.water
    else:
      self.energy -= 1

    if obstacle == 5:
      self.energy -= self.bush
    if obstacle == 6:
      self.energy -= self.tree
    if obstacle == 7:
      self.energy -= self.rock

###testing###
def main():
  testee= user()

  print('Current money: ', testee.money, '\n')
  print('Current energy: ', testee.energy, '\n')

  testee.Affect(2,5)
  testee.Affect(0,0)
  testee.Affect(1,6)

  print('Current money: ', testee.money, '\n')
  print('Current energy: ', testee.energy, '\n')

main()
