#Name Timothy hall
#Date 1/16/20
#File main.py
#Desc Main entry point for the game

from screen import screenManager, splashScreen
from tile import Tiles
from user import user
from item import add_item
from entity import add_entity
from config import loadConfig

from platform import system
if "win" in system().lower(): #works for Win7, 8, 10 ...
    from ctypes import windll
    kernel=windll.kernel32
    kernel.SetConsoleMode(kernel.GetStdHandle(-11),7)

from platform import system
if "win" in system().lower(): #works for Win7, 8, 10 ...
    from ctypes import windll
    kernel=windll.kernel32
    kernel.SetConsoleMode(kernel.GetStdHandle(-11),7)

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
	x_dim= 25
	y_dim= 35

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

	loadConfig(state)
	state.total_entity_chance = 0

	add_entity(state, "Magic Jewel", 0.0)
	add_entity(state, "Greedy Tile", 0.0075)

	#screenManager.setScreen(state, menu())
	screenManager.setScreen(state, splashScreen())
	return state




if __name__ == "__main__":
	main()
