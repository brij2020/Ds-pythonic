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
    def create_list(self, val):
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
            self.create_list(node_val)
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
            self.create_list(node_val)
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
            self.create_list(val)
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
    ''' function for adding node after given node'''
    def add_node_after_given_node(self, node_val, new_node):
        found = False
        if self.list_size() == 0:
            return -1
        if  self.tail.data == node_val:
            node = Node()
            node.data = new_node
            self.head.next = node 
            node.prev = self.tail
            self.tail = node
            found = True
        else :
            
            targate_node = self.head
            while targate_node :
                if targate_node.data == node_val:
                    node = Node()
                    node.data = new_node
                    temp_node = targate_node.next
                    targate_node.next = node
                    node.prev = targate_node
                    temp_node.prev = node
                    node.next  = temp_node
                    found  = True
                    break
                targate_node = targate_node.next
        if found == False:
            print('Node not found !')

        pass


    ''' function for finding node in list '''
    def finde_node(self,node_val):

        node = self.head
        while node :
            if node.data == node_val:
                print('node found ')
                return 0
            node = node.next
        print('node not found in list')    

        pass

    '''' function for removing node from begning '''
    def remove_from_begning(self):
        if self.list_size() == 0:
            print('List is empty ')
            return 0
        if self.list_size() == 1:
            self.head = None
            self.tail = None
            
        else :
            self.head       = self.head.next
            self.head.prev  = None
        pass
    
    
    ''' function for remove node from end '''
    def remove_from_end(self):
        if self.list_size == 0:
            print('list is empty')
            return 0
        if self.list_size() == 1 :
            self.head = None
            self.tail = None
        if self.tail.prev == self.head:
            self.head = self.tail
            self.tail.prev = None
        else :
            self.tail = self.tail.prev
            self.tail.next = None
        pass
    
    ''' Helper function for remove node '''
    def help_remove(self, node):
        if self.list_size() == 0 or self.head.data == node  :
            return -1
        if self.tail.data == node:
            if self.tail.prev == self.head :
                self.tail.prev = None
                self.head = self.tail
                return 1
            else:
                self.tail.prev.prev.next = self.tail
                self.tail.prev = self.tail.prev.prev
                return 1
        else:
            return 0

        pass


    ''' function for removing node before given node '''
    def remove_node_befor_node(self, node):
        if self.help_remove(node) == 1:
            return
        if self.help_remove(node) == -1:
            print('error !')   
        found = False    
        targate_node = self.head.next
        while targate_node :
            if targate_node.data == node :        
                targate_node.prev = targate_node.prev.prev
                targate_node.prev.next = targate_node
                found = True
                break
            if targate_node.next == self.head :
                break
            targate_node = targate_node.next
        
        if found == False:
            print('node not found')
        
        pass

    ''' function for remove node '''
    def remove(self, node_data):
        found = False
        if self.list_size() == 0:
            print('list is empty')
            return
        if self.list_size() == 1 :
            if self.head.data == node_data:
                self.head  = None
                self.tail  = None
                found = True
        elif self.head.data == node_data:
            temp = self.head.next
            temp.pre = None
            self.head = temp
        else:
            node = self.head.next
            while node :
                if node.data == node_data:
                    found = True
                    if node is self.tail:
                        self.tail = self.tail.prev
                        self.tail.next = None
                    else :                        
                        node.next.prev = node.prev
                        node.prev.next = node.next
                node = node.next
            if found == False:
                print('node not found ')
    def remove_after_given_node(self,val):
        
        targate = self.head
        found = False
        if self.list_size() == 0: 
            print('list Empty ')
        while targate:
            if targate.data == val and targate is self.head:
                found = True
                if self.list_size() == 1:
                    print('there is nothing next to this node') 
                if self.head.next is self.tail:
                    self.tail = self.head
                    self.head.next = None
                    
                    break
                else:
                    
                    self.head.next = self.head.next.next
                    self.head.next.prev = self.head
                    
                    break        
            elif targate.data == val:
                found = True
                if targate.next is self.tail:
                    self.tail = targate
                    targate.next = None
                    
                    break
                else:
                    targate.next = targate.next.next
                    targate.next.prev = targate
                    
                    break
            targate = targate.next
        if found == False :
            print('Node not found')    
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
    li.create_list('Python')
    for x in ['C','C++']:
        li.create_list(x)
    li.print_list_from_head()
    li.remove_after_given_node('C++')
    li.remove_after_given_node('C++')
    li.add_node_before('C++','Ruby')
    print(li.list_size())
    print('\n---------------\n')
    li.print_list_from_head()
    pass


if __name__ == '__main__':
    main()



#####################################################
#
# function to be implemented 
#   1-- Insertion 
#       >> create list
#       >> insert node to the end
#       >> insert node to begning 
#       >> insert node before given node
#       >> insert node after given node 
#   2-- Print Operation 
#       >> print entire list from head    
#       >> print entire list from tail
#   3-- Size of list
#       >> Find size of list 
#   4-- Find Node in list 
#   
#   5-- Deletion Node from list
#       >> from begning
#       >> from End
#       >> bfore given node
#       >> after given node 
#       >> remove given node
#   