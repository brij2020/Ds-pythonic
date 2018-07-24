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

    def print_list_from_head(self):
        node = self.head
        while node :
            print(node.data)
            node = node.next
        pass
    
    def print_list_from_tail(self):
        node = self.tail
        while node:
            print(node.data)
            node = node.prev
        
        pass


    def list_size(self):
        node = self.head
        i = 0 
        while node :
            i+=1
            node = node.next
        return i    




def main():
    li = Doubly_List()

    li.add_node_empty_list(12)
    li.add_node_empty_list('Ravi')
    li.add_node_empty_list('Jack')
    for name in ['ramesh','jaiya','beef','suman','ravi','soni','saumya']:
        li.add_node_empty_list(name)
    li.print_list_from_head()
    print('\n----------second operation ------\n')
    li.print_list_from_tail()
    print('\n------------check------------\n')
    print(li.list_size())
    pass



if __name__ == '__main__':
    main()