"""
QUIZE :

        Is given list is pallindrom ?
"""

class Node(object):
    data = None
    next = None
    prev = None  
    pass

class D_List(object):
    head = None
    tail = None                 
    
    def create_D_list(self, val):
        node = Node()
        node.data = val
        node.next = self.head
        self.head = node
        if self.head.next == None:
            self.tail = node
        if self.head.next != None:
            self.head.next.prev = self.head

    def print_list_from_head(self):
        node = self.head 
        while node:
            print(node.data)
            node = node.next
    def print_list_from_tail(self):
        node = self.tail
        while node :
            print(node.data)
            node = node.prev
        pass
    def len_(self):
        node = self.head
        c = 0
        while node:
            c+=1
            node = node.next 
        return c

    def isPallindrom(self):
        x = 0
        co = self.len_() - 1
        tail_node = self.tail
        head_node = self.head
        y = 0
        while tail_node :
            x += (tail_node.data)*pow(10,co)
            co -= 1
            tail_node = tail_node.prev
        co = self.len_() - 1
        while head_node:
            y += (head_node.data)*pow(10,co)
            co -= 1
            head_node = head_node.next
        print(x,y)
        if y == x :
            print('Yes pallindrom')
        else :
            print('not pallindrom number')
    pass

def main():
    print('say hello, world')
    d_lis = D_List()
    d_lis.create_D_list(1)
    d_lis.create_D_list(2)
    d_lis.create_D_list(1)
    d_lis.print_list_from_head()
    print('\n ------------')
    d_lis.print_list_from_tail()
    d_lis.isPallindrom()
    pass

if __name__ == "__main__":
    main()
