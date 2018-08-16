import Singly_linked_list

l1 = Singly_linked_list.List()
l2 = Singly_linked_list.List()

for num in [1,7,1,3,4,5,6]:
    l1.createList(num)
for num in [1,2,34,1,23,12,34,2,12,11]:
    l2.createList(num)


def printNth():
    node = l1.head
    while node:

        if l2.size() >= l1.size():
            n = l2.head
            c = 0
            loop = node.data
            while 1:
                c+=1
                if c == loop:
                
                    print(n.data)
                    break
                n = n.next

        node = node.next
        pass

def main():
    printNth()


if __name__ == '__main__':
    main()
