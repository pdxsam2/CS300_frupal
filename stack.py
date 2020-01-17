#Name Timothy hall
#Date 1/16/20
#File stack.py
#Desc Basic stack implementation

class stack:

	#constructor
	def __init__(self):
		self.items = []
	
	#adds item to top of screen
	def push(self,item):
		self.items.append(item)

	#returns item at top of stack with out removing it
	def peek(self):
		return self.items[len(self.items)-1]

	#removes top item in stack and returns it.
	def pop(self):
		return self.items.pop()

	#returns size of stack
	def size(self):
		return len(self.items)

	#returns true if stack is empty
	def isEmpty(self):
		return self.size() == 0
