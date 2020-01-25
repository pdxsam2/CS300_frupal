# Name Jesse Coyle
# Date 1/22/20
# File items.py
# Desc Items stuff

class Item:
	name = ""
	cost = 0

def make_item(name, cost):
	item = Item()
	item.name = name
	item.cost = cost
	return item

# Note(Jesse): Just a helper function to add the item items array and add an integer to the user's inventory array
def add_item(state, name, cost):
	item = make_item(name, cost)
	state.items.append(item)
	state.user.inv.append(0)
