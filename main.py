#Name Timothy hall
#Date 1/16/20
#File main.py
#Desc Main entry point for the game

from screen import screenManager, screen, testScreen, tileTestScreen
from tile import tiles

screenManager = screenManager()

#Main program loop
def main():
	init()
	running = True

	while(running):	#run until user quits all game screens
		screenManager.update()
		screenManager.draw()
		screenManager.handleInput()
		running = not screenManager.isEmpty()

#Method to initialize anything prior to starting the game loop
def init():
	# Todo(Jesse): Put these into the config when it's there
	tiles.add_terrain("grass", '.', 1)  # id = 1
	tiles.add_terrain("bog", '_', 2)    # id = 2
	tiles.add_terrain("forest", 'f', 3) # id = 3
	tiles.add_terrain("water", '~', 1)  # id = 4 ... We'll need to special case this on the character side

	tiles.add_obstacle("bush", '#', 2)  # id = 1
	tiles.add_obstacle("tree", '♣', 3)  # id = 2
	tiles.add_obstacle("rock", '*', 2)  # id = 3
	
	# Todo(Jesse): Start reading the config here
	
	# screenManager.setScreen(testScreen())
	screenManager.setScreen(tileTestScreen())




if __name__ == "__main__":
	main()
