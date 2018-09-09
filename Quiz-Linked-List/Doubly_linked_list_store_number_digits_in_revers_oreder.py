"""
    QUIZE: In Doubly linked list store digits of a number in 
    in reverse order 
"""

''' Class For Node '''
class Node(object):
    data = None
    next = None
    prev = None
    pass

'''List Class '''
class List(object):
    head = None
    tail = None

    ''' Create Doubly linked List '''
    def create_D_list(self, val):
        node = Node()
        node.data = val
        node.next = self.head
        self.head = node 
        if self.head.next == None:
            self.tail = node 
        if self.head.next != None :
            self.head.next.prev = self.head
        pass

    ''' Print function from Head'''
    def print_list_from_head(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

    '''Print from Tail'''        
    def print_list_from_tail(self):
        node = self.tail
        while node :    
            print(node.data)
            node = node.prev
    
    '''Split a number and store its digit in doubly linked '''
    @staticmethod
    def store_digit(val):
        num = val
        lis = List()
        while num != 0:
            digit = num % 10
            lis.create_D_list(digit)
            num = (num-digit)/10
        return lis
    pass

def main():
    print('hello, world')
    x = 5468132
    store_digi = List().store_digit(x)
    store_digi.print_list_from_tail()
    pass

if __name__ == '__main__':
    main()