# problem:
# Given the root of a binary tree, determine if it is a valid binary search tree (BST).
# A valid BST is defined as follows:
#   The left subtree of a node contains only nodes with keys less than the node's key.
#   The right subtree of a node contains only nodes with keys greater than the node's key.
#   Both the left and right subtrees must also be binary search trees.
# 
# soln:
# two steps:
# => need a function to check of a node is valid
# when going down left tree update upper bound
# when going down right tree update lower bound
# => for every node in tree => check if it is valid 
# recursive DFS
# 
# implementation:
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        return (self.isValid(root, float("-inf"), float("inf")))
        
    def isValid(self, node, l, r):
        if not node:
            return True
        if not (node.val > l and node.val < r):
            return False
        
        return (self.isValid(node.left, l, node.val) and
                self.isValid(node.right, node.val, r))