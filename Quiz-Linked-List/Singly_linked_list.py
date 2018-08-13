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

        
    def print_list(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next
            pass
        pass
