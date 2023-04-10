# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from math import inf

def is_valid_bst(root, low=-inf, hi=inf):
    if not root:
        return True
    
    if not root.left and not root.right:
        return True
    if root.left and not root.right:
        return low < root.left.val < root.val \
               and is_valid_bst(root.left, low, min(hi, root.val))
    elif root.right and not root.left:
        return root.val < root.right.val < hi \
               and is_valid_bst(root.right, max(low, root.val), hi)
    else:
        return low < root.left.val < root.val \
               and root.val < root.right.val < hi \
               and is_valid_bst(root.left, low, min(hi, root.val)) \
               and is_valid_bst(root.right, max(low, root.val), hi)

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return is_valid_bst(root)
