class Node(object):
    data = None
    next = None

    pass


class List(object):
    head = None
    tail = None

    def createList(self, val):

        node = Node()
        node.data = val
        node.next = self.head
        self.head = node
        pass

    def remove_duplication(self):
        node = self.head
        while node :
            xnode = node 
            x = node.next
            while  x:
                if x.data == node.data:
                    xnode.next = x.next
                xnode = x
                x = x.next
                pass 
            node = node.next
        pass

    def print_list(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next


def main():
    lis = List()
    for x in [1,25,10,2,30,1,25,1,10,1,2,20,12,32]:
        lis.createList(x)
    
    lis.print_list()
    lis.remove_duplication()
    print('\n-----------\n')
    lis.print_list()

    
    pass


if __name__ == '__main__':
    main()