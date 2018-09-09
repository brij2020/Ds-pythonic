"""
    QUIZE :
            Store information in linked list 
"""

'''****** MARK Linked List for Each Students ******** '''
class Mark(object):
    next = None
    mark = None
    pass
class Mark_lis(object) :
    head = None
    def markList(self, val):
        node = Mark()
        node.mark = val
        node.next = self.head
        self.head = node
        pass
''' ********************** END *******************''' 


'''***************Students Linked List ************'''
class Node(object):
    roll  = None
    name  = None
    next  = None
    pass

class Students(object):
    head = None
    marks = None
    students = []
    pass_status  = 0

    def store_data(self,roll, name , marks_list):     
        Students.students.append(self)
        node = Node()
        node.roll = roll
        node.name = name
        self.marks = Mark_lis()
        for x in marks_list :
            self.marks.markList(x)        
        node.next = self.head
        self.head = node
    pass

    @staticmethod
    def detail_All_students():
        total = 0
        for x in Students.students:
            mar = x.marks.head
            while mar :
                total += mar.mark
                mar = mar.next
            if (total/3)>=40 :
                Students.pass_status += 1
        print(Students.pass_status)
        pass

    def show_data(self):
        node = self.head
        while node:
            print('{} {}'.format(node.roll,node.name))
            node = node.next
        pass
    pass


def main():
    st1  = Students()
    st2  = Students()
    st3  = Students()
    st4  = Students()

    st1.store_data(120,'Brijbhan',[44,35,30])
    st2.store_data(121,'Ramesh',[12,13,25])
    st3.store_data(122,'Gopi',[12,35,20])
    st4.store_data(123,'Aand',[23,34,26])
    Students().detail_All_students()


    pass

if __name__ == '__main__':
    main()
