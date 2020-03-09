# Name Jesse Coyle
# Date 1/22/20
# File items.py
# Desc Items stuff

class Item:
	name = ""
	cost = 0
	obst = 0		##Note(Sam): this is the index of the obstacle for which this item will be attached to (if it is a tool). See "dealWith" in user.py to see how it is used
	#stat = 0		#this will be the difference between the reduced cost that the tool can do
	stackable = False 	#More than one of this object can be owned in the inventory

def make_item(name, cost, connection, stackable=False):
	item = Item()
	item.name = name
	item.cost = cost
	item.obst= connection
	item.stackable = stackable
	return item

# Note(Jesse): Just a helper function to add the item items array and add an integer to the user's inventory array
def add_item(state, name, cost, connection, stackable):
	item = make_item(name, cost, connection, stackable)
	state.items.append(item)
	state.user.inv.append(0)

# Note(Sam): preliminary attempt to figure out how to connect obstacles and objects
def connect_item(state, item, obstacle):
	state.items[item].obst= obstacle


