#Creating a blueprint of our Node
class Node(object):
    def __init__(self,val):
        self.val = val
        self.next = None

class Soltuion(object):
    def reverse(head):
        # We need to keep track of the previous node because this is a singly
        # linked list, and if we do not have it we can not access it when we
        # move further down the list, we set it to none because it now acts as our tail
        prev = None
        curr = head

        while curr:
            # Our goal is to change current's pointer to the previous node, but
            # when we do so, we no longer have access to curr.next so we need a pointer to make sure we have access to it still
            myNext = curr.next
            # Usually when traversing we ".next", but here we set them to different pointers that are being used
            # Mostly because were changing the pointers so frequently
            curr.next = prev
            prev = curr
            curr = myNext

        # View resulting Linked List:
        # Why start at prev? Because prev has traversed the whole list, and now represents the beginning (head)
        pointer3 = prev
        while pointer3:
            print(pointer3.val)
            pointer3 = pointer3.next


node1 = Node(1)
node2 = Node(2)
node1.next = node2
node3 = Node(3)
node2.next = node3
node4 = Node(4)
node3.next = node4
node5 = Node(5)
node4.next = node5

mySolution = print(Soltuion.reverse(node1))


