'''
Problem: Given the head of a linked list, rotate the list to the right
by k places.
'''
class Node(object):
    def __init__(self,val):
        self.val = val
        self.next = None

class Solution(object):
    def rotateList(head, k):
        if not head or not head.next or k == 0:
            return head

        for _ in range(k):
            pointer1 = head
            pointer2 = head.next
            while pointer2.next:
                pointer1 = pointer1.next
                pointer2 = pointer2.next

            pointer2.next = head
            head = pointer2
            pointer1.next = None


        pointer3 = head
        while pointer3:
            print(pointer3.val)
            pointer3 = pointer3.next




node = Node(1)
node1 = Node(2)
node.next = node1
node2 = Node(3)
node1.next = node2
node3 = Node(4)
node2.next = node3
node4 = Node(5)
node3.next = node4
solution = print(Solution.rotateList(node, 3))






