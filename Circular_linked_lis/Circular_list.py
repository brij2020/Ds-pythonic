
#####################################################################
#                                                                   #
#                                                                   #
#                                                                   #
#                                                                   #
#                                                                   #    
#               Circular Lineked List                               #
#                                                                   #    
#                                                                   #            
#                                                                   #
#                                                                   #        
#####################################################################

class Node(object):
    data = None
    next = None
    pass

class Circular_linked_list(object):
    
    head    = None
    tail    = None
    check   = 0
    """CREATE CIRCULAR LIST"""
    def create_circular_list(self, val):
        node = Node()
        node.data = val
        node.next = self.head
        self.head = node
        if self.check == 0:
            self.tail = node
            self.check += 1 
        self.tail.next = self.head
        pass

    """PRINT FUNCTION """    
    def print_list(self):
        node = self.head
        while node :
            print(node.data)
            node = node.next
            if node == self.tail:
                print('---------one circle -----\n')
        pass

  

def main():
    print('hello, world')

    cll = Circular_linked_list()
    cll.create_circular_list('C#')
    cll.create_circular_list("Java")
    cll.create_circular_list('Python')
    cll.create_circular_list('Nano')
    cll.create_circular_list('JavaScript')
    cll.print_list()

if __name__ == '__main__':
    main()
