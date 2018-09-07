"""
QUIZE :

        Split Linked List in two part alternate nodes (even node )
        go in second list 
"""



''' Node Class for creating node object '''
class Node(object):
    data = None
    next = None
    pass


''' List class for creating List class '''
class List(object):
    head = None

    ''' method for creating list new nodes '''
    def createList(self, val):
        node = Node()
        node.data = val
        node.next = self.head
        self.head = node
    pass

    ''' method for split list at alternate nodes'''
    def split_node_alternate(self):
        node = self.head
        prev = None
        link_node = None
        counter = 0
        even_list = List()
        while node :
            prev = node
            counter += 1
            if counter % 2 == 0:
                link_node.next = prev.next
                even_list.createList(prev.data)
            else :
                link_node = node
            node = node.next
        return even_list


    ''' for print list '''
    def print_list(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next
        pass


def main():
    lis = List()
    for name in [ x for x in range(0,10)]:
        lis.createList(name)
    print('----original list ----\n')
    lis.print_list()

    newl = lis.split_node_alternate()
    print('\n----- even List --- \n')
    newl.print_list()
    print('\n----odd list---- ')
    lis.print_list()
    print('\n-----namespace ------\n')
    print(dir())

    print('hello, world')
    pass


if __name__ == '__main__':
    main()