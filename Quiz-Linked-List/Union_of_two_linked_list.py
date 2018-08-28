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

    def size(self):
        node = self.head
        s = 0
        while node:
            s += 1
            node = node.next
        return s

    def remove_duplication(self):
        node = self.head
        while node:
            xnode = node
            x = node.next
            while x:
                if x.data == node.data:
                    xnode.next = x.next
                xnode = x
                x = x.next
                pass
            node = node.next
        pass

    @staticmethod
    def union(lis1,lis2):
        lis3 = List()
        node1 = lis1.head
        node2 = lis2.head
        while node1 :
            lis3.createList(node1.data)
            node1 = node1.next
        while node2 :
            lis3.createList(node2.data)
            node2 = node2.next
        lis3.remove_duplication()
        return lis3


def main():
    print('say Hello ')
    l1 = List()
    l2 = List()
    for x in [1,2,3,4,5,6,7]:
        l1.createList(x)
    for y in [2,12,3,4,5,13,12]:
        l2.createList(y)
    lis3 = List().union(l1,l2)
    lis3.print_list()
    pass

if __name__ == "__main__":
    main()