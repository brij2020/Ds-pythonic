import random
import Singly_linked_list

li = Singly_linked_list.List()

for num in range(15, 20):
    li.createList(random.randint(20, 50))

def move_smallest_elem_to_begning():
    node = li.head
    min  = node.data
    xnode = None 
    while node :
        if node.data <= min:
            min = node.data
            xnode = node
        node = node.next
    xdata = li.head.data
    li.head.data = min
    xnode.data = xdata
    pass




def main():
    li.print_list()
    move_smallest_elem_to_begning()
    print('\n--operation ---\n')
    li.print_list()
    pass


if __name__ == '__main__':
    main()