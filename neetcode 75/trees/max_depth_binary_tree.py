# problem:
# Given the root of a binary tree, return its maximum depth.
# A binary tree's maximum depth is the number of nodes along the 
# longest path from the root node down to the farthest leaf node.
# 
# soln:
# recursive dfs
# base case: 
#   if there is no root:
#       return 0
#   else recursively go down each node.
#   return 1 + max(left subtree, right subtree) # => starts with 1 + since if there is root then level = 1
# base level will return 1
# second = 1 + 1...
# top = every level counted
# 
# implementation:
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))