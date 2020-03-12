#Name Timothy hall
#Date 1/16/20
#File config.py
#Loads and saves configuration settings and data

#TODO serialize the gamemap size

from item import add_item
from tile import Tiles


def loadConfig(state):
	file = open("config.txt", 'r')
	contents = file.readlines()
	#contents[0] will be terrain
	#contents[1] will be obsticals
	#contents[2] will be items
	#contents[3] will be game settings and such
	#Load terrain
	terrain = contents[0].split(";")
	for t in terrain:
		data = t.split(",")
		#print("Data: " + data[0] + " " + data[1] + " " + data[2])
		state.tiles.add_terrain(data[0], data[1], int(data[2]))
	#load obsticals
	obsticles = contents[1].split(";")
	for o in obsticles:
		data = o.split(",")
		#print("Data: " + data[0] + " " + data[1] + " " + data[2])
		state.tiles.add_obstacle(data[0], data[1], int(data[2]))
	#load items
	items = contents[2].split(";")
	inv_slot = 0	#Note(Austin): I added a field in item to help me find the respective array index for user.inv[]
	for i in items:
		data = i.split(",")
		# Debug: print("Data: " + data[0] + " " + data[1] + " " + data[2] + " " + data[3])
		add_item(state, data[0], int(data[1]), int(data[2]), inv_slot, True if data[3] == "1" else False)
		inv_slot += 1
	
	#load settings
	data = contents[3].split(",")
	state.x_dim = int(data[0])
	state.y_dim = int(data[1])
	state.config_energy = int(data[2])
	state.config_money = int(data[3])
	state.intro_flag = int(data[4])

	file.close()


def saveConfig(state):
	file = open("config.txt","w+")
	line=""
	#write tile data
	for t in state.tiles.terrain:
		line += t.name + "," + t.ascii + "," + str(t.energy) + ";"
	line = line[:-1]	#removes last ';' to prevent parsing errors
	file.write(line + '\n')
	#write obstical data
	line = ""
	for o in state.tiles.obstacles:
		line += o.name + "," + o.ascii + "," + str(o.energy) + ";"
	line = line[:-1]
	file.write(line + "\n")
	#write item data
	line = ""
	for i in state.items:
		line += i.name + "," + str(i.cost) + "," + str(i.obst) + "," + str(1 if i.stackable else 0) + ";"
	line = line[:-1]
	file.write(line + "\n")
	#write settings
	line = ""
	line += str(state.x_dim) + "," + str(state.y_dim) + ","
	line += str(state.config_energy) + "," + str(state.config_money) + ","
	line += str(state.intro_flag)
	file.write(line);

	file.close()