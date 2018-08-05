class Node(object):

    data = None
    next = None

class Stack(object):
    head = None

    def push(self, val):
        node = Node()
        node.data = val
        node.next = self.head
        self.head = node

        pass
    
    def peek(self): 
        if self.size() == 0:
            return 'list is Empty'
        else :
            return self.head.data

    def size(self):
        node = self.head
        counter = 0
        while node :
            counter+=1
            node = node.next
        return counter
        
    def pop(self):

        if self.size() == 0:
            return 'list is empty' 
        else :
            if self.head.next == None:
                data = self.head.data
                self.head = None
                return data
                
            else :
                data = self.head.data
                self.head = self.head.next
                return data

    def peek(self):

        if self.head == None:
            return 'Stack is empty '
        else :
            data = self.head.data
            return data

    def isEmpty(self):
        return True if self.head == None else False

    pass

            


def main():
    print('hello, world')
    stk = Stack()
    stk.push('Ravi')
    stk.push('Rakesh')
    stk.push('Mohan')
    stk.push('Sashi')
    stk.push('C#')
    print(stk.pop())
    print(stk.pop())

    print(stk.peek())
    print(stk.isEmpty())
if __name__ == '__main__':
    main()