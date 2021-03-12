# Intersection of Two Linked Lists
# March 4, 2021
# Time - O(m+n)

def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:       
    def getCount(head):
        count = 0
        curr = head
        
        while curr:
            count += 1 
            curr = curr.next
        return count
     
    def getIntersection(d, headA, headB):
        walkerA = headA
        walkerB = headB
        
        for i in range(d):
            if walkerA is None:
                return None
            walkerA = walkerA.next
    
        while walkerA and walkerB:
            if walkerA == walkerB:
                return walkerA
            walkerA = walkerA.next
            walkerB = walkerB.next
        return None

    countA = getCount(headA)
    countB = getCount(headB)
        
    if countA > countB:
        d = countA - countB
        return getIntersection(d, headA, headB)
    else:
        d = countB - countA
        return getIntersection(d, headB, headA)