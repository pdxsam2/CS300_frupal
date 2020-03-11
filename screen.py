#Name Timothy hall
#Date 1/16/20
#File screen.py
#Desc base class for menu/game screens

from stack import stack

from tile import Tiles, Terrain, Obstacle

from user import user

from map import Map

from item import add_item
from entity import Entity, has_entity_at, get_entity_at, remove_entity_at
from config import saveConfig

import random
import copy
import math
import time

# Note(Jesse): These three classes are used to get raw input from the terminal/commandprompt
class Get_Char:
    def __init__(self):
        try:
            self.cb = Get_Char_Windows()
        except ImportError:
            self.cb = Get_Char_Nix()

    def __call__(self): return self.cb()

class Get_Char_Nix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        stdinfile = sys.stdin.fileno()
        prev_settings = termios.tcgetattr(stdinfile)
        try:
            tty.setraw(sys.stdin.fileno())
            char = sys.stdin.read(1)
        finally:
            termios.tcsetattr(stdinfile, termios.TCSADRAIN, prev_settings)
        return char

class Get_Char_Windows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        byte = msvcrt.getch()
        if byte == b'\xe0':
            byte = msvcrt.getch()
            return byte.decode("utf-8")
        else:
            return byte.decode("utf-8")

get_char = Get_Char()

#Method to clear the screen for screenManager class
def _clear():
	for i in range(40):
		print("\n")

##########################################################################
#                               Screen
##########################################################################
#base class for all screens/menus
class screen:

	def __init__(self):
		self.screenman = None

	#called when the screen is launched. Anything being loaded
	#or initalized should happen here.
	def onStart(self):
		print("Starting")

	#Method to draw screen to console. This is called every
	#iterarion of the game loop, so the screen should only
	#be written once per call. Clearing the previous frame
	#happens after handleInput() is called, so it is not
	#necessary to do it here.
	def draw(self):
		print("Drawing")

	#Updates game logic. Called every iteration of game loop.
	#Place to update any background logic not relavent to user
	#input. May not need this but its here if it is needed.
	def update(self):
		print("Updating")

	#Handles user input. Input is  prompted for in screenManager
	#so it is not  necessary to do it here. This method indirectly
	#controls the while loop
	#[usrin]= the user input
	def handleInput(self, usrin):
		print("Handling input")

	#Called when the screen is closed. Loose ends that need to be
	#tied up or anything that happens when leaving the screen is handled
	#here.
	def onStop(self, state):
		print("Stoping")

	#allows screen to add a screen to the stack above it
	def pushScreen(self, state, screen):
		self.screenman.setScreen(state, screen)

	#called in screenman when added to the stack. Do Not implement in subclasses
	def setScreenManager(self, screenman):
		self.screenman = screenman #Mr. Screenman, bring me a screen.

###########################################################################
#                            Splash Screen
###########################################################################
#Auth Timothy Hall
#Date 6 March 2020
class splashScreen(screen):
	def onStart(self, state):
		return None

	def draw(self, state):
		print("\n\t\t\t\tTeam B Presents:\n\n")
		print("    	 ,gggggggggggggg                                                  ")
		print("    dP\"\"\"\"\"\"88\"\"\"\"\"\"                                            ,dPYb,")
		print("    Yb,_    88                                                  IP'`Yb")
		print("    `\"\"     88                                                  I8  8I")
		print("         ggg88gggg                                              I8  8\'")
		print("            88   8,gggggg,  gg      gg  gg,gggg,      ,gggg,gg  I8 dP ")
		print("            88    dP\"\"\"\"8I  I8      8I  I8P\"  \"Yb    dP\"  \"Y8I  I8dP  ")
		print("      gg,   88   ,8'    8I  I8,    ,8I  I8'    ,8i  i8'    ,8I  I8P   ")
		print("       \"Yb,,8P  ,dP     Y8,,d8b,  ,d8b,,I8 _  ,d8' ,d8,   ,d8b,,d8b,_ ")
		print("         \"Y8P\'  8P      `Y88P\'\"Y88P\"`Y8PI8 YY88888PP\"Y8888P\"`Y88P\'\"Y88")
		print("                                        I8                            ")
		print("                                        I8                            ")
		print("                                        I8                            ")
		print("                                        I8                            ")
		print("                                        I8                            ")
		print("                                        I8                            ")

		print("\n\n\t\tA Game of Adventure, Boats and Weed Wackers.")
		print("Press any key to continue...")


	def handleInput(self, state, usrin):
		self.pushScreen(state, menu())
		self.screenman.closeScreen(state, 0)	#note(Tim): This screen needs to be removed from the
																					#Stack otherwise user will return to it when quiting
																					#the game

	def update(self, state):
		return

