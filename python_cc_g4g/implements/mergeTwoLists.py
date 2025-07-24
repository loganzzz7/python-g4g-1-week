class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
    
def buildList(vals):
    dummy = ListNode()
    curr = dummy
    for val in vals:
        curr.next = ListNode(int(val))
        curr = curr.next
    return dummy.next

def printList(head):
    res = []
    
    while head:
        res.append(str(head.val))
        head = head.next
    return print("-->".join(res))

def mergeTwo(l1, l2):
    dummy = ListNode()
    tail = dummy
    
    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    if l1:
        tail.next = l1
    if l2:
        tail.next = l2
    return dummy.next

def main():
    l1vals = [1, 6, 9, 14, 67]
    l2vals = [2, 4, 5, 90, 99]
    
    l1 = buildList(l1vals)
    l2 = buildList(l2vals)
    print("l1: ")
    printList(l1)
    print("\nl2: ")
    printList(l2)
    print("\nmerged: ")
    printList(mergeTwo(l1, l2))
    
if __name__ == "__main__":
    main()