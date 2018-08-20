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

    def size(self):
        node = self.head
        c = 0
        while node:
            c += 1
            node = node.next
        return c

    def move_forward_a_node(self,info,position):
        node = self.head
        prev = None
        find_node = None
        n    = 0
        while node :
            n += 1
            if node.data == info:
                find_node = node
                break
            prev = node
            node = node.next
        if find_node is None:
            print('node not found \n')
            return 
        if self.size()-(n+position)>=0 :
            while position != 0 :
                position -= 1
                node = node.next

            if find_node == self.head :
                self.head = self.head.next
                tem = node.next
                node.next = find_node
                find_node.next = tem
            else :
                prev.next = find_node.next
                temp = node.next
                node.next = find_node
                find_node.next = temp
        else :
            print('forwarding not possible \n')
        pass

    def reverse(self):
        node = self.head
        copy = List()
        while node:
            copy.create_list(node.data)
            node = node.next
        return copy

    def print_list(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next
            pass
        pass



def main():
    ls = List()
    for z in ['S','A','B','C','E','F']:
        ls.createList(z)
    ls.print_list()
    print('\n')
    x = ls.move_forward_a_node('F',5)
    ls.print_list()




    pass

if __name__ == '__main__':
    main()