###########################################################################
#                            Shop Screen
###########################################################################
#Updated by Timothy Hall 3/8/20
class shopScreen(screen):
	page = 0

	def __init__(self):
		self.message = "Welcome to the shop!"

	def onStart(self, state):
		return

	def draw(self, state):
		s = "****************************************\n"
		s +="               Inventory                \n"
		s +="****************************************\n\n"
		s += "Coins: " + str(state.user.money) + "\n\n"

		for index in range(0, 8):
			arr_index = index + self.page*8
			if len(state.items) <= arr_index:
				s += '\n'
			else:
				item = state.items[arr_index]
				temp = "[" + str(index + 1) + "] " + item.name + '(' + str(state.user.inv[arr_index]) + "):"
				whitespace = 38 - len(str(temp))
				for i in range(whitespace):
					temp += ' '
				s += temp + str(item.cost) + '\n'
				#s += '[' + str(index + 1) + "] " + item.name + '(' + str(state.user.inv[arr_index]) + "):\t\t" + str(item.cost) + '\n'

		if self.page > 0:
			s += "[9] Prev Page\n"
		else:
			s += "\n"

		if len(state.items) - self.page*8 > 8:
			s += "[0] Next Page\n"
		else:
			s += '\n'

		s += "[page: " + str(self.page) + ']\n'

		print(s)

		print(self.message + "\n[press q to exit shop]")

	def update(self, state):
		return

	def handleInput(self, state, usrin):

		if usrin >= '0' and usrin <= '9':
			val = int(usrin)
			if val == 0:
				if len(state.items) - self.page*8 > 8:
					self.page += 1
			elif val == 9:
				# Note(Jesse): If we and self.page > 0 with above it'll make it so you can buy the first item on the next page
				if self.page > 0:
					self.page -= 1
			elif (val - 1 + self.page*8) < len(state.items):
				arr_index = val - 1 + self.page*8
				if state.user.inv[arr_index] == 1 and not state.items[arr_index].stackable:
					self.message = ("You may only have one " + str(state.items[arr_index].name))
				else:
					item = state.items[arr_index]
					if state.user.money < item.cost:
						self.message = "insufficient Money for " + item.name
					else:
						state.user.inv[arr_index] += 1
						state.user.money -= item.cost
						self.message = "bought one " + item.name

		else:
			self.message = "Invalid input"

	def onStop(self, state):
		_clear()
		return

