# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        curr = head
        count = 1

        while curr.next:
            curr = curr.next
            count += 1
        print(count)
        if count == 1:
            print("a")
            return None
        remove_num = count - n
        print(remove_num)
        count = 1
        curr = head
        
        
        if remove_num == 0:
            print("b")
            head = head.next
            return head
        
        while curr.next and count < remove_num:
            curr = curr.next
            count += 1
        print(curr.val)
        remove = curr.next

        curr.next = remove.next
        remove.next = None

        return head