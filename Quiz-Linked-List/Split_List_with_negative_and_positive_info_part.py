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

    def split(self,positive_list,negative_list):
        node = self.head
        i = 0
        positive = None
        while node:
            if node.data >=0:

                if i == 0:
                    self.head = node
                
                i+=1
                positive = node
                positive_list.createList(node.data)
            elif node == self.head:
                negative_list.createList(node.data)

            else:
                negative_list.createList(node.data)
                if positive != None:
                    positive.next = node.next

            node = node.next

        pass


def main():
    print('say hello')
    lis = List()
    positive_list   = List()
    negative_list   = List()
    for x in [1,2,-2,0,-4,-3]:
        lis.createList(x)
    negative_list   = List()
    lis.split(positive_list, negative_list)
    positive_list.print_list()
    print('\n')
    negative_list.print_list()
    print('\n')
    lis.print_list()
    pass
if __name__ == '__main__':
    main()