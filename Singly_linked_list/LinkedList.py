 
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


    '''' function for adding new node at the end of linked-list '''
    def add_node_at_end(self,el):

        prev_node = None
        node  = self.current_node
        if node == None:
            self.add_node(el)
        else:
            while node:
                prev_node = node
                node = node.next
            new_node = Node()
            new_node.data = el
            prev_node.next = new_node
            new_node.next = None
        pass

    ''' function for adding new node between nodes '''
    def add_node_before(self,bel,el):

        self.err()
        node = self.current_node
        prev_node = None
        while node:
            if node.data == bel:
                break
            prev_node = node
            node = node.next
        new = Node()
        new.data = el
        new.next = node
        prev_node.next = new 
        pass


    ''' function for adding new node after given node '''
    def add_node_after(self, aft, el):

        self.err()
        node = self.current_node
        new  = Node()
        new.data = el
        prev_node = None
        while node:
            if node.data == aft:
                break
            prev_node = node
            node = node.next
            
        if prev_node  == None :
            prev_node = new
            new.next = None
        new.next = node.next
        node.next = new    
        pass 

    ''' Helper function '''
    def err(self):
        if self.size() == 0 :
            print('empty  linked list ')
            return 0
        pass

    ''' Function for remove node from end  '''
    def remove_from_end(self):

        node = self.current_node
        prev_node = None
        while node:
            prev_node = node
            if prev_node.next.next == None:
                break
            node = node.next
        prev_node.next = None
        pass



    ''' Function for remove node from begning '''
    def remove_node_from_begning(self):

        self.err()   
        node = self.current_node
        if node.next == None :
            self.current_node = None
        else:
            self.current_node = node.next
            

    
    
    ''' function for printing linked-list '''    
    def print_list(self):
        node = self.current_node
        while node:
            print(node.data)
            node = node.next
        pass

        
        



                
def main():
        # Test Code Here
        
        print('welcome Python \n')
        li = LinkedList()
        for i in ['Hello','ram','mohan','kisan','ravi','lodu','jai']:
            li.add_node(i)
        li.print_list()
        li.remove_node_from_begning()
        li.add_node_after('lodu','jai')
        print('\ncomment\n')
        li.print_list()

        
if __name__ == '__main__':
    main()
    

        

            

    

