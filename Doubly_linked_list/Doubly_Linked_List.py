###############################################
#                                             #               
#                                             #       
#               Doubly Linked List            #   
#                                             #   
#                                             #           
###############################################


print ("hello, python ! World")

'''   class for creating node with two refrences having next and prev '''  
class Node(object):
    prev = None
    data = None
    next = None
    pass

class Doubly_Linked_List(object):
    # two refrences for traversion list from both ends
    current_node = None
    tail         = None

    ''' function for creating doubly linked list  '''
    def createList(self, val):
        node = Node()
        node.data = val
        node.next = self.current_node
        self.current_node = node 
        if self.current_node.next != None:
            node.next.prev = node
        if self.current_node.next == None:
            self.tail = self.current_node
            
        pass

    ''' function for traverse list '''
    def printFromCurrentNode(self):
        node = self.current_node
        while node :
            print(node.data)
            node = node.next

    ''' function for traverse list form tail '''
    def PrintFromTail(self):
        node = self.tail
        while node :
            print(node.data)
            node  = node.prev


def main():
    print('hello, world')
    li = Doubly_Linked_List()
    for name in ['Ruby','C','C#','Java','Pascal','PHP']:
        li.createList(name)


    li.printFromCurrentNode()
    print('\n*************************\n')
    li.PrintFromTail()

if  __name__ == '__main__':
    main()