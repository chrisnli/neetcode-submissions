"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        

        q = deque()
        
        q.append(root)
        q.append(None)
        while q:
            
            curr = q.popleft()
            if curr == None: continue
            if q[0] == None:
                curr.next == None
                q.popleft()
                q.append(curr.left)
                q.append(curr.right)
                q.append(None)
                continue
            q.append(curr.left)
            q.append(curr.right)
            curr.next = q[0]
            
        
        return root