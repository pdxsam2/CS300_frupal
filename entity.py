#Name Jesse Coyle
#Date 2/15/20
#File entity.py
#Desc This will define things on the map that may be interactable, may be drawable

class Entity:
	x = 0
	y = 0
	
	def __init__(self, id, name, chance):
		self.id = id + 1
		self.name = name
		self.chance = chance

def addEntity(state, name, chance):
	assert(chance <= 1.0 and chance >= 0.0)
	state.total_entity_chance += chance
	assert(state.total_entity_chance <= 1)
	entity = Entity(len(state.entity_manifest), name, chance)
	state.entity_manifest.append(entity)

def hasEntityAt(entities, x, y):
	for entity in entities:
		if entity.x == x and entity.y == y:
			return True
	return False

def getEntityAt(entities, x, y):
	for entity in entities:
		if entity.x == x and entity.y == y:
			return entity
	return [] # Todo(Jesse): Uh not sure standard python-esque reporting here if there isn't an entity/ Maybe just a boolean wrapper and have the calling end deal with it
	
# Note(Jesse): If no entity found on tile it doesn't do anything
def removeEntityAt(entities, x, y):
	for index in range(len(entities)):
		entity = entities[index]
		if entity.x == x and entity.y == y:
			del entities[index]
			return

def findFirstEntity(entities, name):
	for entity in entities:
		if entity.name == name:
			return entity

def entityExists(entities, name):
	for entity in entities:
		if entity.name == name:
			return True
	return False