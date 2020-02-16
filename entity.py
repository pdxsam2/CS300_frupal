#Name Jesse Coyle
#Date 2/15/20
#File entity.py
#Desc This will define things on the map that may be interactable, may be drawable

class Entity:
	def __init__(self, id, name):
		self.id = id + 1
		self.name = name

def add_entity(state, name):
	entity = Entity(len(state.entities), name)
	state.entities.append(entity)