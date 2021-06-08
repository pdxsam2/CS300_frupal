#Name Timothy hall
#Date 1/16/20
#File main.py
#Desc Main entry point for the game

from screen import Screen_Manager, Splash_Screen
from tile import Tiles
from user import User
from item import add_item
from entity import add_entity
from config import load_config

from platform import system
if "win" in system().lower(): #works for Win7, 8, 10 ...
    from ctypes import windll
    kernel=windll.kernel32
    kernel.SetConsoleMode(kernel.GetStdHandle(-11),7)

class Camera:
	x = 0
	y = 0
	viewport = 0

class Game_State:
	user = User()
	config_energy = 0
	config_money = 0
	tiles = Tiles()
	camera = Camera()
	items = []
	entity_manifest = []
	entities = []
	total_entity_chance = 0
	x_dim = 25
	y_dim = 35
	intro_flag= 0

screen_manager = Screen_Manager()

#Main program loop
def main():
	state = init()
	running = True

	while(running):	#run until user quits all game screens
		screen_manager.update(state)
		screen_manager.draw(state)
		screen_manager.handle_input(state)
		running = not screen_manager.is_empty()

#Method to initialize anything prior to starting the game loop
def init():
	state = Game_State()

	load_config(state)
	state.total_entity_chance = 0

	add_entity(state, "Magic Jewel", 0.0)
	add_entity(state, "Greedy Tile", 0.0075)

	#screen_manager.set_screen(state, menu())
	screen_manager.set_screen(state, Splash_Screen())
	return state




if __name__ == "__main__":
	main()
