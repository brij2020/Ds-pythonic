#################################################
#                                               #
#                                               #
#                                               #
#                                               #
#           QUEUE IMPLIMENTATIONS               #
#  (FIFO ADT base data structure Linked List)   #                                #
#                                               #
#                                               #
#                                               #
#################################################
"""

	1-  insert()
	2-  del()
	3-  peek()
	4-  display()
	5-  isEmpty()

"""


class Node(object):
	next = None
	data = None
	pass

class Queue(object):
	head = None
	tail = None

	def insert(self,data):
		node = Node()
		node.data = data
		node.next = self.head
		self.head = node
		if node.next == None:
			self.tail = node 
		pass
	
	def delete(self):
		if self.tail == None:
			return None
		data = self.tail.data
		node = self.head
		while node:
			if node.next.next == None:
				self.tail = node
				node.next = None
				break
			node = node.next
		return data			
	def qhelp(self):
		node = self.head
		newQ = Queue() 
		while node :
			newQ.insert(node.data)
			node = node.next
		return newQ

	
	def peek(self):
		if self.tail == None:
			return None
		return self.tail.data

	def display(self):
		x = self.qhelp()
		node = x.head
		while node:
			print(node.data)
			node = node.next
		pass

	def isEmpty(self):
		if self.head == None :
			return True
		else:
			return False
		pass

	pass 


def main():
	print('hey! Programming world')
	q1 = Queue()
	q1.insert('Python')
	q1.insert('Js')
	q1.insert('Ruby')
	q1.insert('Java')
	print('\n------------')
	q1.display()
	print(q1.isEmpty())
			
	pass
if __name__ == '__main__':
	main()