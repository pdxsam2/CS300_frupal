#Name Timothy hall
#Date 1/16/20
#File main.py
#Desc Main entry point for the game
#test change and some more of those
from screen import screenManager, splashScreen
from tile import Tiles
from user import user
from item import addItem
from entity import addEntity
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
	config_energy = 0
	config_money = 0
	tiles = Tiles()
	camera = Camera()
	items = []
	entity_manifest = []
	entities = []
	total_entity_chance = 0
	x_dim= 25
	y_dim= 35
	intro_flag= 0

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
	state.totalEntityChance = 0

	addEntity(state, "Magic Jewel", 0.0)
	addEntity(state, "Greedy Tile", 0.0075)

	#screenManager.setScreen(state, menu())
	screenManager.setScreen(state, splashScreen())
	return state




if __name__ == "__main__":
	main()
