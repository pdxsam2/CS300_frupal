#Name Timothy hall
#Date 1/16/20
#File screen.py
#Desc base class for menu/game screens

from stack import stack

from tile import Tiles, Terrain, Obstacle

from user import user

from map import Map

from item import add_item

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
	def onStop(self):
		print("Stoping")

	#allows screen to add a screen to the stack above it
	def pushScreen(self, state, screen):
		self.screenman.setScreen(state, screen)

	#called in screenman when added to the stack. Do Not implement in subclasses
	def setScreenManager(self, screenman):
		self.screenman = screenman #Mr. Screenman, bring me a screen.


#################################################################
#                IMPLEMENT NEW SCREENS HERE                     #
#################################################################

#A very basic demo class
class testScreen(screen):

	def __init__(self):
		self.message = ""

	def onStart(self, state):
		print("Starting this thing up!")

	def draw(self, state):
		#draw a map border
		s = ""
		for i in range(20):
			s += "* "
		s += "\n"
		for j in range(20):
			s+= "* "
			for k in range(18):
				s+= "  "
			s += "*\n"

		for i in range(20):
			s += "* "
		print(s)
		print(self.message + "\t[press q to quit]")

	def update(self, state):
		return

	def handleInput(self, state, usrin):
		if usrin == "w":
			self.message = "walked north"
		elif usrin == "s":
			self.message = "walked south"
		elif usrin == "a":
			self.message = "walked east"
		elif usrin == "d":
			self.message = "walked west"
		else:
			self.message = "invalid input"

	def onStop(self, state):
		return


class shopScreen(screen):
	page = 0

	def __init__(self):
		self.message = "Welcome to the shop!"

	def onStart(self, state):
		# Todo(Jesse): We'll do some testing of buying stuff here as debug code
		print("")

	def draw(self, state):
		s = ""

		s += "Currency: " + str(state.user.money) + "\n\n"

		for index in range(0, 8):
			arr_index = index + self.page*8
			if len(state.items) <= arr_index:
				s += '\n'
			else:
				item = state.items[arr_index]
				s += '[' + str(index + 1) + "] " + item.name + '(' + str(state.user.inv[arr_index]) + "):\t\t" + str(item.cost) + '\n'

		if self.page > 0:
			s += "[9] Prev Page\n"
		else:
			s += "\n"

		if len(state.items) - self.page*8 > 8:
			s += "[0] Next Page\n"
		else:
			s += '\n'

		s += "[page: " + str(self.page) + ']\n'

		'''
		# Research(Jesse): Do we want to keep the printing of information within the original map dimensions?
		s = "┌"
		for i in range(18):
			s += "──"
		s += "─┐\n"
		for j in range(18):
			s += "│ "
			for k in range(18):
				s += '  '
			s += "│\n"

		s += '└'
		for i in range(18):
			s += "──"
		s += '─┘'
		'''
		print(s)
		print(self.message + "\t[press q to exit shop]")

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
			else:
				# Note(Jesse): -1 to val because arrays are indexed from 0 and our first option is 1...
				val -= 1
				item = state.items[val + self.page*8]
				if state.user.money < item.cost:
					self.message = "insufficient coin for " + item.name
				else:
					state.user.inv[val + self.page*8] += 1
					state.user.money -= item.cost

		else:
			self.message = "invalid input"

	def onStop(self, state):
		_clear()
		return

#
#
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
		print("QUIT - q\n")
		return

	def update(self, state):
		return

	def handleInput(self,state, usrin):
		if(usrin == 'p'):
			self.pushScreen(state, playScreen())
		elif(usrin == 'c'):
			self.pushScreen(state, config())
		else:
			print("Invalid input!\n")
		return

	def onStop(self, state):
		return

