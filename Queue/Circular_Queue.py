"""
    CIRCULAR QUEUE:
            :: In queue after front reach to size of 
            array further insertion is not possible yet there
            are spaces available after deletion of queue 
            element.
            And to overcome this problem we think array as circular .
"""

class Queue(object):
    q = []
    front = -1
    rear  = -1
    Max   = 3
    counter = 0
   
    """ insert method to add new entry in Queue """
    def insert(self,data):
        if self.rear >= self.Max-1:
            print('Queue Overflow')
            return None
        else :
            self.rear  += 1
            self.q.append(data)
            self.counter += 1
        if self.counter == 1: 
            self.front 
        pass

    """ Delete method to delete peek element """
    def delete(self):
        if self.front >= self.Max-1:
            self.front = -1
            self.rear  = -1
            self.q = []
            self.counter = 0
            print('q is empty ')
            return None

        elif self.front == -1 :
            print('Queue is empty ')
        else :
            self.q[self.front] = None
            self.front += 1


    """ peek method return very first element from Queue"""
    def peek(self):    
        if  self.rear == -1:
            print('x Array')
        else :
            return self.q[self.front]


    """ Dsiplay method print all queue element"""
    def display(self):
        if self.front == -1 or self.front >= self.Max-1:
            return None
        else :
            print(self.front,self.rear)
            for i in range(self.front,self.rear+1):
                print(self.q[i])
        pass

    """ isFull return Boolean """
    def isFull(self):
        if self.rear >= self.Max -1 :
            return True
        else :
            return False

    """ isEmpty return Boolean value """
    def isEmpty(self):
        if self.front == -1:
            return True
        else :
            return False
    pass    

def main():
    print('hello, world')
    """ Test case """
    q1 = Queue()
    q1.insert('Ruby')
    q1.insert('Java')
    q1.insert('C#')
    q1.insert(12)
    q1.delete()
    q1.delete()
    q1.delete()
    q1.delete()
    q1.insert('Jai singh')
    print('--------\n')
    q1.display()
    q1.peek()
    pass
if __name__ == '__main__':
    main()