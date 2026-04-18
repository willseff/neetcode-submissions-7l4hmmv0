# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val=val)
            
        curr = root
        while curr:
            print(curr.val)
            if val < curr.val:
                if curr.left:
                    curr = curr.left
                else:
                    curr.left = TreeNode(val=val)
                    curr = None
            else:
                print("else")
                if curr.right:
                    print("new curr")
                    curr = curr.right
                else:
                    print('no curr')
                    curr.right = TreeNode(val=val)
                    curr = None

        return root
            
        