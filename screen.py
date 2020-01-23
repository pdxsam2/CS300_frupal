#Name Timothy hall
#Date 1/16/20
#File screen.py
#Desc base class for menu/game screens

from stack import stack

from tile import Tiles, tiles, Terrain, Obstacle

#Method to clear the screen for screenManager class
def _clear():
	for i in range(100):
		print("\n")

#base class for all screens/menus
class screen:

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

#################################################################
#                IMPLEMENT NEW SCREENS HERE                     #
#################################################################

#A very basic demo class
class testScreen(screen):

	def __init__(self):	
		self.message = ""

	def onStart(self):
		print("Starting this thing up!")
	
	def draw(self):
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

	def update(self):
		return

	def handleInput(self, usrin):
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

	def onStop(self):
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

	def onStart(self):
		print("Starting this thing up!")
	
	def draw(self):
		#draw a map border
		s = "┌"
		for i in range(18):
			s += "──"
		s += "─┐\n"
		for j in range(18):
			s += "│ "
			for k in range(18):
				if test_map[j][k][1] > 0:
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

	def update(self):
		return

	def handleInput(self, usrin):
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

	def onStop(self):
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
	def setScreen(self, screen):
		self.stack.push(screen)
		self._top().onStart()
	
	#Wrapper function for stack.pop(). Calls onStop() on screen prior to 
	#removing it from the stack.
	def closeScreen(self):
		self._top().onStop()
		self.stack.pop()

	#draws the screen for the screen at the top of the stack.
	def draw(self):
		self._top().draw()

	#updates top screen in the stack
	def update(self):
		self._top().update()

	#Default prompt for input. passes user input to the screen 
	#at the top of the stack. if user enters 'q' to quit the screen, it 
	#is handled here.
	def handleInput(self):
		usrin = input()
		if usrin == "q":
			self.closeScreen()
			return
		self._top().handleInput(usrin)
		_clear()
	
	#Returns true if stack is empty
	def isEmpty(self):
		return self.stack.isEmpty()

