#Name Jesse Coyle
#Date 2/08/20
#File map.py
#Desc Map definitions

import random

class Map:

	# Note(Jesse):
	# The generated map is completely random given if the terrain generated is water, no obstacle will be placed
	# The map is generated into a 3D array, a 2D array of 3 layers
	#	layer 1, index 0: Terrain as an ID
	#	layer 2, index 1: Obstacles as an ID
	#	layer 3, index 2: Tile is visible as a boolean
	# The IDs from the terrain and obstacles and randomly grabbed from the terrain and obstacle arrays respectivly
	def __init__(self, tiles, width, height):
		self.arr = []
		self.width = width
		self.height = height
		
		for row in range(0, height):
			for col in range(0, width):
				tile = []
				terrain = random.randint(1, len(tiles.terrain) - 1)
				tile.append(terrain) # Note(Jesse): terrain
				if terrain == 4: # Note(Jesse): Terrain is water
					tile.append(0)
				else:
					tile.append(random.randint(0, len(tiles.obstacles) - 1)) # Note(Jesse): obstacle
				tile.append(False) # Note(Jesse): visible
				self.arr.append(tile)
	
	
	# Note(Jesse): Gets the terrain ID from the 
	def get_terrain(self, x, y):
		assert(y < self.height and x < self.width and x >= 0 and y >= 0)
		return self.arr[y*self.width + x][0]
	
	# Note(Jesse):
	#
	#
	#
	def get_obstacle(self, x, y):
		assert(y < self.height and x < self.width and x >= 0 and y >= 0)
		return self.arr[y*self.width + x][1]
	
	# Note(Jesse):
	#
	#
	#
	def has_obstacle(self, x, y):
		assert(y < self.height and x < self.width and x >= 0 and y >= 0)
		return self.arr[y*self.width + x][1] > 0
	
	# Note(Jesse):
	#
	#
	#
	def is_visible(self, x, y):
		assert(y < self.height and x < self.width and x >= 0 and y >= 0)
		return self.arr[y*self.width + x][2] == 1
		
