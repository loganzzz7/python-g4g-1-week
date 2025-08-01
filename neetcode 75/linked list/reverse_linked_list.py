# problem:
# Given the head of a singly linked list, reverse the list, and return the reversed list.
# 
# soln: use tmp val
# change curr's next to prev and continue until end of list
# 
# implementation:
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        return prev