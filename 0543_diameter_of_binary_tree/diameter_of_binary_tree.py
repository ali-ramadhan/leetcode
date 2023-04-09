# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameter(self, root):
        if not root:
            return 0
        else:
            l = self.diameter(root.left)
            r = self.diameter(root.right)
            self.max = max(self.max, l + r)
            return 1 + max(l, r)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max = 0
        self.diameter(root)
        return self.max
