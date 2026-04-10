# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, Max, Min):
            if not root: 
                return True

            if (root.val == Max or root.val == Min):
                return False
  
            newMax = min(Max, root.val)
            newMin = max(Min, root.val)

            if (root.val > newMax) or (root.val < newMin):
                return False

            return(dfs(root.left, newMax, Min) and dfs(root.right, Max, newMin))

        return dfs(root, 9999999999, -999999999)



        