###########################################################################
#                              Menu Screen
###########################################################################
#Updated by Timothy Hall 3/8/20
#todo(Sam): This is the implementation for the menu and config screens
class menu(screen):
	def __init__(self):
		return
	def onStart(self, state):
		for i in range(100):
				print("\n")
		return

	def draw(self, state):
		print("\n\nFrupal\n\t")
		print("a Team B creation\n\n")
		print("PLAY - p\n")
		print("CONFIGURE - c\n")
		print("HELP - o\n")
		print("QUIT - q\n")
		return

	def update(self, state):
		return

	def handleInput(self,state, usrin):
		if(usrin == 'p'):
			self.pushScreen(state, playScreen())
		elif(usrin == 'c'):
			self.pushScreen(state, config())
		elif(usrin == 'P'):
			self.pushScreen(state, playScreen())
		elif(usrin == 'C'):
			self.pushScreen(state, config())
		# Note(Yichao): Operational guidelines
		elif (usrin == 'o'):
			for i in range(30):
				print(" ")
			print("wsad: move")
			print("e: energy bar")
			print("p: shopping")
			print("v: victory bottom")
			print(" ")
			print("Press any key to quit...")
			quit = input()
		# Note Yichao(end)
		# Reset: remove all
		elif (usrin == 'O'):
			for i in range(30):
				print(" ")
			print("wsad: move")
			print("e: energy bar")
			print("p: shopping")
			print("v: victory button")
			print(" ")
			print("Press any key to quit...")
			quit = input()
		else:
			print("Invalid input!\n")
		return

	def onStop(self, state):
		return

###########################################################################
#                            Config Screen
###########################################################################
#Updated by Timothy Hall 3/8/20
class config(screen):
	def __init__(self):
		return

	def onStart(self, state):
		return

	def draw(self, state):
		#display all available items and obstacles
		print("Current items and costs:\n")
		item_len= len(state.items)
		obst_len= len(state.tiles.obstacles)
		max_len= max(item_len,obst_len)

		for i in range(max_len):
				#These 3 cases handle if there are not the same amount of items and obstacles
				if(i < obst_len and i < item_len):
						print("      Item " + str(i) + "\t\tObstacle " + str(i))
						print("Name: " + state.items[i].name + "\t" + state.tiles.obstacles[i].name)
						print("Cost: " + str(state.items[i].cost) + "\t\t" + str(state.tiles.obstacles[i].energy))
						print("Connection: Obstacle " + str(state.items[i].obst))
				elif(i < obst_len):
						print("\t\t\t\tObstacle " + str(i))
						print("Name: \t\t" + state.tiles.obstacles[i].name)
						print("Cost: \t\t\t" + str(state.tiles.obstacles[i].energy))
				else:
						print("Item " + str(i))
						print("Name: " + state.items[i].name)
						print("Cost: " + str(state.items[i].cost))
						print("Connection: Obstacle " + str(state.items[i].obst))
				print("\n")
		#available options for the user
		print("\n\nOptions: ")
		print("Add - a")
		print("Connect- c (can be used to make a tool usable on an obstacle!)")
		print("Quit - q")
		return

	def update(self, state):
		return

	def handleInput(self,state, usrin):
		_clear()
		#userhas decided to add a new item or obstacle
		if (usrin == 'a'):
				print("Would you like to add an obstacle or an item?")
				print("Item - i")
				print("Obstacle - o")
				selection= str(input())[0]

				if(selection == 'i'):
						print("Enter a name for your new item")
						name= input()

						print("Enter a cost for your new item")
						cost= input()
						while(not cost.isnumeric()):
							print("Invalid input. Please enter an integer for your cost.")
							cost= input()
						cost = int(cost)

						print("Is this item stackable? [y/n]")
						e= str(input())
						if e == 'y' or e == 'Y':
							e= True
						else:
							e= False
						add_item(state, name, cost, 0, len(state.items), e)
				elif(selection == 'o'):
						print("Enter a name for your object")
						name= input()

						print("Enter a symbol for your object")
						symbol= input()[0]
						#s= str(input())[0]

						print("Enter an energy cost for stepping on this object")
						cost= input()
						while(not cost.isnumeric()):
							print("Invalid Input. Enter an integer for your cost.")
							cost= input()
						cost = int(cost)
						state.tiles.add_obstacle(name,symbol,cost)
		#user has decided to connect an item and an obstacle
		elif (usrin == 'c'):
				#display all items and obstacles
				item_len= len(state.items)
				obst_len= len(state.tiles.obstacles)
				max_len= max(item_len,obst_len)

				for i in range(max_len):
						if(i < obst_len and i < item_len):
								print("      Item " + str(i) + "\t\tObstacle " + str(i))
								print("Name: " + state.items[i].name + "\t" + state.tiles.obstacles[i].name)
								print("Cost: " + str(state.items[i].cost) + "\t\t" + str(state.tiles.obstacles[i].energy))
								print("Connection: Obstacle " + str(state.items[i].obst))
						elif(i < obst_len):
								print("\t\t\t\tObstacle " + str(i))
								print("Name: \t\t" + state.tiles.obstacles[i].name)
								print("Cost: \t\t\t" + str(state.tiles.obstacles[i].energy))
						else:
								print("      Item " + str(i))
								print("Name: " + state.items[i].name)
								print("Cost: " + str(state.items[i].cost))
								print("Connection: Obstacle " + str(state.items[i].obst))
						print("\n")

				#poll for which objects and items you would like to connect
				print("Enter the number for which item you would like to connect")
				item= input()
				while(True):
					if not item.isnumeric():
						print("Invalid Input. Please enter an integer for your item.")
					elif item.isnumeric() and (int(item) < 0 or int(item) > item_len-1):
						print("Input out of bounds. Please enter a valid obst number")
					else:
						break
					item= input()
				item = int(item)

				print("Which obstacle will it be connected to?")
				obst= input()
				while(True):
					if not obst.isnumeric():
						print("Invalid Input. Please enter an integer for your item.")
					elif obst.isnumeric() and (int(obst) < 0 or int(obst) > obst_len-1):
						print("Input out of bounds. Please enter a valid obst number")
					else:
						obst = int(obst)
						break
					obst= input()
				obst = int(obst)
				state.items[item].obst= obst
		else:
				print("Invalid input")

		return


	def onStop(self, state):
		saveConfig(state)

