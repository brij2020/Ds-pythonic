
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
    
    head = None
    tail = None


    def create_circular_list(self, val):
        node = Node()

        node.data = val
        node.next = self.head
        self.head = node
    def print_list(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next
        pass 

    
    pass



def main():
    print('hello, world')

    cll = Circular_linked_list()
    cll.create_circular_list('C#')
    cll.create_circular_list("Java")
    cll.print_list()

if __name__ == '__main__':
    main()
