# problem:
# Given the roots of two binary trees root and subRoot, 
# return true if there is a subtree of root with the same structure and node values of subRoot 
# and false otherwise.
# A subtree of a binary tree tree is a tree that consists of a node in tree 
# and all of this node's descendants. The tree tree could also be considered as a subtree of itself.
# 
# soln:
# recursive dfs
# for each node check if tree2 is same tree as tree1
# => two steps:
# first implement isSameTree to check if two trees are the same
# then from tree1 check if same as tree2 starting from each node.
# 
# implementation:
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True # => empty tree if subtree of any tree
        if not root:
            return False # => root is empty and subRoot is not -> therefore not match
        
        if self.isSameTree(root, subRoot):
            return True # => if init node already gives same tree then tree2 is subtree of tree1
        
        # recursive check every node if leads to same tree as subroot tree
        return (self.isSubtree(root.left, subRoot) or
                self.isSubtree(root.right, subRoot))
        
        
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        
        return (self.isSameTree(p.left, q.left) and
                self.isSameTree(p.right, q.right))