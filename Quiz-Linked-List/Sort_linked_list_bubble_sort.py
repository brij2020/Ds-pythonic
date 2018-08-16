import Singly_linked_list

lis = Singly_linked_list.List()

def sort_SLL():

    node1 = lis.head
    while node1:
        node2 = lis.head
        while node2:
            if node1.data <= node2.data:
                temp = node1.data
                node1.data = node2.data
                node2.data = temp
            node2 = node2.next    
        node1 = node1.next
    pass

def main():

    for x in ['Ramesh','Loki','Jai','Arnab']:
        lis.createList(x)
    lis.print_list()
    sort_SLL()
    print('\n--Sorted Linked list--\n')
    lis.print_list()
    pass

if __name__ == '__main__':
    main()