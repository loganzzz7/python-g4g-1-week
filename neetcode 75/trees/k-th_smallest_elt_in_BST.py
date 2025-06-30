# problem:
# Given the root of a binary search tree, and an integer k, 
# return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
# 
# soln:
# can use inorder recursive dfs or
# iterative dfs =>
# traverse the tree -> add each node to stack
# when reach null child -> go back to parent and pop: first popped is smallest
# then go right child and repeat the process
# on each pop increment counter
# when counter val == k: -> most recent pop is k-th smallest elt
# return recent pop when counter == k
# 
# implementation:
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        counter = 0
        curr = root
        stack = []
        
        while curr or stack:
            while curr: # while node is not null
                # add node to stack
                stack.append(curr)
                # traverse down the left
                curr = curr.left
            # curr is now null => pop to go back to parent
            curr = stack.pop()
            counter += 1
            if counter == k:
                return curr.val
            # else go to right child and repeat process -> iterative DFS
            curr = curr.right
            