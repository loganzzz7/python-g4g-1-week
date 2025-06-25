# problem:
# You are given the head of a singly linked-list. The list can be represented as:
# 
# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:
# 
# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.
# 
# soln:
# separate list into first and second half;
# reverse second half
# merge the two lists
# first point to second
# second point to first .next

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = head.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None
        prev = None
        
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        first = head
        second = prev
        
        while second:
            tmpl = first.next
            tmpr = second.next
            first.next = second
            second.next = tmpl
            first = tmpl
            second = tmpr