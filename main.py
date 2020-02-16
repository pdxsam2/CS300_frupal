#Name Timothy hall
#Date 1/16/20
#File main.py
#Desc Main entry point for the game

from screen import screenManager, screen, testScreen, playScreen, shopScreen, menu
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
	entities = []

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

	add_item(state, "Power Bar", 10)
	add_item(state, "Binoculars", 30)
	add_item(state, "Weed Whacker", 10) # Note(Jesse): What if the store just sold gasoline and you can use it for any of these? Galaxy Brain
	add_item(state, "Jack Hammer", 20)
	add_item(state, "Chain Saw", 10)
	add_item(state, "Boat", 50)
	
	add_entity(state, "Magic Jewel")
	add_entity(state, "Hungry Tile")
	
	# Todo(Jesse): Start reading the config here

	'''
	# Note(Jesse): Debug printing out... might be useful for the config readin
	for index in range(0, len(state.tiles.terrain)):
		terrain = state.tiles.terrain[index]
		print("Terrain(", index, "):", terrain.name, "ascii:", terrain.ascii, "energy use:", terrain.energy)

	print("")

	for index in range(0, len(state.tiles.obstacles)):
		obstacle = state.tiles.obstacles[index]
		print("Obstacle(", index, "):", obstacle.name, "ascii:", obstacle.ascii, "energy use:", obstacle.energy)

	print("")

	for index in range(0, len(state.items)):
		item = state.items[index]
		print("Item(", index, "):", item.name, "costs:", item.cost, "[currency]")

	print("///////// End Debug Print")
	'''
	
	# screenManager.setScreen(state, tileTestScreen())
	# screenManager.setScreen(shopScreen())
	screenManager.setScreen(state, menu())

	return state




if __name__ == "__main__":
	main()
