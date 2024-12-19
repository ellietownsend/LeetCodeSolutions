'''
Problem: Merge Two Sorted List
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Constraints:
The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
'''

#Create the blueprint of our node
class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution(object):
    def mergeTwoLists(self, node1, node2):
        # Edge case for empty lists
        if not node1 and not node2:
            return None
        if not node1:
            return node2
        if not node2:
            return node1
        # I will need two pointers, one at the head of each list
        pointer1 = node1
        pointer2 = node2
        # Why include a dummy node? To create our third list, instead of trying to merge one list into the other
        # When we return our list we will want to return dummy.next to disreg the dummy node
        dummy = Node(0)
        curr = dummy

        while node1 and node2:
            if node1.val < node2.val:
                curr.next = node1
                curr = node1
                node1 = node1.next
            else:
                curr.next = node2
                curr = node2
                node2 = node2.next

            curr.next = node1 if node1 else node2

        return dummy.next



