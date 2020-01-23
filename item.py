# Name Jesse Coyle
# Date 1/22/20
# File items.py
# Desc Items stuff

class Item:
	name = ""
	cost = 0

def add_item(name, cost):
	item = Item()
	item.name = name
	item.cost = cost
	return item
