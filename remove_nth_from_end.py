# Two Pointers
# March 3, 2021

def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
    dummy = ListNode(0)
    dummy.next = head
    walker = dummy
    runner = dummy
    
    for i in range(n+1):
        runner = runner.next
        
    while runner:
        runner = runner.next
        walker = walker.next

    walker.next = walker.next.next
    return dummy.next