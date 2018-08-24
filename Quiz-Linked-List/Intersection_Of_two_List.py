######################################################
#       Intersection of Two Lists                    #
######################################################


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
        while node :
            print(node.data)
            node = node.next
        pass

    def size(self):
        node = self.head
        s = 0
        while node:
            s+=1
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
    def intersection(listA,listB):
        #print('hi')
        node1 = listA.head
        result_list = List()
        while node1:
            node2 = listB.head
            while node2:
                if node1.data == node2.data:
                    result_list.createList(node1.data)
                    break
                node2 = node2.next
            node1 = node1.next
        return result_list

def main():
    print('hi py')
    lisA = List()
    lisB = List()
    for x in [21,3,2,12,33,23,112,122]:
        lisA.createList(x)
    for x in [21,2,35,1,12,41,10]:
        lisB.createList(x)
    lisA.remove_duplication()
    lisB.remove_duplication()
    lisA.print_list()
    print('\n')
    lisB.print_list()
    print('\n intersection \n')
    x = List().intersection(lisA, lisB)
    x.print_list()
    pass

if __name__ == '__main__':
    main()
