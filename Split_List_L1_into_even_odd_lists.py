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

    def print_list(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next
            pass
        pass
    def split(self,lis1,lis2):
        node = self.head
        while node:
            if node.data % 2 == 0:
                lis1.createList(node.data)
            else :
                lis2.createList(node.data)
            node = node.next
        pass

def main():
    print('say hello')

    L1 = List()
    L_even = List()
    L_odd = List()

    for x in [i for i in range(0,30)]:
        L1.createList(x)
    L1.split(L_even, L_odd)
    L1.print_list()
    print('original list\n')
    L_even.print_list()
    print('even List \n')
    L_odd.print_list()
    print('odd list')


    pass

if __name__ == '__main__':
    main()