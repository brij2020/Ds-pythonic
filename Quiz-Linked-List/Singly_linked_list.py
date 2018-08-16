#########################
#
#
#
#   Skelton for list
#
#
#
############################

class Node(object):
    data =  None
    next = None

    pass

class List(object):
    head = None
    tail = None

    def createList(self, val):

        node = Node()
        node.data = val
        node.next = self.head
        self.head = node
        pass

    def size(self):
        node = self.head
        c = 0
        while node:
            c += 1
            node = node.next
        return c

    def reverse(self):
        node = self.head
        copy = List()
        while node:
            copy.create_list(node.data)
            node = node.next
        return copy

    def print_list(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next
            pass
        pass
