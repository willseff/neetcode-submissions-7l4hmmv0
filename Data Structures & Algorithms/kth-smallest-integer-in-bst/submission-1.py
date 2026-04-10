# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        k_smallest = []
        counter = 0
        def inOrder(root):
            nonlocal counter, k_smallest

            if not root:
                return

            inOrder(root.left)
            k_smallest.append(root.val)
            counter += 1
            if counter == k:
                return
            inOrder(root.right)
        
        inOrder(root)

        return k_smallest[k-1]

        