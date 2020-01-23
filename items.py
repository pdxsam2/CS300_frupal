# Name Jesse Coyle
# Date 1/22/20
# File items.py
# Desc Items stuff

class Item:
	name = ""
	cost = 0
	id = 0 # Note(Jesse): Not sure if we'll need the id for item here but I'll add it

class Items:
	arr = []

	def add_item(self, name, cost):
		item = Item()
		item.name = name
		item.cost = cost
		item.id = len(arr)
		arr.append(item)
