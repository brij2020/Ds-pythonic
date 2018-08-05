import random


class Node(object):
    
    data = None
    next = None

    def __init__(self,val, link):
        self.data = val 
        self.next = link
    pass


class Linked_list(object):
    head = None

    def create_list(self,val):
        
        node = Node(val,self.head)
        self.head = node 
        pass

    #Minmum value in linked list O(N)    
    def min(self):
        if self.head == None:
            return 
        min = self.head.data
        node = self.head
        while node :
            if min >= node.data:
                min = node.data
            node = node.next

        return min
    
    #Maximum number in linked list O(N)
    def max(self):
        if self.head == None:
            return
        max = self.head.data
        node = self.head
        while node :
            if max <= node.data:
                max = node.data
            node = node.next
        return max
        


def main():

    '''' Test Code Here '''
    num = []
    for i in range(1,10):
        ran = random.randint(10,100)
        num.append(ran)
    
    li = Linked_list()
    print(num)
    for n in num:
        li.create_list(n)

    print('minimum number is ',li.max())
    pass

if __name__ == '__main__':
    main()

                


