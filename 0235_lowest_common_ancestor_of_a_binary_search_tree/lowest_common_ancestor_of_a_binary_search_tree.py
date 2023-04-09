# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # If root is between p and q, then p and q are in different subtrees and root is the LCA.
        if p.val <= root.val <= q.val or q.val <= root.val <= p.val:
            return root
        
        if p.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q) # LCA must be in the left subtree.
        else:
            return self.lowestCommonAncestor(root.right, p, q) # LCA must be in the right subtree.
