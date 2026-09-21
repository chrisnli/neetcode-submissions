# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        

        def traversal(node):
            if node.left == None and node.right == None and node.val == target:
                return None

            if node.left:
                node.left = traversal(node.left)
            
            if node.right:
                node.right = traversal(node.right)

            if node.left == None and node.right == None and node.val == target:
                return None
            
            return node
        
        
        return traversal(root)