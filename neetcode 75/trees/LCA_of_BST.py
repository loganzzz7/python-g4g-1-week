# problem:
# Given a binary search tree (BST), 
# find the lowest common ancestor (LCA) node of two given nodes in the BST.
# return value of the LCA node
# According to the definition of LCA on Wikipedia: 
#     “The lowest common ancestor is defined between two nodes p and q as the lowest node 
#     in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
# 
# soln:
# two steps:
# => first need to check if root is the LCA for two given nodes p and q -> if not:
#   => if lca < root: go left; elif lca > root: go right
# => then traverse down the tree until and return the node that is valid
# 
# implementation:
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root
        
        while True:
            if p.val < curr.val and q.val < curr.val:
                # => lca must be less than curr.val -> therefore go left
                curr = curr.left
            elif p.val > curr.val and q.val > curr.val:
                # => lca must be greater than curr.val -> go right
                curr = curr.right
            else:
                # this is a valid lca
                return curr