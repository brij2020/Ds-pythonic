import random
import Singly_linked_list

li = Singly_linked_list.List()

for num in range(15,20):
    li.createList(random.randint(20,50))


def foo():
    node = li.head
    max = node.data
    node = node.next
    prev = None
    while node :
        prev = node
        if max < node.data:
            max   = node.data
            xnode = node 
        node = node.next
    
    temp = prev.data
    prev.data = max
    xnode.data = temp

def main():
    li.print_list()
    foo()
    print('\n----------\n')
    li.print_list()


if __name__ == '__main__':
    main()