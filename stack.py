class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class Stack:
	def __init__(self, head):
		self.head = head

	def push(self, data):
		new = Node(data)
		n = self.head
		new.next = n
		self.head = new 

	# just move the head down, dont need to actually delete the value
	def pop(self):
		n = self.head
		self.head = n.next

	# print the value at the head / aka top of stack
	def seek(self):
		print ("Hi", self.head.data)

	# Check if the stack is empty 
	def empty(self):
		if self.head.data == None:
			return True
		else:
			return False

	def print_stack(self):
		n = self.head
		while n != None:
			print(n.data)
			n = n.next

my_stack = Stack(Node("A"))
my_stack.push("B")
my_stack.push("C")

my_stack.pop()
my_stack.seek() 
print (my_stack.empty ())

my_stack.print_stack()
