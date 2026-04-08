# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    max_diameter_grand = 0
    def maxDepth(self, root:Optional[TreeNode]) -> int:
        if root :
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        else:
            return 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root:
            self.diameterOfBinaryTree(root.left)
            max_diameter = self.maxDepth(root.left) + self.maxDepth(root.right)
            if max_diameter > self.max_diameter_grand:
                self.max_diameter_grand = max_diameter
            self.diameterOfBinaryTree(root.right)

        return(self.max_diameter_grand)
        
        