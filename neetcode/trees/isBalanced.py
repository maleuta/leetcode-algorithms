#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):
            if root is None:
                return [True, 0]

            left, right = dfs(root.left), dfs(root.right)

            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1

            return [balanced, 1+max(left[1], right[1])]

        return dfs(root)[0]


    #     if root is None:
    #         return True
        
        
    #     left_height = self.height(root.left)
    #     right_height = self.height(root.right)

    #     if abs(left_height - right_height) > 1:
    #         return False
        
    #     return self.isBalanced(root.left) and self.isBalanced(root.right)
            

    # def height(self, root):

    #         if root is None:
    #             return 0

    #         h_left = self.height(root.left)
    #         h_right = self.height(root.right)

    #         return 1 + max(h_left, h_right)