class config(screen):
	def __init__(self):
		return

	def onStart(self, state):
		return

	def draw(self, state):
		print("Current items and costs:\n")
		item_len= len(state.items)
		obst_len= len(state.tiles.obstacles)
		max_len= max(item_len,obst_len)

		for i in range(max_len):
				if(i < obst_len and i < item_len):
						print("      Item " + str(i) + "\t\tObstacle " + str(i))
						print("Name: " + state.items[i].name + "\t" + state.tiles.obstacles[i].name)
						print("Cost: " + str(state.items[i].cost) + "\t\t" + str(state.tiles.obstacles[i].energy))
				elif(i < obst_len):
						print("\t\t\t\tObstacle " + str(i))
						print("Name: \t\t" + state.tiles.obstacles[i].name)
						print("Cost: \t\t\t" + str(state.tiles.obstacles[i].energy))
				else:
						print("Item " + str(i))
						print("Name: " + state.items[i].name)
						print("Cost: " + str(state.items[i].cost))
				print("\n")
		print("\n\nOptions: ")
		print("Add - a")
		print("Connect- c (can be used to make a tool usable on an obstacle!)")
		print("Quit - q")
		return

	def update(self, state):
		return

	def handleInput(self,state, usrin):
		_clear()
		if (usrin == 'a'):
				print("Would you like to add an obstacle or an item?")
				print("Item - i")
				print("Obstacle - o")
				selection= str(input())[0]

				if(selection == 'i'):
						print("Enter a name for your new item")
						c= str(input())
						print("Enter a cost for your new item")
						d= str(input())
						add_item(state, c, d)
				elif(selection == 'o'):
						print("Enter a name for your object")
						c= str(input())
						print("Enter a symbol for your object")
						s= str(input())[0]
						print("Enter an energy cost for stepping on this object")
						i= int(input())
						state.tiles.add_obstacle(c,s,i)
		elif (usrin == 'c'):
				item_len= len(state.items)
				obst_len= len(state.tiles.obstacles)
				max_len= max(item_len,obst_len)

				for i in range(max_len):
						if(i < obst_len and i < item_len):
								print("      Item " + str(i) + "\t\tObstacle " + str(i))
								print("Name: " + state.items[i].name + "\t" + state.tiles.obstacles[i].name)
								print("Cost: " + str(state.items[i].cost) + "\t\t" + str(state.tiles.obstacles[i].energy))
								###print("Object connection: "
						elif(i < obst_len):
								print("\t\t\t\tObstacle " + str(i))
								print("Name: \t\t" + state.tiles.obstacles[i].name)
								print("Cost: \t\t\t" + str(state.tiles.obstacles[i].energy))
						else:
								print("Item " + str(i))
								print("Name: " + state.items[i].name)
								print("Cost: " + str(state.items[i].cost))
						print("\n")

				print("Enter the number for which item you would like to connect")
				item= int(input())
				if(item < 0 or item > item_len):
						##user isn't going to see this bc it'll be before the clear!
						print("Invalid input!")
						return
				print("Which obstacle will it be connected to?")
				connectee= int(input())
				if(connectee < 0 or connectee > obst_len):
						print("Invalid input!")
						return
				state.items[item].obst= connectee
		else:
				print("Invalid input")

		return


	def onStop(self, state):
		return

