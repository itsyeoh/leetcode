# Linked List
# March 6, 2021


class Solution:
	# l1: [3,1,4]
	# l2: [7,0,9]
	# L:  [0,2,3,1]
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    	sumHead = dummy = ListNode(0)
    	carry = 0
    	val = 0

    	while l1 or l2 or carry:
    		val = carry + (l1.val if l1 else 0) + (l2.val if l1 else 0)
    		l1 = l1.next if l1 else None
    		l2 = l2.next if l2 else None
    		dummy.next = ListNode(val % 10)
    		carry = val//10
    		dummy = dummy.next
    	return sumHead.next