class  Node(object):
    next = None
    data = None
    def __init__(self,val,nex):
        self.next = nex
        self.data = val
        pass

    pass 
class  List(object):
    head = None

    def  create_list(self,val):
        node = Node(val,self.head)
        self.head = node

        pass
    def list_size(self):
        node = self.head
        length = 0
        while node:
            length+=1
            node = node.next
        return length

    ''' function for checking identical or not O( N^2 )'''    
    def isIdentical(self,lis):
        co = 0
        if self.list_size() != lis.list_size() :
            return False
        node1 = self.head
        while  node1:
            node2 = lis.head
            while node2:

                if node1.data == node2.data :
                    co+=1
                    break
                node2 = node2.next
                pass
            node1 = node1.next
            pass
        if co == self.list_size():
            return True
        else :
        
            return False      
        
    pass



def main():
    

    li1 = List()
    li2 = List()

    li1.create_list('ravi')
    li1.create_list('jai')
    li1.create_list('jack')
    li1.create_list('govi')
    li1.create_list('saini')


    li2.create_list('saini')
    li2.create_list('jack')
    li2.create_list('govi')
    li2.create_list('ravi')
    li2.create_list('jai')
    x = li1.isIdentical(li2)
        
    print(x)
    
    pass








if __name__ == '__main__':
    main()