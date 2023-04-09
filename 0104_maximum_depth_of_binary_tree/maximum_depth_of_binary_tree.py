# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def max_depth(root):
    if not root:
        return 0
    elif not root.left and not root.right:
        return 1
    elif not root.left:
        return 1 + max_depth(root.right)
    elif not root.right:
        return 1 + max_depth(root.left)
    else:
        return 1 + max(max_depth(root.left), max_depth(root.right))

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return max_depth(root)