###########################################################################
#                                Play Screen 
###########################################################################
#Updated by Timothy Hall 3/8/20
class playScreen(screen):

	def __init__(self):
		self.message = ""

	def onStart(self, state):
		# Todo(Jesse): Change the width and height to whatever the config says
		dim = 25
		state.map = Map(state.tiles, dim + 10, dim)

		# Note(Jesse): Adding entities to the world...
		#              greedy tiles
		for y in range(state.map.height):
			for x in range(state.map.width):
				entropy = random.random()
				# print("entropy is:" + str(entropy) + "at: " + str(x) + "," + str(y))
				if entropy == 0.0:
					continue
				entity_id = 0
				for entity in state.entity_manifest:
					if entropy <= entity.chance:
						entity_id = entity.id
						break
					else:
						entropy -= entity.chance
				if entity_id > 0:
					print("[DEBUG]: creating greedy tile entity at:" + str(x + 1) + "," + str(y + 1))
					entity = copy.deepcopy(state.entity_manifest[entity_id - 1])
					entity.x = x
					entity.y = y
					state.entities.append(entity)

		# Todo/Research(Jesse): Do we want to throw out multiple?
		entity = copy.deepcopy(state.entity_manifest[0]) # Note(Jesse): Magic Jewel
		entity.x = random.randint(0, state.map.width - 1);
		entity.y = random.randint(0, state.map.height - 1);
		remove_entity_at(state.entities, entity.x, entity.y)
		print("[DEBUG]: spawning magic jewels at " + str(entity.x + 1) + " " + str(entity.y + 1))
		state.entities.append(entity)

		# Note(Jesse): Camera init
		state.camera.x = state.camera.y = 0
		state.camera.viewport = min(dim, 17)

		state.user = user()

		# Note(Yichao): Allow user to change initial money and energy
		diyEnergy = 20
		diyMoney = 100

		for i in range(30):
			print()
		print("Do you want to modify the initial energy (press Y/y or N/n)?")
		choice = input()
		while choice != 'Y' and choice != 'y' and choice != 'N' and choice != 'n':
			for i in range(30):
				print()
			print("Invalid input, please re-enter")
			choice = input()

		if choice == 'Y' or choice == 'y':
			for i in range(50):
				print()
			print("Enter a number for initial energy, enter an integer")
			diyEnergy = input()
			try:
				diyEnergy = int(diyEnergy)
			except ValueError:
				for i in range(30):
					print()
				print("Input was not an integer")
				print("Please restart the program")
				exit()

		while diyEnergy <= 0:
			for i in range(50):
				print()
			print("Show me the meaning of negative energy?")
			print("Enter a number for initial energy, enter an integer")
			diyEnergy = input()
			try:
				diyEnergy = int(diyEnergy)
			except ValueError:
				for i in range(30):
					print()
				print("Input was not a integer")
				print("Please restart the program")
				exit()

		for i in range(30):
			print()

		print("Do you want to modify the initial money (press Y/y or N/n)?")
		choice = input()
		while choice != 'Y' and choice != 'y' and choice != 'N' and choice != 'n':
			for i in range(30):
				print()
			print("Invalid input, please re-enter")
			choice = input()

		if choice == 'Y' or choice == 'y':
			for i in range(30):
				print()
			print("Enter a number for initial money, enter an integer")
			diyMoney= input()
			try:
				diyMoney = int(diyMoney)
			except ValueError:
				for i in range(30):
					print()
				print("Input was not a integer")
				print("I don't think you can play the game because you can make such a stupid mistake")
				print("The game is over!")
				exit()

		while diyMoney<= 0:
			for i in range(30):
				print()
			print("Are you in debt? We don't accept people in debt in this game")
			print("Enter a number for initial money, enter an integer")
			diyMoney = input()
			try:
				diyMoney = int(diyMoney)
			except ValueError:
				for i in range(30):
					print()
				print("Input was not a integer")
				print("I don't think you can play the game because you can make such a stupid mistake")
				print("The game is over!")
				exit()

		state.user.energy = diyEnergy
		state.user.money = diyMoney

		for i in range(30):
			print()
		# Note Yichao(End)
		# Reset: remove all

		print("Starting this thing up!")

	def draw(self, state):
		# Note Yichao: seperate into two group to print, useful for print color
		s = ""
		t = ""
		t += "Player:\n"
		t += "    Energy:   " + str(state.user.energy) + '\n'
		t += "    Currency: " + str(state.user.money) + '\n'
		t += " Pos:\n"
		t += "   X: " + str(state.user.x + 1) + '\n'
		t += "   Y: " + str(state.user.y + 1) + '\n'
		# Note Yichao(End)
		# Reset:
		# s = ""
		# s += "Player:\n"
		# s += "    Energy:   " + str(state.user.energy) + '\n'
		# s += "    Currency: " + str(state.user.money) + '\n'
		# s += " Pos:\n"
		# s += "   X: " + str(state.user.x + 1) + '\n'
		# s += "   Y: " + str(state.user.y + 1) + '\n'

		tiles = state.tiles
		map = state.map
		camera = state.camera

		#draw a map border
		s += "┌"
		for i in range(camera.viewport):
			s += "──"
		s += "─┐\n"
		# Note(Jesse): To make bottom left 1,1 and top right to be x, x... I'm just drawing the map inverted, and just displaying to the user that
		#              their coords are just +1 of what they actually are (see above where we print player information)
		for j in range(camera.viewport - 1, -1, -1):
			s += "│ "
			for k in range(camera.viewport):
				x = k + camera.x
				y = j + camera.y
				if y == state.user.y and x == state.user.x:
					s += '■'
				elif not map.is_visible(x, y):
					s += ' '
				elif map.has_obstacle(x, y) > 0:
					# Note(Jesse): Obstacle is there
					s += tiles.obstacles[map.get_obstacle(x, y)].ascii
				else:
					s += tiles.terrain[map.get_terrain(x, y)].ascii
				s += ' '
			s += "│\n"

		s += '└'
		for i in range(camera.viewport):
			s += "──"
		s += '─┘'
		# Note(Yichao): print information
		print(t)
		# Note(Yichao)(End)
		# Reset: remove all above

		# Note(Yichao): Colorful print
		# IMPORTANT: only availbale for command line
		# To invoke this, change the line: usrin = get_char() to usrin = input() in handleInput(self, state): in screen.py
		print(end=' ')
		for i in s:
			if i == '.':
				print("\033[0;32;40m. \033[0m", end='')
			elif i == '_':
				print("\033[0;33;40m_ \033[0m", end='')
			elif i == 'f':
				print("\033[0;36;40mf \033[0m", end='')
			elif i == '~':
				print("\033[0;34;40m~ \033[0m", end='')
			elif i == '#':
				print("\033[0;35;40m# \033[0m", end='')
			elif i == 'T':
				print("\033[0;31;40mT \033[0m", end='')
			elif i == '*':
				print("\033[0;37;40m* \033[0m", end='')
			else:
				print(i, end=' ')
		print()

		print("\033[0;32;40m. \033[0m" + " grass " +
			  "\033[0;33;40m_ \033[0m" + " bog " +
			  "\033[0;36;40mf \033[0m" + " forest " +
			  "\033[0;34;40m~ \033[0m" + " water " +
			  "\033[0;35;40m# \033[0m" + " bush " +
			  "\033[0;31;40mT \033[0m" + " tree " +
			  "\033[0;37;40m* \033[0m" + " rock " +
			  "■ " + " hero ")
		print()
		# Note(Yichao): Colorful print(End)
		# Reset:
		# print(s)
		print(self.message + "\t[press q to quit]")

	def update(self, state):
		user = state.user
		camera = state.camera
		map = state.map

		user.reveal_surroundings(state.items, state.map)
		if user.x > camera.x + camera.viewport - 4 and camera.x + camera.viewport < map.width:
			state.camera.x += 1
		elif user.x < camera.x + 4 and camera.x > 0:
			state.camera.x -= 1
		elif user.y > camera.y + camera.viewport - 4 and camera.y + camera.viewport < map.height:
			state.camera.y += 1
		elif user.y < camera.y + 4 and camera.y > 0:
			state.camera.y -= 1

	def handleInput(self, state, usrin):
		if usrin == "p":
			self.pushScreen(state, shopScreen())
			return
		else:
			self.message = state.user.action(state.map, state.items, state.tiles, state.entities, usrin)
			return

	def onStop(self, state):
		return


