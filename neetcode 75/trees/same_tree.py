# problem:
# Given the head of a linked list, remove the nth node from the end of the list and return its head.
# Example 1:
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# 
# soln:
# use l and r ptrs 
# let r be n ahead of l
# once r reaches end -> l.next will be the nth node that needs to be removed
# then make l.next = l.next.next -> discarding the nth node
# 
# implementation:
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        l = dummy
        r = head.next
        
        while n > 0:
            r = r.next
            n -= 1
        
        while r:
            l = l.next
            r = r.next
            
        l.next = l.next.next
        
        return dummy.next