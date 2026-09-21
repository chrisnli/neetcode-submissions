# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        

        def valid(node, left, right):
            if node == None: return True
            
            curr = (node.val > left) and (node.val < right)

            return valid(node.left, left, node.val) and valid(node.right, node.val, right) and curr

        return valid(root, float('-inf'), float('inf'))
        