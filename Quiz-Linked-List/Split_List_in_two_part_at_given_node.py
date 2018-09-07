"""
    Split Singly Linked List in two part at given node

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
    def createList(self,val):
        node = Node()
        node.data = val
        node.next = self.head
        self.head = node
    pass

    ''' method for split list in two part  '''
    def split_at_node(self,info):
        node = self.head
        newList = List()
        split_node = None
        while node :
            if node.data == info:
                node = node.next
                split_node = node
                break
            node = node.next
        while node :
            newList.createList(node.data)
            node = node.next
        split_node.next = None
        return newList

    ''' for print list '''
    def print_list(self):
        node = self.head 
        while node:
            print(node.data)
            node = node.next
        pass 


def main():
    lis = List()
    for name in ['ram','shyam','jaya','shushma']:
        lis.createList(name)
    newli = lis.split_at_node('jaya')
    newli.print_list()
    print('\n operation')
    lis.print_list()
    print('\n namespace')
    print(dir())
    
    print('hello, world')
    pass

if __name__ == '__main__':
    main()