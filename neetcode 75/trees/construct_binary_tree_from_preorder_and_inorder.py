# problem:
# Given two integer arrays preorder and inorder 
# where preorder is the preorder traversal of a binary tree and 
# inorder is the inorder traversal of the same tree, construct and 
# return the binary tree.
# 
# soln:
# IMPORTANT things to note:
# the first val of the preorder list is always the root => this is dfs from top order
# => so it tracks nodes as going down left
# inorder is dfs from base order 
# => so it goes down left tree first until reaches None and then goes back to parent
# THEREFORE => we can use nodes from preorder to find the left and right node counts in inorder
# then we use those counts to partition the rest of the preorder list to:
#   find the left side nodes and the right side nodes
#   then we build root.left which is recursive(nodes from left of inorder to root in inorder)
#   and root.right which is recursive(nodes from root in inorder to right of inorder) 
# => then we repeat this process on each side
# 
# implementation:
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        # basecase: -> if there is nothing in either list then the node is a null node
        if not preorder or not inorder:
            return None
        
        # first val in preorder is always root
        root = TreeNode(preorder[0])
        # mid is the index of root in inorder
        mid = inorder.index(preorder[0])

        # preorder[1:mid + 1] => this partitions from val after root until index of mid + 1 (exclusive)
        #   => mid is the index of root in inorder and it determines how many vals are in the left tree
        # inorder[:mid] => this is everything up to the mid index (this is the root) 
        #   => everything before the root is on left side
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
        
        return root