# DFS (Depth-First Search) -> all paths from a to b; subset; topological sort; cycle detection:
# RUNTIME = O(V + E) => visits all vertices V and edges
# SPACE = O(V) => queue stores all vertices V
# stack = LIFO
# Pseudo-code =>
# DFS(graph, node, visited):
#   mark node as visited
#   process node (print)
#   for neighbour in node:
#       if neighbour not in visited:
#           recursively call DFS on neighbour
# 
# explanation:
# 1. Create a set to keep track of visited nodes.
# 2. Start from the initial node.
# 3. Mark the node as visited and process it (e.g., print it).
# 4. For each neighbor of the node:
#     a. If it hasn’t been visited:
#         - Recursively apply DFS on the neighbor.
# 5. DFS will keep going down one path until it reaches a dead end,
#    then it backtracks and explores the next branch.
# 
# implementation:
# First Call =>
# visited: A
# stack: A -> recurse to B

# Second Call =>
# visited: A, B
# stack: A, B -> recurse to D

# Third Call =>
# visited: A, B, D
# stack: A, B, D; D has no neighbors -> return to B (LIFO)

# Fourth Call =>
# backtrack to B -> recurse to E
# visited: A, B, D, E
# stack: A, B, E -> recurse to F

# Fifth Call =>
# visited: A, B, D, E, F
# stack: A, B, E, F; F has no neighbors -> return to E -> return to B

# Sixth Call =>
# backtrack to A -> recurse to C
# visited: A, B, D, E, F, C
# stack: A, C -> recurse to F; F is visited -> return

# Traversal Complete
# Final Visited Order (DFS):
# A -> B -> D -> E -> F -> C
# 
# recursive structure:
# dfs("A")
# ├── dfs("B")
# │   ├── dfs("D")   <- returns (no neighbors) --returns to %rip register in dfs("B")
# │   └── dfs("E")
# │       └── dfs("F") <- returns (no neighbors)
# │       <- returns to dfs("B")
# <- returns to dfs("A")
# └── dfs("C")
#     └── dfs("F") <- already visited -> skip
# 
# implementation:
graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["F"],
    "F": []
}

# def dfs(g, v, visited = None):
#     # only create visited on first iteration
#     if visited == None:
#         visited = set()

#     visited.add(v)
#     print("current vertex:", v)

#     for neighbour in g[v]:
#         if neighbour not in visited:
#             dfs(g, neighbour, visited)

# print(dfs(graph, "A"))

# PRACTICE 05/25/2025
# def dfs(g, v, visited = None):
#     if visited == None:
#         visited = set()
    
#     visited.add(v)
#     print("current vertex:", v)

#     for neighbour in g[v]:
#         if neighbour not in visited:
#             dfs(g, neighbour, visited)

# def dfs(g, v, visited = None):
#     if visited == None:
#         visited = set()
    
#     visited.add(v)
#     print("current vertex:", v)

#     for neighbour in g[v]:
#         if neighbour not in visited:
#             dfs(g, neighbour, visited)

# def dfs(g, v, visited = None):
#     if visited == None:
#         visited = set()
    
#     visited.add(v)
#     print("current v:", v)

#     for neighbour in g[v]:
#         if neighbour not in visited:
#             dfs(g, neighbour, visited)

# def dfs(g, v, visited = None):
#     if visited == None:
#         visited = set()
    
#     visited.add(v)
#     print("current v:", v)
    
#     for neighbour in g[v]:
#         if neighbour not in visited:
#             dfs(g, neighbour, visited)

# print(dfs(graph, "A"))


# def dfs(g, v, visited = None):
#     if visited == None:
#         visited = set()
    
#     visited.add(v)
#     print("current v:", v)

#     for neighbour in g[v]:
#         if neighbour not in visited:
#             dfs(g, neighbour, visited)

# def dfs(g, v, visited = None):
#     if visited == None:
#         visited = set()
#     visited.add(v)
#     print("current node:", v)
#     for neighbour in g[v]:
#         if neighbour not in visited:
#             dfs(g, neighbour, visited)

# print(dfs(graph, "A"))

# def dfs(g, v, visited = None):
#     if visited == None:
#         visited = set()
    
#     visited.add(v)
#     print("current v:", v)

#     for neighbour in g[v]:
#         if neighbour not in visited:
#             dfs(g, neighbour, visited)

# def dfs(g, v, visited = None):
#     if visited == None:
#         visited = set()

#     visited.add(v)
#     print("current:", v)
#     for neighbour in g[v]:
#         if neighbour not in visited:
#             dfs(g, neighbour, visited)

# def dfs(g, v, visited = None):
#     if visited == None:
#         visited = set()
    
#     visited.add(v)
#     print("current v:", v)

#     for neighbour in g[v]:
#         if neighbour not in visited():
#             dfs(g, neighbour, visited)

# def dfs(g, v, visited = None):
#     if visited == None:
#         visited = set()

#     visited.add(v)
#     print("current v:", v)

#     for neighbour in g[v]:
#         if neighbour not in visited:
#             dfs(g, neighbour, visited)


def dfs(g, v, visited = None):
    if visited == None:
        visited = set()
    
    visited.add(v)
    print("current v:", v)

    for neighbour in g[v]:
        if neighbour not in visited:
            dfs(g, neighbour, visited)