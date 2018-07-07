 
'''


###########################################################
#                                                         #
#                                                         #
#                    Singly-Linked-List                   #
#                                                         #
###########################################################


'''

'''
    Creating a node class for making a node
'''

class Node(object):

        def __init__(self):

            self.data = None
            self.next = None

        pass

'''
    Creating a Linked List class for all function of linked list implemented

'''

class LinkedList(object):

    def __init__(self):
        self.current_node = None

    ''' Function for adding new node to the list '''
    def add_node(self,data):

        node = Node()
        node.data = data
        node.next = self.current_node
        self.current_node = node
        pass

    
    ''' function for finding size of linked list'''
    def size(self):

        size    = 0
        node    = self.current_node
        while node :
            size+=1
            node = node.next
        return size
        pass

    
    ''' function for finding data from linked list '''    
    def find_data(self, el):

        node = self.current_node

        while node :
            
            if node.data == el:
                return el+' is found \n'
            
                
            node = node.next
        return el+' is not found \n'
        pass
    
    
    ''' function for printing linked-list'''    
    def print_list(self):
        node = self.current_node
        while node:
            print(node.data)
            node = node.next
        pass
    












                
def main():
    
        print('welcome Python \n')
        li = LinkedList()
        for i in ['ramesh','suresh','mahesh','bangali','gopi','sukhi','sabina']:
            li.add_node(i)    

        print(li.find_data('Mahesh'))
        


if __name__ == '__main__':
        main()
    

        

            

    

