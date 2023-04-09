# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def depth(root):
    if not root:
        return 0
    
    return 1 + max(depth(root.left), depth(root.right))

def is_balanced(root):
    if not root:
        return True
    
    return is_balanced(root.left) and is_balanced(root.right) and abs(depth(root.left) - depth(root.right)) <= 1

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return is_balanced(root)
