class BuildNode(object):
	def __init__(self, data, previous_node = None, next_node = None):
			self.data = data
			self.previous_node = previous_node
			self.next_node = next_node

	def set_next(self, next_node):
			self.next_node = next_node			

class BuildDoublyLinked(object):
	def __init__(self):
			self.head = None
			self.tail = None
			self.size = 0

	def appendNode(self, data):
			current_node = BuildNode(data, self.tail)
			if self.head == None:
				self.head = current_node	
			if self.tail != None:
				self.tail.set_next(current_node)
			self.tail = current_node
			self.size += 1	
			return self		

	def printIndexForward(self, index):
			if self.size == 0:
				return "List is empty!"
			elif index + 1 > self.size:
				return "Index does not exist!"	
			elif index == 0:
				return self.head
			elif index + 1 == self.size:
				return self.tail
			else:
				current_node = self.head
				for node_index in range(0, index):
					current_node = current_node.next_node
				return current_node

	def deleteIndexForward(self, index):
			if self.size == 0:
				return "List is empty!"
			elif index + 1 > self.size:
				return "Index does not exist!"
			elif self.size == 1:
				self.head = None
				self.tail = None
				self.size = 0
			elif index + 1 == self.size:
				new_tail = self.tail.previous_node
				new_tail.next_node = None
				self.tail = new_tail
				self.size -= 1
			elif index == 0:
				new_head = self.head.next_node
				new_head.previous_node = None
				self.head = new_head
				self.size -= 1
			else:
				current_node = self.head
				for node_index in range(0, index):
					current_node = current_node.next_node
				previous_node_adjust = current_node.previous_node	
				next_node_adjust = current_node.next_node
				previous_node_adjust.next_node = next_node_adjust
				next_node_adjust.previous_node = previous_node_adjust
				self.size -= 1

	def printListForward(self):
			node_to_print = self.head
			while node_to_print != None:
				print node_to_print.data
				node_to_print = node_to_print.next_node		

	def printListBack(self):
			node_to_print = self.tail
			while node_to_print != None:
				print node_to_print.data
				node_to_print = node_to_print.previous_node				

link = BuildDoublyLinked()

link.appendNode(1)
link.appendNode(2)
link.appendNode(3)
link.appendNode(4)

data = link.printIndexForward(2)
print data.data

link.deleteIndexForward(2)

link.printListForward()















					
