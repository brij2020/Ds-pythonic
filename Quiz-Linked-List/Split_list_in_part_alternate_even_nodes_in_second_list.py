"""
QUIZE :

        Split Linked List in two part alternate nodes (even node )
        go in second list 
"""



''' Node Class for creating node object '''
class Node(object):
    data = None
    next = None
    pass


''' List class for creating List class '''
class List(object):
    head = None

    ''' method for creating list new nodes '''
    def createList(self, val):
        node = Node()
        node.data = val
        node.next = self.head
        self.head = node

    pass

    
    ''' for print list '''
    def print_list(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next
        pass


def main():
    lis = List()
    for name in ['ram', 'shyam', 'jaya', 'shushma']:
        lis.createList(name)
    
    
    
    
    
    
    print('\n namespace')
    print(dir())

    print('hello, world')
    pass


if __name__ == '__main__':
    main()