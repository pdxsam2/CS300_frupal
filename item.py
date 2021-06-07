# Name Jesse Coyle
# Date 1/22/20
# File items.py
# Desc Items stuff

class Item:
	name = ""
	cost = 0
	obst = 0		##Note(Sam): this is the index of the obstacle for which this item will be attached to (if it is a tool). See "dealWith" in user.py to see how it is used
	#stat = 0		#this will be the difference between the reduced cost that the tool can do
	slot = 0		#Note(Austin): this is the index of the user inventory array in user.py to find it later
	stackable = False 	#More than one of this object can be owned in the inventory

def makeItem(name, cost, connection, order, stackable=False):
	item = Item()
	item.name = name
	item.cost = cost
	item.obst= connection
	item.slot = order
	item.stackable = stackable
	return item

# Note(Jesse): Just a helper function to add the item items array and add an integer to the user's inventory array
def addItem(state, name, cost, connection, order, stackable):
	item = make_item(name, cost, connection, order, stackable)
	state.items.append(item)
	state.user.inv.append(0)

# Note(Sam): preliminary attempt to figure out how to connect obstacles and objects
def connectItem(state, item, obstacle):
	state.items[item].obst= obstacle

def getSlot(items, item_name):
	for item in items:
		if item.name == item_name:
			return item.slot
	return -1