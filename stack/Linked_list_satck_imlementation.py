
class Node(object):
    data = None
    next = None
    pass 

class Stack(object):

    head  = None

    def push(self, val) :
        node = Node()
        node.data = val
        node.next = self.head
        self.head = node
    

    def pop(self):
        if self.head == None:
            return None
        elif self.head.next == None:
            value = self.head.data
            self.head = None
            return value
        else :
            data = self.head.data
            self.head = self.head.next
            return data


    def size(self):
        node = Node()
        counter = 0 
        while node :
            counter += 1
            node = node.next
        return counter

    def isEmpty(self):
        return True if self.size() == 0 else False  

    def peek(self):
        if self.size() == 0:
            print('List is empty ')
        else :
            return self.head.data

    pass    



def main():

    stk = Stack()
    stk.push('ravi')
    stk.push(12)
    stk.push('Love')
    print(stk.pop())
    print(stk.pop())
    print(stk.pop())
    print(stk.pop())
    print(stk.peek())
    pass

if __name__ == '__main__':
    main()  