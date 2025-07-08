# problem:
# Given a reference of a node in a connected undirected graph.
# 
# Return a deep copy (clone) of the graph.
# 
# Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.
# 
# class Node {
#     public int val;
#     public List<Node> neighbors;
# }
# 
# soln:
# hashmap of old to new with recursive dfs
# start at first node, recursively go thru each neighbour 
# -> for each neighbour recursively go through each neighbour
# until basecase => create new node with same val
# 
# implementation:
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        otn = {} #old to new hashmap
        
        def dfs(node):
            # if the node visited is already cloned => return to the cloned node
            # basecase for going back up
            if node in otn:
                return otn[node]
            
            copy = Node(node.val)
            otn[node] = copy
            
            for neighbour in node.neighbors:
                # copy each neighbour of node to the cloned node
                copy.neighbors.append(dfs(neighbour))
                # this goes to basecase where the appended neighbour is created as a node
            return copy
        dfs(node)
                