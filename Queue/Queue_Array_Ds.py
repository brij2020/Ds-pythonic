"""
    Queue : Implementation Base DS Array

"""

class Queue(object):
    q = []
    front = -1
    rear  = -1
    Max   = 10
    counter = 0
   
    def insert(self,data):
        if self.rear >= self.Max:
            print('Queue Overflow')
            return None
        self.rear  += 1
        self.q.append(data)
        self.counter += 1
        if self.counter == 1: 
            self.front += 1
        pass
    def delete(self):
        if self.front > self.rear:
            return 'queue is empty '
        self.q[self.front] = None
        self.front += 1
    def peek(self):
        if self.front == -1 or self.front >= self.Max:
            return None
        return self.q[self.front]
        
    def display(self):
        if self.front == -1 or self.front >= self.Max:
            return None
        else :
            for i in range(self.front,self.Max):
                print(self.q[i])
        pass
    def isFull(self):
        if self.rear >= self.Max:
            return True
        else :
            return False
        
    def isEmpty(self):
        if self.rear == -1 or self.front >= self.Max :
            return True
        else :
            return False
    pass    




def main():
    print('hello, world')
    q1 = Queue()
    
    q1.insert(0)
    q1.insert(1)
    q1.insert(211)
    q1.insert(22)
    q1.insert(23)
    q1.insert(12)
    q1.insert(85)
    q1.insert(123)
    q1.insert(45)
    q1.insert(74)
    q1.insert(55)
    print(q1.isFull())
    print(q1.peek())
    q1.delete()
    q1.delete()
    q1.delete()
    q1.delete()
    q1.delete()
    q1.delete()
    q1.delete()
    q1.delete()
    q1.delete()
    q1.delete()
    q1.delete()
    q1.delete()
    q1.delete()
    print(q1.isEmpty())
    print(q1.isFull())
    print(q1.peek())
    print('----Operation --\n')
    q1.display()
    pass
if __name__ == '__main__':
    main()