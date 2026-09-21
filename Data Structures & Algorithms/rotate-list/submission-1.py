# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None: return head
        
        curr = head
        count = 1
        while curr.next is not None:
            curr = curr.next
            count += 1
        curr.next = head
        length = count
        count = 0
        curr = head
        k = length - (k % length)
        while count < k:
            curr = curr.next
            count += 1
        result = curr
        for i in range(length - 1):
            curr = curr.next
        
        curr.next = None
        return result
