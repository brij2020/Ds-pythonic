"""

    Find out does a list contain cycle or not is ?
    if it has then find out the node from where looping starts.
    Remove the node and make it Null terminated list.

"""

class  Node(object):
    data  = None
    next  = None

    pass

class Group_list(object):
    tail = None
    head = None
    check = 0

    """ create cicrular Linked List """
    def create_cicular_list(self,val):
        node = Node()
        node.data = val
        node.next = self.head
        self.head = node
        if self.check == 0:
            self.tail = node
            self.check += 1
        self.tail.next = self.head
        pass

    """ Singly Linked List """
    def create_null_terminated_list(self,val):
        node = Node()
        node.data = val
        node.next = self.head
        self.head = node
        pass

    """ Print List """
    def print_list(self):
        node = self.head
        ck   = 0
        while node :
            print(node.data)
            if node.next == self.head:
                print('\n-----cycle-----')
                if ck == 1:
                    break
                ck += 1

            node = node.next
        pass


    """ check for list contail loop Or Not """
    def is_list_contain_cycle(self):
        node = self.head
        isCycle = False
        while node :
            if node.next == self.head:
                self.tail.next  = None
                node.next = None
                isCycle = True
                break
            node = node.next
        if isCycle:
            print('contain cyacle at Node ',node.data)
        else :
            print('NUll terminated list')
    pass

def main():
    print('hello, world')
    sll = Group_list() #Singly Linked List
    cll = Group_list() #Cricular Linked List 

    #Circular Linked List
    cll.create_cicular_list('x')
    cll.create_cicular_list('y')
    cll.create_cicular_list('z')
    cll.create_cicular_list('xx')
    cll.create_cicular_list('yy')
  
    #Silgly Linked List
    sll.create_null_terminated_list('B')
    sll.create_null_terminated_list('C')
    sll.create_null_terminated_list('D')
    sll.create_null_terminated_list('E')
    cll.print_list()
    cll.is_list_contain_cycle()
    cll.is_list_contain_cycle()
    sll.is_list_contain_cycle()
    pass

if __name__ == '__main__':
    main()