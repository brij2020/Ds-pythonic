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
            if node.next == None:
                break
            prev = node
            node = node.next
        xnode = self.head
        self.head = node
        self.head.next = xnode.next
        xnode.next = None
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
    lang = ['C#','Java','Python','Javascript','VBScript']
    for lang in lang:
        li.createList(lang)
    li.printList()
    li.swap_node_link()
    print('\n--seprate operation --\n')
    li.printList()
    li.createList('Ruby')
    print('\n--seprate operation --\n')
    li.printList()
    li.swap_node_link()
    print('\n--seprate operation --\n')
    li.printList()

if __name__ == '__main__':
    main()