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
        xprev = None
        pos = 0
        node_found = None
        while node :
            prev = node
            node = node.next
            if self.head.data = info :
                prev = self.head.next
                self.head = prev
            if node.data == info:
                node_found = node
                while node:
                    pos += 1
                    xprev = node
                    node = node.next
                    if node == None:
                        return
                    if pos == position:
                        break


            if pos == position:
                break
        if position == 1:
            prev.next = node_found.next
            ylink = prev.next.next
            prev.next.next = node_found
            node_found.next = ylink

        else:
            prev.next = node_found.next
            zrep = node.next
            node.next = node_found
            node_found.next = zrep

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
    x = ls.move_forward_a_node('F',3)
    print(x)
    ls.print_list()




    pass

if __name__ == '__main__':
    main()