###########################################################################
#                             Screen Manager
###########################################################################
class screenManager:

	#constructor
	def __init__(self):
		self.stack = stack()

	#internal method to stack.peek() at stack. Do not use outside of class.
	def _top(self):
		return self.stack.peek()

	#Wrapper function for stack.push(). calls onStart() for the screen being
	#added to the stack.
	def setScreen(self, state, screen):
		self.stack.push(screen)
		self._top().setScreenManager(self)
		self._top().onStart(state)

	#Wrapper function for stack.pop(). Calls onStop() on screen prior to
	#removing it from the stack.
	def closeScreen(self, state, index=-1):
		if index == -1:
			self._top().onStop(state)
			self.stack.pop()
		else:
			self.stack.remove(index)

	#draws the screen for the screen at the top of the stack.
	def draw(self, state):
		self._top().draw(state)

	#updates top screen in the stack
	def update(self, state):
		self._top().update(state)

	#Default prompt for input. passes user input to the screen
	#at the top of the stack. if user enters 'q' to quit the screen, it
	#is handled here.
	def handleInput(self, state):
		usrin = get_char()
		if usrin == "q":
			_clear()
			self.closeScreen(state)
			return
		elif usrin == "Q":
			_clear()
			self.closeScreen(state)
			return
		self._top().handleInput(state, usrin)
		_clear()
	#Returns true if stack is empty
	#Returns true if stack is empty
	def isEmpty(self):
		return self.stack.isEmpty()
