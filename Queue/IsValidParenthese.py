"""
Valid Parentheses in Expression

"""
import sys

class Node(object):
    next = None
    data = None
    pass

class Stack(object):
    head = None   
    def insert(self, data):
        node = Node()
        node.data = data
        node.next = self.head
        self.head = node 
    
    def pop(self):
        if self.head == None:
            return None
        else :
            node_value = self.head.data
            if self.head.next == None:
                self.head = None
                return node_value
            else :
                self.head = self.head.next
                return node_value
    
    def printPrentheseStack(self):
        node = self.head 
        while node :
            print(node.data)
            node = node.next
    
    def peek(self):
        if self.head == None:
            return None
        return self.head.data
    
    @staticmethod    
    def help__(symbol,match):
        if symbol == ')' and match == '(':
            return True
        elif symbol == '}' and match == '{':
            return True
        elif symbol == ']' and match == '[':
            return True
        else :
            return False

    @staticmethod
    def match():
        symbolStack    = Stack()
        # readExpression = sys.stdin.readline()
        readExpression = "(12+10)+[{21-(x-12)+}]"
        express        = list(readExpression)
        leftSymbol     = ['[','{','(']
        rightSymbol    = [']','}',')'] 
        parentheseList = list(express)
        for symbol in parentheseList:
            if symbol in leftSymbol:
                symbolStack.insert(symbol)
            elif symbol in rightSymbol:
                match = symbolStack.pop()
                if Stack().help__(symbol,match) != True:
                    print('!invalid prenthese ')
                    return 
        if symbolStack.peek() == None:
            print('Valid prentheses !')
def main():
    print('hello, world')
    Stack().match()
    pass

if __name__ == '__main__':
    main()