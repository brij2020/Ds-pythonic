"""
QUIZE:
        delete only info part of the pointed node in 
        singly linked list
"""

class Node(object):
    data = None
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
        while node :
            print(node.data)
            node = node.next
            pass
        pass
    def del_info(self,node_info):
        node = self.head
        while node :
            if node.data == node_info:
                del node.data 
            node = node.next

        pass

    
def main():
    print('say hello,')
    lis = List()
    for x in ['a','b','c','d','e','f']:
        lis.createList(x)
    lis.print_list()
    lis.del_info('a')
    print('some operation ')
    lis.print_list()


    
if __name__ == '__main__':
    main()