#Name Timothy hall
#Date 1/16/20
#File screen.py
#Desc base class for menu/game screens

from stack import stack

from tile import Tiles, Terrain, Obstacle

from user import user

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
	def pushScreen(self, screen):
		self.screenman.setScreen(screen)

	#called in screenman when added to the stack. Do Not implement in subclasses
	def setScreenManager(self, screenman):
		self.screenman = screenman


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
		if int(usrin) >= 0 and int(usrin) <= 9:
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
# Note(Jesse): This is just a test map before I get the actual test map
# width:  18
# height: 18
#
test_map = [
	[[3, 1], [3, 1], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [4, 0], [2, 2], [4, 0]],
	[[3, 0], [3, 1], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [2, 0], [2, 0], [2, 0], [2, 2], [2, 2], [4, 0], [4, 0], [4, 0]],
	[[3, 0], [3, 1], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [2, 0], [2, 0], [2, 0], [2, 2], [2, 2], [4, 0], [4, 0], [4, 0]],
	[[3, 0], [3, 1], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [2, 0], [2, 0], [2, 0], [2, 0], [4, 0], [4, 0], [4, 0]],
	[[3, 1], [3, 1], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [2, 0], [2, 0], [2, 0], [2, 2], [2, 0], [2, 0], [2, 0]],
	[[3, 1], [3, 1], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0]],
	[[3, 0], [3, 1], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [2, 0], [2, 0], [2, 0], [1, 0], [1, 3]],
	[[3, 0], [3, 3], [1, 0], [1, 0], [1, 2], [1, 2], [1, 2], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 3]],
	[[3, 0], [3, 3], [1, 0], [1, 0], [1, 2], [1, 3], [1, 2], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 3]],
	[[3, 0], [3, 3], [1, 0], [1, 0], [1, 2], [1, 2], [1, 2], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 3]],
	[[3, 0], [3, 1], [3, 1], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 3]],
	[[3, 0], [3, 1], [3, 0], [3, 1], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [3, 0]],
	[[3, 0], [3, 1], [3, 0], [3, 0], [3, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [3, 0]],
	[[3, 0], [3, 1], [3, 0], [3, 0], [3, 0], [3, 2], [1, 3], [1, 3], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [3, 0], [3, 0], [2, 0]],
	[[3, 0], [1, 0], [1, 0], [1, 2], [3, 0], [3, 2], [3, 2], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [3, 0], [2, 0], [2, 0], [2, 0]],
	[[3, 0], [1, 0], [1, 0], [1, 0], [3, 0], [3, 2], [3, 2], [3, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [3, 0], [2, 0], [2, 0], [2, 0]],
	[[3, 0], [1, 0], [1, 0], [1, 0], [3, 0], [3, 2], [3, 2], [3, 3], [3, 0], [1, 0], [1, 0], [3, 0], [1, 0], [1, 0], [3, 0], [2, 0], [2, 0], [2, 0]],
	[[3, 0], [3, 0], [3, 0], [3, 0], [3, 0], [3, 2], [3, 2], [3, 2], [3, 2], [3, 0], [3, 0], [3, 0], [3, 0], [3, 0], [3, 0], [2, 0], [2, 0], [2, 0]]
]

class tileTestScreen(screen):

	def __init__(self):	
		self.message = ""

	def onStart(self, state):
		print("Starting this thing up!")
	
	def draw(self, state):
		
		s = ""
		
		s += "Player:\n"
		s += "    Energy:   " + str(state.user.energy) + '\n'
		s += "    Currency: " + str(state.user.money) + '\n'
		s += " Pos:\n"
		s += "   X: " + str(state.user.x) + '\n'
		s += "   Y: " + str(state.user.y) + '\n'
		
		tiles = state.tiles
		
		#draw a map border
		s += "┌"
		for i in range(18):
			s += "──"
		s += "─┐\n"
		for j in range(18):
			s += "│ "
			for k in range(18):
				if j == state.user.y and k == state.user.x:
					s += '@'
				elif test_map[j][k][1] > 0:
					# Note(Jesse): Obstacle is there
					s += tiles.obstacles[test_map[j][k][1]].ascii
				else:
					s += tiles.terrain[test_map[j][k][0]].ascii
				s += ' '
			s += "│\n"

		s += '└'
		for i in range(18):
			s += "──"
		s += '─┘'
		print(s)
		print(self.message + "\t[press q to quit]")

	def update(self, state):
		return

	def handleInput(self, state, usrin):
		# Todo(Jesse): Rewrite this once we get map implementation
		if usrin == "w":
			newX = state.user.x
			newY = state.user.y - 1
			tile_id = test_map[newY][newX][0]
			tile = state.tiles.terrain[tile_id]
			if state.user.energy >= tile.energy:
				state.user.move(0, -1, tile.energy)
				self.message = "walked north onto " + tile.name + str(tile_id)
			else:
				self.message = "You do not have enough energy to move north"
		elif usrin == "s":
			newX = state.user.x
			newY = state.user.y + 1
			tile_id = test_map[newY][newX][0]
			tile = state.tiles.terrain[tile_id]
			if state.user.energy >= tile.energy:
				state.user.move(0, 1, tile.energy)
				self.message = "walked south onto " + tile.name + str(tile_id)
			else:
				self.message = "You do not have enough energy to move south"
		elif usrin == "a":
			newX = state.user.x - 1
			newY = state.user.y
			tile_id = test_map[newY][newX][0]
			tile = state.tiles.terrain[tile_id]
			if state.user.energy >= tile.energy:
				state.user.move(-1, 0, tile.energy)
				self.message = "walked east onto " + tile.name + str(tile_id)
			else:
				self.message = "You do not have enough energy to move east"
		elif usrin == "d":
			newX = state.user.x + 1
			newY = state.user.y
			tile_id = test_map[newY][newX][0]
			tile = state.tiles.terrain[tile_id]
			if state.user.energy >= tile.energy:
				state.user.move(1, 0, tile.energy)
				self.message = "walked west onto " + tile.name + str(tile_id)
			else:
				self.message = "You do not have enough energy to move west"
		elif usrin == "e":
			# Note(Jesse): We're assuming 0 is the power bar here
			if state.user.inv[0] > 0:
				state.user.inv[0] -= 1
				state.user.energy += 10
				self.message = "Consumed Power Bar"
			else:
				self.message = "You do not have any Power Bars left"
		elif usrin == "p":
			state.screenManager.setScreen(state, shopScreen())
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
		usrin = input()
		if usrin == "q":
			self.closeScreen(state)
			return
		self._top().handleInput(state, usrin)
		_clear()
	
	#Returns true if stack is empty
	def isEmpty(self):
		return self.stack.isEmpty()
