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
			self.root = None
			self.size = 0

	def appendNode(self, data):
			self.current_Node = BuildNode(data, self.root)
			if self.head == None:
				self.head = self.current_Node
			self.tail = self.current_Node	
			if self.root != None:
				self.root.set_next(self.current_Node)
			self.root = self.current_Node
			self.size += 1	
			return self		

	def printList(self):
			print_node = self.head
			while print_node != None:
				print print_node.data
				print_node = print_node.next_node		

	def printListBack(self):
			print_node = self.tail
			while print_node != None:
				print print_node.data
				print_node = print_node.previous_node				

link = BuildDoublyLinked()

link.appendNode(1)
link.appendNode(2)
link.appendNode(3)

print link.printList()
print link.printListBack()
















					
