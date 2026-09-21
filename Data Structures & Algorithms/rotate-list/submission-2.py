# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        list_len = 1
        if not head: return head
        curr = head
        while curr.next:
            list_len += 1
            curr = curr.next
        print(list_len)
        curr.next = head
        k = list_len - (k % list_len)
        print(k)
        new_head = head
        for i in range(k):
            new_head = new_head.next
        print(new_head.val)
        curr_new = new_head
        print(curr_new.next.val)
        for i in range(list_len - 1):
            curr_new = curr_new.next
        print(curr_new)
        curr_new.next = None
        return new_head