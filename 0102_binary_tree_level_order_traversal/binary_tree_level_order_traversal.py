# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def level_order(root, nodes, level=0):
    if not root:
        return nodes
    
    if level in nodes:
        nodes[level].append(root.val)
    else:
        nodes[level] = [root.val]

    if root.left:
        level_order(root.left, nodes, level+1)
    
    if root.right:
        level_order(root.right, nodes, level+1)

    return nodes


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodes = level_order(root, {})

        level = 0
        ordered = []
        while level in nodes:
            ordered.append(nodes[level])
            level += 1

        return ordered
        
