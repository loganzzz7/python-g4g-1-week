class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def reverseList(head):
    curr = head
    prev = None
    
    while curr:
        tmp = curr.next
        curr.next = prev
        prev = curr
        curr = tmp
    return prev

def buildList(values):
    dummy = ListNode()
    curr = dummy
    
    for val in values:
        curr.next = ListNode(int(val))
        curr = curr.next
    return dummy.next

def printList(head):
    res = []
    
    while head:
        res.append(str(head.val))
        head = head.next
    return print("-->".join(res))

def main():
    values = [1, 23, 4, 5, 123]
    head = buildList(values)
    print("before reverse: ")
    printList(head)
    reversed_head = reverseList(head)
    print("after reverse: ")
    printList(reversed_head)

if __name__ == "__main__":
    main()