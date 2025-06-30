# problem:
# Given the root of a binary tree, return the level order traversal of its nodes' values. 
# (i.e., from left to right, level by level).
# 
# soln:
# iterative bfs
# start a queue =>
# put root in queue
# then bfs the tree
# for every node:
#   track the nodes values of this level &
#   add its children into the queue
# then after every level => put the level in the result arr if it is not []
# return result
# 
# implementation:
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        
        queue = deque()
        queue.append(root)
        
        while queue:
            level = []
            for i in range(len(queue)):
                curr = queue.popleft()
                if curr:
                    level.append(curr.val)
                    queue.append(curr.left)
                    queue.append(curr.right)
            if level:
                result.append(level)
        return result