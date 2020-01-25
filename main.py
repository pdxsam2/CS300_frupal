#Name Timothy hall
#Date 1/16/20
#File main.py
#Desc Main entry point for the game

from screen import screenManager, screen, testScreen, tileTestScreen, shopScreen
from tile import Tiles
from user import user
from item import add_item

class GameState:
	screenManager = screenManager()
	user = user()
	tiles = Tiles()
	items = []

#Main program loop
def main():
	state = init()
	running = True

	while(running):	#run until user quits all game screens
		state.screenManager.update(state)
		state.screenManager.draw(state)
		state.screenManager.handleInput(state)
		running = not state.screenManager.isEmpty()

#Method to initialize anything prior to starting the game loop
def init():
	state = GameState()
	
	# Todo(Jesse): Put these into the config when it's there
	state.tiles.add_terrain("grass", '.', 1)  # id = 1
	state.tiles.add_terrain("bog", '_', 2)    # id = 2
	state.tiles.add_terrain("forest", 'f', 3) # id = 3
	state.tiles.add_terrain("water", '~', 1)  # id = 4 ... We'll need to special case this on the character side

	state.tiles.add_obstacle("bush", '#', 2)  # id = 1
	state.tiles.add_obstacle("tree", '♣', 3)  # id = 2
	state.tiles.add_obstacle("rock", '*', 2)  # id = 3
	
	add_item(state, "Power Bar", 10)
	add_item(state, "Binoculars", 30)
	add_item(state, "Weed Whacker", 10) # Note(Jesse): What if the store just sold gasoline and you can use it for any of these? Galaxy Brain
	add_item(state, "Jack Hammer", 20)
	add_item(state, "Chain Saw", 10)
	
	add_item(state, "1 Chain Saw", 10)
	add_item(state, "2 Chain Saw", 10)
	add_item(state, "3 Chain Saw", 10)
	add_item(state, "4 Chain Saw", 10)
	add_item(state, "5 Chain Saw", 10)
	add_item(state, "6 Chain Saw", 10)
	add_item(state, "7 Chain Saw", 10)
	add_item(state, "8 Chain Saw", 10)
	add_item(state, "9 Chain Saw", 10)
	add_item(state, "10Chain Saw", 10)
	add_item(state, "11Chain Saw", 10)
	add_item(state, "12Chain Saw", 10)
	add_item(state, "13Chain Saw", 10)

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
	
	# screenManager.setScreen(testScreen())
	state.screenManager.setScreen(state, tileTestScreen())
	# screenManager.setScreen(shopScreen())
	
	return state




if __name__ == "__main__":
	main()
