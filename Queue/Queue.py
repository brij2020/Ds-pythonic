#################################################
#                                               #
#                                               #
#                                               #
#                                               #
#           QUEUE IMPLIMENTATIONS               #
#  (LIFO ADT base data structure Linked List)   #                                #
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
		if self.head == None:
			return 0
		delo = self.head
		self.head = self.head.next
		return  delo

	def peek(self):
		if self.head == None:
			return
		return self.head.data

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

	q.display()
	q.del_()
	q.del_()
	print('\n *********Operation ******** \n')
	q.display()
	q.insert('Javascript')
	q.insert('Java')
	print('\n***********operation********\n')
	q.display()
	print(q.isEmpty())


if __name__ == '__main__':
	main()
