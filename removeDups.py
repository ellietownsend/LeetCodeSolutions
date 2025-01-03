# Creating a
class Node(object):
    def __init__(self,val):
        self.val = val
        self.next = None

class Solution(object):
    def removeDups(head):
        p1 = head
        p2 = head.next

        while p2:
            if p1.val == p2.val:
                p1.next = p2.next
            else:
                p1 = p1.next

            p2 = p2.next

        pointer3 = head
        while pointer3:
            print(pointer3.val)
            pointer3 = pointer3.next



#List 1:
node1 = Node(1)
node2 = Node(2)
node1.next = node2
node3 = Node(3)
node2.next = node3
node4= Node(3)
node3.next = node4
node5 = Node(4)
node4.next = node5
node6 = Node(4)
node5.next = node6


solution =  print(Solution.removeDups(node1))