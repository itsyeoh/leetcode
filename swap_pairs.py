# Two Pointers
# March 3, 2021

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        runner = dummy
        
        while runner.next and runner.next.next:
            r1 = runner.next
            r2 = runner.next.next
            
            runner.next = r2
            r1.next = r2.next
            r2.next = r1
            
            runner = runner.next.next
        return dummy.next
        