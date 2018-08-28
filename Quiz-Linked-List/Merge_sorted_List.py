import Singly_linked_list

lis1 = Singly_linked_list.List()
lis2 = Singly_linked_list.List()
lis   = Singly_linked_list.List()


def merge(lis1,lis2):
    node1 = lis1.head
    node2 = lis2.head
   
    while node1:
        while node2:
            if node1.data >= node2.data:
                lis.createList(node1.data)
                break
            else:
                lis.createList(node2.data)
            node2 = node2.next
            pass

def sort_SLL(lis):

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

    for x in [1, 0, 8, 1, 4, 6, 125, 45, 12, 30, 12]:
        lis1.createList(x)

    for x in [1, 0, 8, 1, 4, 6, 125, 45, 12, 30, 12]:
        lis2.createList(x)

    sort_SLL(lis1)
    sort_SLL(lis2)
    merge(lis1,lis2)

    print('\n--Sorted Linked list--\n')
    lis.print_list()
    pass


if __name__ == '__main__':
    main()