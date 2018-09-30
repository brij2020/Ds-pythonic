"""
PRIORITY QUEUE
"""

class Node(object):
    next = None
    data = None
    priority = None
    pass

class PeriorityQueue(object):
    head = None
    
    def insert(self, data, priority):
        node = Node()
        node.data = data
        node.priority = priority
        node.next = self.head
        self.head = node

    def delete(self):
        node = self.head
        if node == None:
            return None
        min  = self.findMin()
        pre  = None
        targateNode = None
        counter = 0 
        while node:
            if counter >= 1 :
                pre = targateNode
            targateNode = node
            node = node.next
            counter += 1
            if targateNode.priority == min:     
                break
        if targateNode == self.head :
            self.head = targateNode.next
            return targateNode.data
        else :
            pre.next = targateNode.next
            return targateNode.data     
        
    def findMin(self):
        node = self.head
        min  = self.head.priority
        while node :
            if min > node.priority:
                min = node.priority
            node = node.next
        return min    

    def peek(self):
        if self.head == None:
            return None
        min = self.findMin()
        return min

    pass  

def main():
    preQ = PeriorityQueue()
    preQ.insert("Ruby",5)
    preQ.insert("Pascal",1)
    preQ.insert("Pen",4)
    preQ.insert("Microsoft",3)
    preQ.insert("Adobe",12)
    preQ.insert("Js",10)
    preQ.insert(12,3)
    preQ.insert("Kal",8)
    preQ.insert("123",8)
    preQ.insert(112,1)
    preQ.insert(133,4)
    print(preQ.delete())
    print(preQ.delete())
    print(preQ.delete())
    print(preQ.delete())
    print(preQ.delete())
    print(preQ.delete())
    print(preQ.delete())
    print(preQ.delete())
    print(preQ.delete())
    print(preQ.delete())
    print(preQ.delete())
    print(preQ.delete())
    print(preQ.delete())
    print(preQ.delete())
    print(preQ.delete())
    
    pass
if __name__ == '__main__':
    main()