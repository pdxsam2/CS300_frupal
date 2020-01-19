#Name Timothy hall
#Date 1/16/20
#File screen.py
#Desc base class for menu/game screens

from stack import stack

# Research(Jesse): Do we just have to stack these things? Can we just import the whole file?
from tile import tiles, tileAscii, isValidObstacle

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
#
test_map_width = 18
test_map = [
	[[3, 5], [3, 5], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 6], [2, 0]],
	[[3, 0], [3, 5], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [2, 0], [2, 0], [2, 0], [2, 6], [2, 6], [2, 0], [2, 0], [2, 0]],
	[[3, 0], [3, 5], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [2, 0], [2, 0], [2, 0], [2, 6], [2, 6], [2, 0], [2, 0], [2, 0]],
	[[3, 0], [3, 5], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0]],
	[[3, 5], [3, 5], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [2, 0], [2, 0], [2, 0], [2, 6], [2, 0], [2, 0], [2, 0]],
	[[3, 5], [3, 5], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0], [2, 0]],
	[[3, 0], [3, 5], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [2, 0], [2, 0], [2, 0], [1, 0], [1, 7]],
	[[3, 0], [3, 7], [1, 0], [1, 0], [1, 6], [1, 6], [1, 6], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 7]],
	[[3, 0], [3, 7], [1, 0], [1, 0], [1, 6], [1, 7], [1, 6], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 7]],
	[[3, 0], [3, 7], [1, 0], [1, 0], [1, 6], [1, 6], [1, 6], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 7]],
	[[3, 0], [3, 5], [3, 5], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 7]],
	[[3, 0], [3, 5], [3, 0], [3, 5], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [3, 0]],
	[[3, 0], [3, 5], [3, 0], [3, 0], [3, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [3, 0]],
	[[3, 0], [3, 5], [3, 0], [3, 0], [3, 0], [3, 6], [1, 7], [1, 7], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [3, 0], [3, 0], [2, 0]],
	[[3, 0], [1, 0], [1, 0], [1, 6], [3, 0], [3, 6], [3, 6], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [3, 0], [2, 0], [2, 0], [2, 0]],
	[[3, 0], [1, 0], [1, 0], [1, 0], [3, 0], [3, 6], [3, 6], [3, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [3, 0], [2, 0], [2, 0], [2, 0]],
	[[3, 0], [1, 0], [1, 0], [1, 0], [3, 0], [3, 6], [3, 6], [3, 7], [3, 0], [1, 0], [1, 0], [3, 0], [1, 0], [1, 0], [3, 0], [2, 0], [2, 0], [2, 0]],
	[[3, 0], [3, 0], [3, 0], [3, 0], [3, 0], [3, 6], [3, 6], [3, 6], [3, 6], [3, 0], [3, 0], [3, 0], [3, 0], [3, 0], [3, 0], [2, 0], [2, 0], [2, 0]]
]

class enumTestScreen(screen):

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
				# s += "  "
				# Note(Jesse): You can have test_map be the type id of the tile of the map, run it through a map (the key value pair structure) to get it's
				#              printable ascii glyph. If you'd like to make the test_map an array of structures that contain an ascii character and a number id for
				#              the tile type that may be preferable to you.
				#              We planned on having a 3D array, with the 3rd dimension being 2 Z slices, the first slice is the terrain, and the second slice are obstacles
				#              I suggest once the test map is in, we check to see if there are obstacles on this x, y coord, if so output it's ascii glyph, if not then 
				#              print the terrain one... Or maybe make the differing terrain change the color of the printed ascii, while the obstacle provides the ascii glyph itself?
				#              for now this is very much test code
				if isValidObstacle(test_map[j][k][1]):
					s += tileAscii[test_map[j][k][1]] + ' '
				else:
					s += tileAscii[test_map[j][k][0]] + ' '
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

