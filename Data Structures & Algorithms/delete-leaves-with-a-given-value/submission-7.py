# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:

        def postOrder(root, target):
            if not root:
                return
            
            postOrder(root.left, target)
            postOrder(root.right, target)

            if root.left:
                if not root.left.right and not root.left.left and root.left.val == target:
                    root.left = None

            if root.right:
                if not root.right.right and not root.right.left and root.right.val == target:
                    root.right = None

        postOrder(root, target)
        if root.val == target and not root.left and not root.right:
            return None
        return root

        