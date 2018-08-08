class Node(object):
    data = None
    next = None

    pass 


class List(object):
    head = None
    tail = None

    def createList(self,val):
    
        node = Node()
        node.data = val
        node.next = self.head
        self.head = node
        pass
    
    def copy(self):
        copy = List()
        node = self.head
        while node :        
            copy.createList(node.data)
            node = node.next
        copy.reverseList()    
        return copy
    
    def reverseList(self):
        node = self.head
        temp = None
        while node:
            self.tail = node
            node = node.next
            self.tail.next = temp
            temp = self.tail
            pass
        self.head = self.tail
        pass
    
    def print_list(self):
        node = self.head
        while node :
            print(node.data)
            node = node.next

def main():

    original_li = List()
    copy = List()
    original_li.createList('Ruby')
    original_li.createList('C#')
    original_li.createList('C')
    original_li.createList('Python')
    cop  = original_li.copy()
    original_li.print_list()
    print('\n---seperate ----------\n')
    cop.print_list()
    pass

if __name__ == '__main__':
    main()