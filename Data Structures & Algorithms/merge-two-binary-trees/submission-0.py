# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
            
        def inOrder(root1, root2):

            if not root1 and not root2:
                return

            elif not root1:
                root3 = TreeNode(val=root2.val)
                root3.left = inOrder(root2.left, None)
                root3.right = inOrder(root2.right, None)
            
            elif not root2:
                root3 = TreeNode(val=root1.val)
                root3.left = inOrder(root1.left, None)
                root3.right = inOrder(root1.right, None)
            
            elif root1 and root2:
                root3 = TreeNode(val=root1.val + root2.val)
                root3.left = inOrder(root1.left, root2.left)
                root3.right = inOrder(root1.right, root2.right)

            return root3

        return inOrder(root1, root2)

           