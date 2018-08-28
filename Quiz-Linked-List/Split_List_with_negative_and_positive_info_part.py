"""
Quiz : from L1 list find negative info part nodes delete nodes
and insert them in L2 using positive info part create list L3 .

"""


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

    def split(self):
        node = self.head
        l2   = List()
        l3   = List()
        positive = None 
        while node:
            if node.data < 0:
                l2.createList(node.data)
                if node == self.head:
                    self.head = node.next
            else :
                i = 0
                if i == 0 :
                    positive = node
                if i == 1:
                    positive.next = node 
                    positive = node 
                i += 1
            node  = node.next
        pass


def main():
    print('say hello')
    lis = List()
    for x in [1,2,-2,0,-4,3]:
        lis.createList(x)
    lis.split()
        
    lis.print_list()
    pass
if __name__ == '__main__':
    main()