from collections import deque

"""
Queue of game actions to be executed
Stores button presses and calls the corresponding function
Synchronized to timer
ActionQueue consists of:
	MAX_SIZE = 10
	Queue that holds lists of 3 stackable actions
ActionQueue is allowed to do:
	get_size: Returns current size of queue
	has_space: Checks if more actions can be enqueued
	enqueue_move: Add a move to the queue; creates an ActionStack to store that move
	dequeue_move: Resolve a move, removing it from the stack; get rid of stack if it is empty
	stack_move: Add a move to the frontmost ActionStack of the queue
	clear_stack: Remove an ActionStack from the queue
"""
class ActionQueue(object):
	def __init__(self):
		self.queue = deque([])
		self.MAX_SIZE = 10
	
	"""
	Returns current size of queue
	"""
	def get_size(self):
		return len(self.queue)
	
	"""
	Checks if there is still space left in the queue
	"""
	def has_space(self):
		return ( len(self.queue) < self.MAX_SIZE )

	"""
	Add a move to the queue
	Creates an ActionStack to store that move

	Fails if the queue is full
	"""
	def enqueue_move(self, action):
		if self.has_space():
			a = ActionStack()
			self.queue.append(a)
			
			return a.push_move(action)
		else:
			return -1
	
	"""
	Resolve a move, removing it from the stack
	Get rid of stack if it is empty

	Fails if the queue is empty
	"""
	def dequeue_move(self):
		if self.get_size() == 0:
			out = self.queue[0].pop_move();
			
			# Clean up
			self.clear_stack()
			
			return out
		else:
			return -1
	
	"""
	Add a move to the frontmost ActionStack of the queue
	
	Fails if the stack is full
	Only considers the frontmost stack
	"""
	def stack_move(self, action):
		return self.queue[0].push_move(action)
	
	"""
	Remove an ActionStack from the queue
	"""
	def clear_stack(self):
		if self.queue[0].get_size() == 0:
			self.queue.popleft()


"""
Stack of game actions to be evaluated
Shift adds actions to stack, but only to the stack in the front of the queue
ActionStack consists of:
	MAX_SIZE = 10
	Stack: List of stacked actions
ActionQueue is allowed to do:
	get_size: Returns current size of stack
	has_space: Check if there is space to add a move
	push_move: Add a move to the stack
	pop_move: Resolve a move, removing it from the stack
"""
class ActionStack(object):
	def __init__(self):
		self.stack = []
		self.MAX_SIZE = 3
	
	
	"""
	Returns current size of stack
	"""
	def get_size(self):
		return len(self.stack)
	
	"""
	Checks if there is still space left in the queue
	"""
	def has_space(self):
		return ( len(self.stack) < self.MAX_SIZE )
	
	"""
	Pushes move onto stack

	Fails if stack is full
	"""
	def push_move(self, action):
		if len(self.stack) < self.MAX_SIZE:
			self.stack.append(action)
			return 0
		else:
			return -1
	
	"""
	Pops move off of stack

	Fails if stack is empty
	"""
	def pop_move(self):
		return self.pop()
