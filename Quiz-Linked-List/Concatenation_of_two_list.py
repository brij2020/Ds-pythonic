"""
QUIZE :
        Concatenate two list 
"""

class Node(object):
    next = None
    data = None
    pass

class List(object):
    head = None

    def create_list(self, val):
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
        pass
    def len_(self):
        c = 0 
        node = self.head
        while node :
            c += 1
            node = node.next
        return c

    def concatenate(self,lis):
        conn = None
        newLis = List()

        if self.len_() > lis.len_():
            node = lis.head
            tail =  None
            conn = self.head
        else :
            node = self.head
            conn = lis.head
        newLis.head = node
        while node :
            self.tail = node
            node = node.next
        self.tail.next = conn
        return newLis
    pass


def main():
    print('say hello')
    lis1 = List()
    lis12 = List()
    for x in [11,2312,23,2,1,12,3,4,22,21]:
        lis1.create_list(x)
    for y in [x for x in range(20,26)]:
        lis12.create_list(y)
    lis1.print_list()
    print('\n --operation ---')
    lis12.print_list()
    lis3 = lis1.concatenate(lis12)
    print('\nresulted list')
    lis3.print_list()
    pass

if __name__ == '__main__':
    main()
