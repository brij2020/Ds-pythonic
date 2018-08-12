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

		methods to applied
		
		1-  insert()
		2-  del()
		3-  peek()
		4-  display()
		5-  isEmpty()

"""


class Node(object):

	data = None
	next = None

	pass


class Queue_(object):

	head = None


	def insert(self, val):

		node = Node()
		node.data = val
		node.next = self.head
		self.head = node
		pass

	def del_(self):
		node = self.head
		prev = None
		while node:

			if node.next == None:
				break
			prev = node
			node = node.next
		prev.next = None
		return node.data
	def peek(self):
		node = self.head
		while node :
			node = node.next
			if node.next == None:
				break
		return node.data

	def display(self):

		node = self.head
		while node:
			print(node.data)
			node = node.next
		pass


	def isEmpty(self):

		if self.head == None:
			return True
		else :
			return False

	pass



def main():
	# test area
	q = Queue_()

	for pro in ['Ruby','C#','Python','Camel','C','Java']:
		q.insert(pro)
	q.del_()
	q.del_()
	q.del_()
	q.del_()
	q.insert('Java7')
	print(q.peek())
if __name__ == '__main__':
	main()
