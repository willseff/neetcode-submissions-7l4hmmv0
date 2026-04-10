# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = -999999999

        def dfs(root):
            nonlocal res 
            if not root:
                return 0

            right = dfs(root.right)
            left = dfs(root.left)
            res = max(res, right + left + root.val, right + root.val, left + root.val, root.val)


            return max(root.val, root.val + max(dfs(root.right), dfs(root.left)))
            
        dfs(root)
        return res
            
        
        