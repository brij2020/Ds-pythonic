"""
    STACK :
            Stack ADT LIFO(last in first out mechanism )
            1 : Push() 
            2 : Pop()
            3 : Peek()
            4 : IsEmpty()
            Base datastructure is linked List            
"""

class Node(object):
    next = None
    data = None
    pass
class Stack(object):
    head = None
    
    def push(self,data):
        node = Node()
        node.data = data
        node.next = self.head
        self.head = node
        pass
    def pop(self):
        x = self.head
        if x == None:
            return None
        self.head = x.next
        return x.data

    def length_(self):
        node = self.head
        i    = 0
        while node :
            i += 1
            node = node.next
        return i

    def peek(self):
        if self.head == None:
            print('Stack is empty ')
            return 0
        return self.head.data
    def isEmpty(self):
        if self.head == None:
            return True
        else :
            return False

    pass

    def PrintStack(self):
        node = self.head
        while node :
            print(node.data)
            node = node.next
        pass 
         
def main():
    print('hello, world')
    stk1 = Stack()
    stk1.push('Jai')
    stk1.push('Ruby')
    stk1.push('S')
    print(stk1.length_())
    stk1.PrintStack()
    print(stk1.pop())
    print(stk1.isEmpty())
    pass
if __name__ == '__main__':
    main()