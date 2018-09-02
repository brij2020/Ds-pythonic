"""

    Combine two list as alternative node from one list to another 
    and small list at end is empty
    eg
    L1:  1 -> 7 ->3 -> 4
    L2:  13 -> 8
    combined L1: 1 -> 13 -> 7 -> 8 -> 3 -> 4
    L2         : empty

"""

class Node(object):
    data = None
    next = None

    pass


class List(object):
    head = None

    def createList(self, val):

        node = Node()
        node.data = val
        node.next = self.head
        self.head = node
        pass

    def size(self):
        node = self.head
        c = 0
        while node:
            c += 1
            node = node.next
        return c

    def print_list(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next
            pass
        pass

    @staticmethod
    def combine(list1,list2 ):
        if list1.size() > list2.size():
            node_small = list2.head
            node_big   = list1.head
            list2.head = None
        else:
            node_small = list1.head
            node_big   = list2.head
            list1.head = None
        temp_long =  None
        temp_sort = None
        while node_small :
            temp_sort  = node_small
            node_small = node_small.next
            temp_long  = node_big
            node_big   = node_big.next
            temp_long.next = temp_sort
            temp_sort.next = node_big
        
        pass

def main():
    print('say hello')

    l1 = List()
    l2 = List()
    for x in [45,12,10,13]:
        l1.createList(x)
    for y in [1,3]:
        l2.createList(y)
    
    List().combine(l1,l2)
    l1.print_list()
    print('\n')
    l2.print_list()

    pass 

if __name__ == '__main__':
    main()