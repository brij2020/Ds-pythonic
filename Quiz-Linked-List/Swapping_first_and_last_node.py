class Node(object):
    data = None
    next = None
    pass


class List(object):
    head = None

    def createList(self, node_val):

        node = Node()
        node.data = node_val
        node.next = self.head
        self.head = node
        pass


    def swap_element(self):
        head_data = self.head.data
        node = self.head
        while node :
            xnode = node
            node = node .next
            pass
        self.head.data = xnode.data
        xnode.data = head_data
    def swap_node_link(self):
        node = self.head
        prev = None

        while node :
            prev = node
            node = node.next
            if node.next == None:
                break
        xnode = self.head
        self.head = prev.next
        self.head.next = xnode.next
        prev.next = xnode

        pass



    def printList(self):

        node = self.head
        while node:
            print(node.data)
            node = node.next

            pass
        pass


def main():
    # test area
    li = List()
    lang = ['C#','Java']
    for lang in lang:
        li.createList(lang)
    li.printList()
    li.swap_node_link()
    print('\n------------\n')
    print(li.head.data)
    print(li.head.next.data)
    


if __name__ == '__main__':
    main()