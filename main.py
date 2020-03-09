#Name Timothy hall
#Date 1/16/20
#File main.py
#Desc Main entry point for the game

from screen import screenManager, screen, testScreen, splashScreen, playScreen, shopScreen, menu
from tile import Tiles
from user import user
from item import add_item
from entity import add_entity

class Camera:
	x = 0
	y = 0
	viewport = 0

class GameState:
	user = user()
	tiles = Tiles()
	camera = Camera()
	items = []
	entity_manifest = []
	entities = []
	total_entity_chance = 0

screenManager = screenManager()

#Main program loop
def main():
	state = init()
	running = True


	while(running):	#run until user quits all game screens
		screenManager.update(state)
		screenManager.draw(state)
		screenManager.handleInput(state)
		running = not screenManager.isEmpty()

#Method to initialize anything prior to starting the game loop
def init():
	state = GameState()

	# Note(Jesse): I don't think these should be moved into the config, we should think on this one perhaps
	state.tiles.add_terrain("grass", '.', 1)  # id = 1
	state.tiles.add_terrain("bog", '_', 2)    # id = 2
	state.tiles.add_terrain("forest", 'f', 2) # id = 3
	state.tiles.add_terrain("water", '~', 1)  # id = 4 ... We'll need to special case this on the character side

	state.tiles.add_obstacle("bush", '#', 2)  # id = 1
	state.tiles.add_obstacle("tree", '♣', 3)  # id = 2
	state.tiles.add_obstacle("rock", '*', 2)  # id = 3

	add_item(state, "Power Bar", 10, 0, True)
	add_item(state, "Binoculars", 30, 0, False)
	add_item(state, "Weed Whacker", 10,1, False) # Note(Jesse): What if the store just sold gasoline and you can use it for any of these? Galaxy Brain
	add_item(state, "Jack Hammer", 20, 2, False)
	add_item(state, "Chain Saw", 10, 3, False)
	add_item(state, "Boat", 50, 0, False)

	state.total_entity_chance = 0
	add_entity(state, "Magic Jewel", 0.0)
	add_entity(state, "Greedy Tile", 0.0075)

	#screenManager.setScreen(state, menu())
	screenManager.setScreen(state, splashScreen())
	return state




if __name__ == "__main__":
	main()
