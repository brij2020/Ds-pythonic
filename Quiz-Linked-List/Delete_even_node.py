"""
QUIZE : Delete even position node from linked list
"""

class Node(object):
    data = None
    next = None 
    pass
    
class List(object):
    head = None
    def creatList(self,val):
        node = Node()
        node.data = val
        node.next = self.head
        self.head = node 
        pass

    def print_list(self):
        node = self.head
        while node :
            print(node.data)
            node = node.next
        pass

    def del_even_node(self):
        node = self.head
        odd_node = None
        while node :
            odd_node = node
            node = node.next
            if odd_node.next == None:
                return 0
            if odd_node != None:
                odd_node.next = node.next
                node = odd_node.next



    pass

def main():
    print('say hello')
    lis = List()
    for x in ['Ramesh','Suresh','Jai','Komal','Monish']:
        lis.creatList(x)
    lis.print_list()
    print('\n operation ')
    lis.del_even_node()
    lis.print_list()


    pass
if __name__ == '__main__':
    main()