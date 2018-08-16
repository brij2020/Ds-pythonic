import Singly_linked_list

# Linked List function
lis = Singly_linked_list.List()
def remove_first():

    node = lis.head
    prev = None
    while node :
        prev = node
        node = node.next
        pass
    xnode = lis.head
    lis.head = xnode.next
    prev.next = xnode
    xnode.next = None
    
    pass

def main():
    for x in ['C#','Ruby','Python','Pascal']:
        lis.createList(x)
    lis.print_list()
    remove_first()
    print('\n-------------\n')
    lis.print_list()
    pass


if __name__ == '__main__':
    main()
