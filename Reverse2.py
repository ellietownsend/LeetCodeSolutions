#Blueprint of our node
class Node(object):
    def __init__(self,val):
        self.val = val
        self.next = None

class Solution(object):
    def reverse2(head, left, right):
        if not head or left == right:
            return head

        dummy1 = Node(0)
        dummy1.next = head
        curr = head
        dcurr = dummy1
        #Create two lists, this one is the one without reversing
        for _ in range(left-1):
            dcurr = dcurr.next
        curr = dcurr.next


        prev = None

        for _ in range(right-left + 1):
            myNext = curr.next
            curr.next = prev
            prev = curr
            curr = myNext

        dcurr.next.next = curr
        dcurr.next = prev

        return dummy1.next



















