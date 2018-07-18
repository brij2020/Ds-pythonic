
'''


        Singly Linked List 


'''

import sys
# Class For node 


class Node(object):
    
    data = None
    next = None



class List(object):
    
    current_node = None
    
    '''**************** function for add node to empty list*************** O(1) '''
    def add_node(self,val):
        
        node = Node()
        node.data = val
        node.next = self.current_node
        self.current_node = node
        pass 

    ''' *************** function for add after given node *************** O(N) '''
    def add_after_node(self,val,new_val):

        node = self.current_node
        prev   = None
        found = False
        while node :
            prev = node
            if prev.data == val:
                new_node = Node()
                new_node.data = new_val
                new_node.next = prev.next
                prev.next = new_node
                found = True
                break
            node = node.next
        if found == False:
            print('data not found')
        pass

    '''******************* function for insert new node before given node*****************  O(N) '''
    def add_node_before(self,val,new_val):
    
        if self.size() == 0:
            print('list is empty ')
            return 0
        node = self.current_node
        pre  = None
        new_node = Node()
        new_node.data = new_val
        found = False
        while node:
            pre = node
            if pre.data == val:
                new_node.next = pre
                found = True
                self.current_node = new_node
                break

            node = node.next
            if node == None:
                if self.size() == 1 and pre.data == val:
                    new_node.next = pre
                    self.current_node = new_node 
                    found = True
                    break
            elif node.data == val:
                new_node.next = node
                pre.next = new_node
                found = True
                break
        if found == False:
            print('node not found! ')
        pass 

    '''****************function for travers the list***************** O(N) '''    
    def print_list(self):
        if self.size() == 0:
            print('list is empty !')
            return 0
        node = self.current_node

        while node:
            print(node.data)
            node = node.next
        pass

    ''' *************** function for size *********** O(N) '''
    def  size(self):
        node = self.current_node
        c=0
        while node :
            c+=1
            node = node.next
        return c

    '''************* Adding node to the end of list O(N) ********'''
    def add_node_end(self, val):
        node = self.current_node
        pre = None
        new_node = Node()
        new_node.data = val
        while node :
            pre = node
            node = node.next
            if node == None:
                pre.next = new_node
                
        pass

    '''******************* function for addnig node at begning to list ***************O(1)'''
    def add_at_begning(self,val):
        new_node = Node()
        new_node.data = val
        node = self.current_node
        if node == None:
            self.current_node = new_node
            new_node.next  = None
        else:
            new_node.next = node
            self.current_node = new_node
        pass

    ''' *************************function for deletion node from begning O(1) *****************'''
    def remove_from_begning(self):
        if self.size() == 0:
            print('List is empty and operation can\'t perform on empty list' )
            return 0
        node = self.current_node
        if node.next == None:
            self.current_node = None
        else :
            self.current_node = node.next
        
        pass    
    
    '''***************** function for remove a perticular node  O(n)************ '''
    def remove(self, val):

        if(self.size() == 0):
            print('List is empty ')
            return 0
        node = self.current_node
        pre  = None
        found = False
        while node:

            if node.data == val:
                found = True
                if node.next == None:
                    if self.size() == 1:
                        self.current_node = None
                        return 0
                    else:
                        pre.next = None
                        return 0 
                elif self.current_node.data == val:
                    self.current_node = node.next
                    return 0
                else :
                    pre.next = node.next

            pre = node
            node = node.next    
        if found == False:
            print('node not found!')
        pass

    '''************* function for delet node from end O(N) *********'''
    def remove_from_end(self):
        if self.size() == 0:
            print('List is empty :')
            return 0
        node = self.current_node
        pre = None
        while node :
                if node.next == None:
                    if self.size() == 1:
                        self.current_node = None
                    else:
                        pre.next = None    
                pre = node 
                node  = node.next
        pass
    '''************** function for delet node after given node O(N)****** '''
    def remove_after_node(self, val):
        if self.size() == 0:
            print('List is Empty !')
            return 0
        node = self.current_node
        pre  = None
        found = False
        while node:
            pre = node
            node = node.next
            if pre.data == val:
                found = True
                if self.size() == 1:
                    print('single node list !')
                    return 0
                if pre.next == None:
                    print('the given node is last !')
                    return 0
                pre.next = node.next
        if found == False:    
            print('Node not found !')
        pass




    ''' *********** Removing Node before given Node O(N) '''  
    def remove_before(self, node_val):

        if self.size()==1 or self.size() == 0 or self.current_node.data == node_val:
            print('think about it there is node before head node ')
            return 0
        node = self.current_node
        pre = None
        found = False
        i = 0
        while node :
            if i == 0 :
                pre_node  =  None
                i = i+1
            else:
                pre_node  = pre
            pre = node 
            node = node.next
            if self.current_node.next.data == node_val:
                found = True
                self.current_node = self.current_node.next
                return 0
            elif node.data == node_val:
                pre_node.next = node
                found = True
                return  0
        if found == False:
            print('node not found !')
        pass

def main():
    print('Hello Python World')
    li = List()
    for nam in ['mahesh','vikash','ravi','jai','mohan']:
        li.add_node(nam)
    li.remove_before('Sai')
    li.print_list()
if __name__ == '__main__':
    main()

