# problem:
# Given the root of a binary tree, invert the tree, and return its root.
# 
# soln:
# recursive DFS =>
# base case:
# if not root: return None
# tmp = root.left
# root.left = root.right
# root.right = tmp
# recursive(root.left)
# recursive(root.right)
# return root
# 
# implementation
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        tmp = root.left
        root.left = root.right
        root.right = tmp
        
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root