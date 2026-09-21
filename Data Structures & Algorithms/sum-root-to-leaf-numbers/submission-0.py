# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        all_num = []
        def traversal(node, number):
            nonlocal all_num
            if not node.left and not node.right:
                all_num.append(number * 10 + node.val)
                return

            if node.left:
                traversal(node.left, number * 10 + node.val)

            if node.right:
                traversal(node.right, number * 10 + node.val)
            return
        
        traversal(root, 0)

        return sum(all_num)