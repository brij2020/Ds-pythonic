"""
Application Of Stack

"""
import sys
class Node(object):
    node = None 
    data = None
    pass
class Stack(object):
    head = None
    def insert(self,data):
        node = Node()
        node.data = data
        node.next = self.head
        self.head = node 
    def delete(self):
        if self.head == None:
            return None
        data =  self.head.data
        if self.head.next != None:
            self.head = self.head.next
        else :
            self.head = None
        return data
    def printList(self):
        node = self.head
        while node :
            print(node.data)
            node = node.next
    def con(self):
         node = self.head
         x       = ''
         while node:
             x += self.delete()
             node = node.next
         return x
    
    @staticmethod
    def reverseString():
        rev = Stack()
        x = ''
        strg = sys.stdin.readline()
        strg = list(strg)
        for i in strg :
            rev.insert(i)
        rev.printList()
        x =  rev.con()
        return x
        
    pass


def main():
    print(Stack().reverseString())
    
    pass

if __name__ == '__main__':
    main() 
