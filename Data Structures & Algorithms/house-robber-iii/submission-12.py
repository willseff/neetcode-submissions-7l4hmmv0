# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        cache = {}

        def mem(root):
            if root in cache:
                return cache[root]
            
            # max if current node is robbed
            if not root:
                return 0
            #print(root.val)
            if root.left and root.right:
                robMax = root.val + mem(root.left.left) + mem(root.left.right) + mem(root.right.right) + mem(root.right.left)
            elif root.left:
                robMax = root.val + mem(root.left.left) + mem(root.left.right)
            elif root.right:
                robMax = root.val + mem(root.right.right) + mem(root.right.left)
            else:
                #print("leaf node")
                cache[root] = root.val
                return root.val

            #print("RobMax: " + str(robMax))

            # vs max if current node isn't robbed
            noRobMax = mem(root.right) + mem(root.left)

            #print("noRobMax: " + str(noRobMax))
            cache[root] = max(robMax, noRobMax)
            return cache[root]

        return mem(root)
        