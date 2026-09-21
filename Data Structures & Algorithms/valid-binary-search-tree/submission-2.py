# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        traversal = []
        def inorder(node):
            nonlocal traversal
            if node.left:
                inorder(node.left)
            traversal.append(node.val)
            if node.right:
                inorder(node.right)

            return
        
        inorder(root)
        print(traversal)
        for i in range(1, len(traversal)):
            if traversal[i] <= traversal[i - 1]:
                return False
        return True
