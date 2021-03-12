# Two Pointers
# March 6, 2021
# Leetcode 82

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        new_head = ListNode(0, head)
        dummy = new_head
        
        while head:
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                dummy.next = head.next
            else:
                dummy = dummy.next
            head = head.next
            
        return new_head.next