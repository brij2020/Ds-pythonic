"""
    QUIZE : 
        In Doubly linked list store digits of a number in 
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
        temp_num = 0
        lis = List()
        counter = 0
        while num != 0:
            digit = num % 10
            temp_num =  int (temp_num + digit*pow(10,counter))
            if num < 999:
                lis.create_D_list(int(num))
                break
            if counter == 3:
                lis.create_D_list(temp_num)
                temp_num = 0
                counter = 0
            counter += 1 
            num = (num-digit)/10
        return lis
    pass

def main():
    print('hello, world')
    x = 5464152458
    store_digi = List().store_digit(x)
    store_digi.print_list_from_tail()
    pass

if __name__ == '__main__':
    main()