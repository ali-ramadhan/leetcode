# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def contains(root, p, memory):
    if not root:
        return False
    
    key = (root.val, p.val)
    if key in memory:
        return memory[key]

    if root.val == p.val:
        memory[key] = True
        return True

    result = contains(root.left, p, memory) or contains(root.right, p, memory)
    memory[key] = result

    return result

def contains_left(root, p, memory):
    if root:
        return root.val == p.val or contains(root.left, p, memory)
    else:
        return False

def contains_right(root, p, memory):
    if root:
        return root.val == p.val or contains(root.right, p, memory)
    else:
        return False

def lowest_common_ancestor(root, p, q, memory):
    p_in_left = contains_left(root, p, memory)
    p_in_right = contains_right(root, p, memory)
    q_in_left = contains_left(root, q, memory)
    q_in_right = contains_right(root, q, memory)

    if (p_in_left and q_in_right) or (q_in_left and p_in_right):
        return root
    elif p_in_left and q_in_left:
        return lowest_common_ancestor(root.left, p, q, memory)
    elif p_in_right and q_in_right:
        return lowest_common_ancestor(root.right, p, q, memory)

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return lowest_common_ancestor(root, p, q, {})
