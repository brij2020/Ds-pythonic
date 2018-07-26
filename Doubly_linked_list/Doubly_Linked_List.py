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
    
    
    ''' function for adding node before given node'''
    def add_node_before(self, node_val, val):
        found = False
        if self.list_size() == 0:
            return -1
        if self.head.data == node_val :
            self.add_node_empty_list(val)
            found = True
        else :
            node       =  Node()
            node.data  = val
            targate_node = self.head
            while targate_node :
                if targate_node.data == node_val:
                    found = True
                    pre_targate       = targate_node.prev
                    node.next         = targate_node
                    targate_node.prev = node
                    pre_targate.next  = node
                    node.prev         = pre_targate
                targate_node = targate_node.next
            if found == False:
                print('data not found! ')

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
    li.add_node_empty_list('Python')
    li.add_node_before('Python','Javascript')
    li.add_node_before('Javascript','Typescript')
    li.add_node_before('Typescript','VBscript')
    li.add_node_before('VBscript','Java')
    #li.add_node_before('Python','Javascript')
    li.add_node_before('VBscript','C++')
    li.add_node_before('JaVa','Brijbhan')
    li.print_list_from_head()
    print('\n---------py seperator -------------\n')
    li.print_list_from_tail()

    # li.add_node_at_end('Brijbhan')
    # li.add_node_at_end('Jack')
    # for name in ['ramesh','jaiya','beef','suman','ravi','soni','saumya']:
    #     li.add_node_empty_list(name)

    # li.add_node_at_end('singh')
    # li.print_list_from_head()
    # print('\n----------second operation ------\n')
    # li.print_list_from_tail()
    # # print('\n------------check------------\n')
    # print(li.list_size())

    
    
    pass






if __name__ == '__main__':
    main()



#####################################################
#
# function to be implemented 
#   1-- Insertion 
#       >> insert node to empty list
#       >> insert node to the end
#       >> insert node to begning 
#       >> insert node before given node
#       >> insert node after given node 
#   2-- Print Operation 
#       >> print entire list from head    
#       >> print entire list from tail
#   3-- Size of list
#       >> Find size of list 
#
#
#
#
#