class playScreen(screen):

	def __init__(self):
		self.message = ""

	def onStart(self, state):
		# Todo(Jesse): Change the width and height to whatever the config says
		dim = 25
		state.map = Map(state.tiles, dim, dim)

		state.camera.x = state.camera.y = 0
		state.camera.viewport = min(dim, 17)

		state.user = user()
		print("Starting this thing up!")

	def draw(self, state):
		s = ""

		s += "Player:\n"
		s += "    Energy:   " + str(state.user.energy) + '\n'
		s += "    Currency: " + str(state.user.money) + '\n'
		s += " Pos:\n"
		s += "   X: " + str(state.user.x + 1) + '\n'
		s += "   Y: " + str(state.user.y + 1) + '\n'

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
		print(s)
		print(self.message + "\t[press q to quit]")

	def update(self, state):
		user = state.user
		camera = state.camera
		map = state.map

		user.reveal_surroundings(state.map)
		if user.x > camera.x + camera.viewport - 4 and camera.x + camera.viewport < map.width:
			state.camera.x += 1
		elif user.x < camera.x + 4 and camera.x > 0:
			state.camera.x -= 1
		elif user.y > camera.y + camera.viewport - 4 and camera.y + camera.viewport < map.height:
			state.camera.y += 1
		elif user.y < camera.y + 4 and camera.y > 0:
			state.camera.y -= 1

	def handleInput(self, state, usrin):

		map = state.map

		# Rewrites(Austin)
		if usrin == "w":
			newX = state.user.x
			newY = state.user.y + 1
			if newY > map.height - 1:
				self.message = "You cannot leave the island"
				return
			terrain_id = map.get_terrain(newX, newY)
			obstacle_id = map.get_obstacle(newX, newY)
			# water
			if terrain_id == 4 and state.user.inv[5] < 1:
				self.message = "You cannot cross water without a boat"
				return
			# there's an obstacle
			if map.has_obstacle(newX, newY):
				obstacle_name = state.tiles.obstacles[obstacle_id].name
				# deal with the obstacle
				if state.user.dealWith(map, newX, newY):
					self.message = "You removed the " + obstacle_name
					return
			# movement is now boolean
			if state.user.move_north(state.tiles.terrain[terrain_id], state.tiles.obstacles[obstacle_id]):
				self.message = "walked north onto " + state.tiles.terrain[terrain_id].name + str(terrain_id)
			else:
				self.message = "You do not have enough energy to move north"
		elif usrin == "s":
			newX = state.user.x
			newY = state.user.y - 1
			if newY < 0:
				self.message = "You cannot leave the island"
				return
			terrain_id = map.get_terrain(newX, newY)
			obstacle_id = map.get_obstacle(newX, newY)
			# water
			if terrain_id == 4 and state.user.inv[5] < 1:
				self.message = "You cannot cross water without a boat"
				return
			# there's an obstacle
			if map.has_obstacle(newX, newY):
				obstacle_name = state.tiles.obstacles[obstacle_id].name
				# deal with the obstacle
				if state.user.dealWith(map, newX, newY):
					self.message = "You removed the " + obstacle_name
					return
			if state.user.move_south(state.tiles.terrain[terrain_id], state.tiles.obstacles[obstacle_id]):
				self.message = "walked south onto " + state.tiles.terrain[terrain_id].name + str(terrain_id)
			else:
				self.message = "You do not have enough energy to move south"
		elif usrin == "a":
			newX = state.user.x - 1
			newY = state.user.y
			if newX < 0:
				self.message = "You cannot leave the island"
				return
			terrain_id = map.get_terrain(newX, newY)
			obstacle_id = map.get_obstacle(newX, newY)
			# water
			if terrain_id == 4 and state.user.inv[5] < 1:
				self.message = "You cannot cross water without a boat"
				return
			# there's an obstacle
			if map.has_obstacle(newX, newY):
				obstacle_name = state.tiles.obstacles[obstacle_id].name
				# deal with the obstacle
				if state.user.dealWith(map, newX, newY):
					self.message = "You removed the " + obstacle_name
					return
			if state.user.move_west(state.tiles.terrain[terrain_id], state.tiles.obstacles[obstacle_id]):
				self.message = "walked west onto " + state.tiles.terrain[terrain_id].name + str(terrain_id)
			else:
				self.message = "You do not have enough energy to move west"
		elif usrin == "d":
			newX = state.user.x + 1
			newY = state.user.y
			if newX > map.width - 1:
				self.message = "You cannot leave the island"
				return
			terrain_id = map.get_terrain(newX, newY)
			obstacle_id = map.get_obstacle(newX, newY)
			# water
			if terrain_id == 4 and state.user.inv[5] < 1:
				self.message = "You cannot cross water without a boat"
				return
			# there's an obstacle
			if map.has_obstacle(newX, newY):
				obstacle_name = state.tiles.obstacles[obstacle_id].name
				# deal with the obstacle
				if state.user.dealWith(map, newX, newY):
					self.message = "You removed the " + obstacle_name
					return
			if state.user.move_east(state.tiles.terrain[terrain_id], state.tiles.obstacles[obstacle_id]):
				self.message = "walked east onto " + state.tiles.terrain[terrain_id].name + str(terrain_id)
			else:
				self.message = "You do not have enough energy to move east"
		elif usrin == "e":
			# Note(Jesse): We're assuming 0 is the power bar here
			if state.user.inv[0] > 0:
				state.user.inv[0] -= 1
				state.user.energy += 10
				self.message = "Consumed Power Bar"
			else:
				self.message = "You do not have any Power Bars left"
		elif usrin == "p":
			self.pushScreen(state, shopScreen())
		elif usrin == "v":
			# Note(Jesse): Victory button
			state.map.reveal_map()
			# Note(Jesse): Today I learn that python can hold practically any integer number, that's neat
			state.user.energy = 4294967295
			state.user.money =  4294967295
		else:
			self.message = "invalid input"

	def onStop(self, state):
		return

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
	def closeScreen(self, state):
		self._top().onStop(state)
		self.stack.pop()

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
		self._top().handleInput(state, usrin)
		_clear()

	#Returns true if stack is empty
	def isEmpty(self):
		return self.stack.isEmpty()
