#Name Timothy hall
#Date 1/16/20
#File main.py
#Desc Main entry point for the game

from screen import screenManager, screen, testScreen, enumTestScreen

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
	#screenManager.setScreen(testScreen())
	screenManager.setScreen(enumTestScreen())




if __name__ == "__main__":
	main()
