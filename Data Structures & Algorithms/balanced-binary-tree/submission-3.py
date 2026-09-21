# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        result = True
        def helper(node):
            nonlocal result
            if not node.left and not node.right:
                return 0
            
            if node.left: left = helper(node.left) + 1
            else: left = 0
            if node.right: right = helper(node.right) + 1
            else: right = 0
            result = result & (abs(left - right) <= 1)
            return max(left, right)
        if not root:
            return True
        helper(root)
        return result

