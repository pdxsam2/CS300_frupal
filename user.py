#Name Sam Parker
#Date 1/19/20
#File user.py
#Desc This is the user that will be affected by the obstacles/terrain on the current tile

#Implementation Changes: Austin Brown
#Date 2/2/20
from item import Item, getSlot
from entity import Entity, hasEntityAt, getEntityAt, removeEntityAt, findFirstEntity, entityExists

import math

class user:
  #Status   Note(Sam): these numbers were arbitrarily chosen and should be adjusted relative to how the game feels to play
  energy= 20
  money= 100
  magic_jewels = 0

  x = 0
  y = 0

  # Note(Jesse): An array of integers, the index is the index in the items array from item.py
  inv = []

  def setPosition(self, x, y):
    self.x = x
    self.y = y
  
  def exert(self, cost):
    self.energy -= cost
    return " You have lost " + str(cost) + " energy."

  # Note(Austin): This now returns if the user is able to move
  def move(self, dx, dy, delta_energy):
    if delta_energy > self.energy:
      return False
    self.x += dx
    self.y += dy
    return True


  # Note(Austin): This checks if the user has the correct item for the given obstacle
  def dealWith(self, obstacle, items):
    item_name  = ""
    for item in items:
      if item.obst == obstacle:
        if self.inv[item.slot] > 0:
          item_name = item.name
    return item_name

  def revealSurroundings(self, items, map):
    radius = 1
    if self.inv[getSlot(items, "Binoculars")] > 0: # Note(Jesse): If has Binoculars
      radius = 2

    for row in range(self.y - radius, self.y + radius + 1):
      for col in range(self.x - radius, self.x + radius + 1): # Note(Jesse): Iterating through a radius appron around the player
        if row >= 0 and row < map.height and col >= 0 and col < map.width:
          map.tileSetVisible(col, row)

  # Rework: Austin 3/10/20
  def action(self, map, items, tiles, entities, usrin):
    if usrin == "w":
      newX = self.x
      newY = self.y + 1
      direction = "north"
    elif usrin == "s":
      newX = self.x
      newY = self.y - 1
      direction = "south"
    elif usrin == "d":
      newX = self.x + 1
      newY = self.y
      direction = "east"
    elif usrin == "a":
      newX = self.x - 1
      newY = self.y
      direction = "west"
    elif usrin == "e":
      power_bar_index = getSlot(items, "Power Bar")
      if self.inv[power_bar_index] > 0:
        self.inv[power_bar_index] -= 1
        self.energy += 10
        return "You consumed a Power Bar. +10 Energy!"
      else:
        return "You do not have any Power Bars left."
    elif usrin == "v":
      self.magic_jewels += 1
      map.revealMap()
      self.energy = 4294967295
      self.money = 4294967295
      return "Nothing can stop you now!"
    elif usrin == "l":
      if entity_exists(entities, "Magic Jewel") and self.inv[get_slot(items, "Magic Locator")] > 0:
        jewels = find_first_entity(entities, "Magic Jewel");
        diffX = jewels.x - self.x
        diffY = jewels.y - self.y
        if diffX == 0 and diffY == 0:
          # Note(Jesse): Ideally I imagine the user wouldn't see this message since they win when they go onto the tile, perhaps?
          return "This device becomes heavy, and makes a peculiar sound. Upon this ground, you know magic is to be found."
        elif abs(diffX) > abs(diffY):
          if diffX < 0:
            return "The Locator pulls itself somewhat Westward"
          else:
            return "The Locator feels a need to go Eastward"
        elif abs(diffX) <= abs(diffY):
          if diffY < 0:
            return "The Locator tends Southbound"
          else:
            return "The Locator urges Northward"
      else:
        return "You scratch your head."
    else:
      return "Invalid Input!"
      
    # bounds check
    if newX > map.width - 1 or newX < 0 or newY > map.height - 1 or newY < 0:
      return "You cannot leave the island."

    terrain_id = map.getTerrainId(newX, newY)
    obstacle_id = map.getObstacleId(newX, newY)
    # water
    boat_slot = getSlot(items, "Boat")
    if int(boat_slot) > 0:
      to_return = "You cannot cross water without a boat."
      if terrain_id == 4 and self.inv[boat_slot] < 1:
        if self.energy > 0:
          return to_return + self.exert(1)
        else:
          return to_return
    # test code
    else:
      return "It's broken! panic! boat_slot is: " + str(boat_slot)

    #obstacles
    if map.coordHasObstacle(newX, newY):
      item_name = self.dealWith(map.getObstacleId(newX, newY), items)
      if item_name != "":
        to_return = "You try to remove the " + tiles.obstacles[obstacle_id].name + " with your " + item_name + ","
        cost = 1
      else:
        to_return = "You try remove the " + tiles.obstacles[obstacle_id].name + " with brute force,"
        cost = tiles.obstacles[obstacle_id].energy
      if (cost > self.energy):
        return to_return + " but do not have the energy."
      else:
        map.coordRemoveObstacle(newX, newY)
        self.money += 3
        return to_return + " and succeed! +3 gold!" + self.exert(cost)
    
    #movement
    if self.move(newX - self.x, newY - self.y, tiles.terrain[terrain_id].energy):
      if hasEntityAt(entities, newX, newY):
        entity = getEntityAt(entities, newX, newY)
        if entity.id == 2:  # Note(Jesse): Greedy Tile
          self.money = math.floor(self.money*0.5)
          to_return = ", where a greedy tile stole half your money!"
        elif entity.id == 1: # Note(Jesse): Magic Jewel
          self.magic_jewels += 1
          to_return = ", where you found The Magic Jewels!"
        removeEntityAt(entities, newX, newY)
        return "You moved " + direction + " onto a " + tiles.terrain[terrain_id].name + to_return + self.exert(tiles.terrain[terrain_id].energy)
      return "You moved " + direction + " onto a " + tiles.terrain[terrain_id].name + '.' + self.exert(tiles.terrain[terrain_id].energy)
    return "You do not have enough energy to move " + direction + " onto a " + tiles.terrain[terrain_id].name + '.'
