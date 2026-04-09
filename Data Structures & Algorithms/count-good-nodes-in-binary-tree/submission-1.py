# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    numGoodNodes = 0
    def inOrderMax(self, root, maxAbove):
        if not root:
            return

        if root.val >= maxAbove:
            maxAbove = root.val
            self.numGoodNodes += 1

        self.inOrderMax(root.left, maxAbove)
        self.inOrderMax(root.right, maxAbove)
        
    def goodNodes(self, root: TreeNode) -> int:
        self.inOrderMax(root, -999999999)
        return self.numGoodNodes
        

        

        