# Name Jesse Coyle
# Date 1/18/2020
# File tile.py
# Desc definitions for tiles
from enum import IntEnum, unique

# Note(Jesse): Instead of enums we may have to use something towards the end, when the user wants to create their own obstacles and obstacle tools
#              probably just going to use this for now for testing..
#              once we add the ability for the user to add more obstacles and obstacle items, we'll have to shove this into a dynamic array of sorts
#              Or perhaps not we could keep a counter starting at the size of the enum and assign the new obstacle value to that number then increment
#              the number... Probably the most interesting way, and we can generalize the case statement for the user defined method based on info
#              from the config file.
# Todo(Jesse): A method of a growing enum, or assigning obstacles a number for use in the map
# Todo/Research(Jesse): Do we want to split tiles into terrain and obstacle enums seperately?
# Usage: tiles.[the enum]
#        tiles.Terrain_grass when referenced will be just a number, 1
@unique
class tiles(IntEnum):
    Void           = 0 # Note(Jesse): An uninitialized and invalid terrain... however, it could be a valid obstacle if no obstacle. 
	                   #              Make sure to check for these when checking for specific tiles
    Terrain_grass  = 1
    Terrain_bog    = 2
    Terrain_forest = 3
    Terrain_water  = 4
    Obstacle_bush  = 5
    Obstacle_tree  = 6
    Obstacle_rock  = 7
    count          = 8 # Note(Jesse): We may keep this around depending on how we want to implement adding obstacles from the config

tileAscii = {
	tiles.Terrain_grass : '.',
	tiles.Terrain_bog   : '_',
    tiles.Terrain_forest: 'f',
    tiles.Terrain_water : '~',
    tiles.Obstacle_bush : '#',
    tiles.Obstacle_tree : '♣',
    tiles.Obstacle_rock : '*'
}

def isValidObstacle(id):
	return id >= tiles.Obstacle_bush and id < tiles.count
