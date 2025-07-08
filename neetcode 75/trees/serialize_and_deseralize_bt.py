# problem:
# Serialization is the process of converting a data structure or object into a sequence of bits 
# so that it can be stored in a file or memory buffer, or transmitted across a network connection 
# link to be reconstructed later in the same or another computer environment.
# 
# Design an algorithm to serialize and deserialize a binary tree. 
# There is no restriction on how your serialization/deserialization algorithm should work. 
# You just need to ensure that a binary tree can be serialized to a string and 
# this string can be deserialized to the original tree structure.
# 
# soln:
# use preorder traversal on the seralized string to create new tree
# when reconstructing tree => recursive dfs preorder: basecase == when l and r children are null
# to seralize tree -> run dfs and for null nodes append "N"; else append node.val
# 
# implementation:
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        def dfs(node):
            if not node:
                res.append("N")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(res) # => convert output into a string e.g. -> "1, 2, N, N, 3, 4, N, N, 5, N, N"

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        vals = data.split(",") # use comma to split up data str into list e.g. -> [1, 2, N, N, 3, 4, N, N, 5, N, N]
        self.i = 0 # pointer to track where in the data str we are
        
        def dfs():
            if vals[self.i] == "N":
                # "N" represents a Null node -> inc pointer and ret a null node
                self.i += 1
                return None
            else:
                node = TreeNode(int(vals[self.i])) # => vals is a str arr -> convert to int and use it as node.val
                self.i += 1 # => inc ptr
            node.left = dfs() # => create left node with next i
            node.right = dfs() # => create right node with next next i
            return node
        return dfs()