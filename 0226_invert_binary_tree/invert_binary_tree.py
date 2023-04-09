# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def invert_tree(root):
    if root:
        root.left, root.right = invert_tree(root.right), invert_tree(root.left)
        return root

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return invert_tree(root)
