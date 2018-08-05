 
class  Node(object):

    data = None
    next = None
    pass

class LinkedList(object):
    
    head = None

    def createList(self,val):
        node = Node()
        node.data = val
        node.next = self.head
        self.head = node
        
    def find_Occurences(self, elem_value):
        node = self.head
        counter = 0
        while node:
            if node.data == elem_value :
                counter+=1
            node = node.next
        return counter
        
 
    pass


def main():

    List = LinkedList()
    for x in ['C#','Ruby','JavaScript','Python','']:
        List.createList(x)
    List.createList('C#')
    List.createList('C#')
    List.createList('Python')
    List.createList('Ruby')
    
    print(List.find_Occurences('Python'))
    


    pass

if __name__ == '__main__':
    main()

"""
    Coplexity of this  method 
        def find_Occurences(self, elem_value):

        O(N)    
"""