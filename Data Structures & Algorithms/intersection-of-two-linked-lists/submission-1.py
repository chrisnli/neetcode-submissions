# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        setA = set()
        setA.add(headA)
        setB = set()
        setB.add(headB)
        currA = headA
        currB = headB
        while currA is not None or currB is not None:
            if currA:
                setA.add(currA)
                if currA in setB:
                    return currA

                currA = currA.next
            if currB:
                setB.add(currB)
                if currB in setA:
                    return currB
                
                currB = currB.next
        return None