import Singly_linked_list
li = Singly_linked_list.List()
for x in [1,5,2,10,4,1,5,10,2,4,5,10,2,5,4,41,0,10]:
    li.createList(x)

def del_all(val):
    node = li.head
    prev = None
    while node :
        if node.data == val:
            if node is li.head:
                li.head = node.next
            else:
                prev.next = node.next
            
        prev = node
        node = node.next
    pass

        



def main():
    li.print_list()
    del_all(49)
    print('\n----------------\n')
    li.print_list()
    pass



if __name__ == '__main__':
    main()
