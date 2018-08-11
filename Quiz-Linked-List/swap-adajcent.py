#######
#
#   Swapping adjacent element in linked list 
#
######


class Node(object):
    
    data = None
    next = None
    
    pass 


class List(object):
    head = None

    def createList(self, node_val):
        
        node = Node()
        node.data = node_val
        node.next = self.head
        self.head = node 
        pass
    

    def swap_by_swapping_info(self,node,side_node):
        head = self.head

        while head :
            if head.next != None:
                if head.data == node and head.next.data == side_node :
                    temp = head.next.data
                    head.next.data = head.data
                    head.data = temp
            head = head.next
        
            pass        
        
        pass


    def swap_by_swapping_link(self,val,val1):
        
        
        pass


    def printList(self):
        
        node = self.head
        while node:
            print(node.data)
            node =  node.next
            
            pass
        pass

    pass

def main():

    li = List()
    for i in ['Ruby','C#','C++','Java','Pascal','Javascript']:
        li.createList(i)
    li.printList()
    li.swap_by_swapping_info('Pascal','Java')
    
    print('\n------ doing some operation ---\n')
    li.printList()
    pass


if __name__ == '__main__':
    main()