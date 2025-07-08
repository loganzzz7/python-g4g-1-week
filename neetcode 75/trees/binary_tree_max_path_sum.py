# problem:
# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence 
# has an edge connecting them. A node can only appear in the sequence at most once. 
# Note that the path does not need to pass through the root.
# 
# The path sum of a path is the sum of the node's values in the path.
# 
# Given the root of a binary tree, return the maximum path sum of any non-empty path.
# 
# soln DFS O(n):
# recursive -> traverse down left and right
# on return -> return max path sum w out split -> parent + max(l, r)
# if child is neg ret -> max(parent + child, parent)
# use a max var to track max split sum at every node -> at end return max sum between split n no split sums
# 
# code implementation:
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # init max to root val
        maxS = [root.val]
        
        def dfs(node):
            if not node:
                return 0
            leftMax = max(dfs(node.left), 0)
            rightMax = max(dfs(node.right), 0) # => avoid neg children
            
            # check for split sum at each node
            maxS[0] = max(maxS[0], node.val + leftMax + rightMax)
            
            # return max path sum w out split to prev recursive call
            return node.val + max(leftMax, rightMax)

        dfs(root)
        
        return maxS[0]