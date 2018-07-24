###############################################
#                                             #               
#                                             #       
#               Doubly Linked List            #   
#                                             #   
#                                             #           
###############################################


class Node(object):
    next = None
    prev = None
    data = None
    pass

class Doubly_List(object):
    head = None
    tail = None

    ''' function for adding node to empty list '''
    def add_node_empty_list(self, val):
        node = Node()
        node.data = val
        node.next = self.head
        self.head = node
        if self.head.next == None :
            self.tail = self.head
        if self.head.next != None :
            self.head.next.prev = self.head

        pass

    ''' function for adding node at end O(1)'''
    def add_node_at_end(self,node_val):
        if self.list_size() == 0:
            self.add_node_empty_list(node_val)
            return 0
        node = Node()
        node.data      = node_val
        last_node      = self.tail
        last_node.next = node
        node.prev      = last_node
        self.tail      = node
        pass

    ''' function for adding new node at begning O(1)'''
    def add_node_at_begning(self, node_val):
        if self.list_size() == 0 :
            self.add_node_empty_list(node_val)
            return 0

        node       = Node()
        node.data  = node_val
        front      = self.head
        node.next  = front
        front.prev = node
        self.head  = node
        pass
        
        
    ''' function for print_list_from_head O(N)'''
    def print_list_from_head(self):
        node = self.head
        while node :
            print(node.data)
            node = node.next
        pass

    ''' function for print list from tail O(N)'''
    def print_list_from_tail(self):
        node = self.tail
        while node:
            print(node.data)
            node = node.prev
        
        pass

    ''' function for size of DList O(N)'''
    def list_size(self):
        node = self.head
        i = 0 
        while node :
            i+=1
            node = node.next
        return i    
    
     



def main():
    li = Doubly_List()
    li.add_node_at_end('Brijbhan')
    li.add_node_at_end('Jack')
    for name in ['ramesh','jaiya','beef','suman','ravi','soni','saumya']:
        li.add_node_empty_list(name)
    

    li.add_node_at_end('singh')
    li.print_list_from_head()
    print('\n----------second operation ------\n')
    li.print_list_from_tail()
    # print('\n------------check------------\n')
    print(li.list_size())

    
    
    pass







if __name__ == '__main__':
    main()