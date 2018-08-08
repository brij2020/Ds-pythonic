#########################################
#
#
#           Creating Function to reverse list 'L'
#           and L shoud remain same 
#




class Node(object):
    data = None
    next = None

    pass


class List(object):
    head = None

    def create_list(self, val):

        node = Node()
        node.data = val
        node.next = self.head
        self.head = node
        pass

    def reverse(self):
        node = self.head
        copy = List()
        while node :
            copy.create_list(node.data)
            node = node.next
        return copy
    def print_list(self):
        node = self.head
        while node :
            print(node.data)
            node = node.next
        pass 

    pass


def main():

    li = List()
    for name in ['C','C#','Javascript','Python','Ruby']:
        li.create_list(name)

    li.print_list()
    copyli = li.reverse()
    print('\n-----------\n')
    copyli.print_list()    


    print('hello, world')



if __name__ == '__main__':
    main()