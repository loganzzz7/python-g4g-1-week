# problem:
# Given the roots of two binary trees p and q, 
# write a function to check if they are the same or not.
# Two binary trees are considered the same if they are structurally identical, 
# and the nodes have the same value.
# 
# soln:
# recursive dfs
# base cases:
#   if not tree1 and not tree2:
#       return True => two empty trees are equal
#   if not tree1 or not tree2:
#       return False => if one tree is empty -> not same
#   if tree1.val != tree2.val:
#       return False => if the node values of the trees are not the same -> not same
#   return recursive(tree1.left, tree2.left AND
#                   tree1.right, tree2.right)
# 
# implementation:
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        
        return (self.isSameTree(p.left, q.left) and 
                self.isSameTree(p.right, q.right))