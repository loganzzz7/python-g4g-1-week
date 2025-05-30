# BFS (Breadth First Seach) -> shortest path; word ladder; level order traversal; cycle detection:
# RUNTIME = O(V + E) => visits all vertices V and edges
# SPACE = O(V) => queue stores all vertices V
# start at 0 node => search neighbours of 1 distance, 2 distance, 3 distance, ...
# queue => FIFO
# Pseudo-code =>
# BFS(graph, start):
#     Create a queue and enqueue the start node
#     Mark the start node as visited
#     While the queue is not empty:
#         Dequeue the current node
#         Process the current node (e.g., print it)
#         For each neighbor of the current node:
#             If the neighbor has not been visited:
#                 Mark it as visited
#                 Enqueue the neighbor
# 
# problems:
# 1. shortest-path on unweighted graph
# 2. level order traversal
# 3. finding the minimum number of operations --> reach a goal w the fewest number of moves
# 4. flood fill --> fill matrix of connected cells
# 
# draw:
#               A
#           B       C
#       D   E-------F
# 
# -------- traversal --------
# First Iteration =>
# visited: A
# queue: A (front)
# 
# Second Iteration =>
# visited: A, B, C
# queue: A (remove); B (front) and C enqueued
# 
# Third Iteration =>
# visited: A, B, C, D, E
# queue: B (remove), C (front); D and E enqueued
# 
# Fourth Iteration =>
# visited: A, B, C, D, E, F
# queue: C (remove), D (front), E; F enqueued
# 
# Fifth Iteration =>
# visited: A, B, C, D, E, F
# queue: D (remove), E (front), F; NO NEIGHBOURS SO NOTHING ENQUEUED
# 
# Sixth Iteration =>
# visited: A, B, C, D, E, F
# queue: E (remove), F (front); F is neighbour but already visited so SKIP
# 
# Seventh Iteration =>
# visited: A, B, C, D, E, F
# queue: F (remove); EMPTY QUEUE => No neighbours --BFS DONE
# 
# implementation:
from collections import deque

graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["F"],
    "F": []
}

# explanation:
# create a set of visited
# create a queue of vertices
# place the first vertice in visited and add it to queue
# pop the first vertice; 
#   => if the neighbours of the first vertice are not visited;
#       => add them to visited and queue them
# go to the second vertice queued and repeat until no more queued vertices left
# def breadth_first_search(g, v):
#     visited = set()
#     queue = deque()
#     queue.append(v)
#     visited.add(v)
#     while len(queue) > 0:
#         current = queue.popleft()
#         print("current node:", current)
#         # print("current neighbours:", g[current])
#         for neighbour in g[current]: # => g[current] is a list of neighbours => [b, c...]
#             if neighbour not in visited:
#                 visited.add(neighbour)
#                 queue.append(neighbour)

# print(breadth_first_search(graph, "A"))
# current node: A
# current node: B
# current node: C
# current node: D
# current node: E
# current node: F
# None

# PRACTICE 05/24/2025
# def breadth_first_search(g, v):
#     # init a list of visited
#     # init a queue of v
#     visited = set()
#     queue = deque()
#     # add the first node to visited
#     # add the first node to queue
#     visited.add(v)
#     queue.append(v)
#     while len(queue) > 0:
#         # pop the first v in queue
#         current = queue.popleft()
#         print("current node:", current)
#         # traverse the neighbours of v
#         for neighbour in g[current]:
#             # if not visited => add them to visited and queue them
#             if neighbour not in visited:
#                 visited.add(neighbour)
#                 queue.append(neighbour)

# print(breadth_first_search(graph, "B"))

# def bfs(g, v):
#     # init visited & queue
#     visited = set()
#     queue = deque()
#     visited.add(v)
#     queue.append(v)
#     while len(queue) > 0:
#         current = queue.popleft()
#         print("current node:", current)
#         for neighbour in g[current]:
#             if neighbour not in visited:
#                 visited.add(neighbour)
#                 queue.append(neighbour)

# print(bfs(graph, "A"))

# def bfs(g, v):
#     visited = set()
#     queue = deque()
#     visited.add(v)
#     queue.append(v)
#     while len(queue) > 0:
#         current = queue.popleft()
#         print("current node:", current)
#         for neighbour in g[current]:
#             if neighbour not in visited:
#                 visited.add(neighbour)
#                 queue.append(neighbour)

# print(bfs(graph, "A"))

# def bfs(g, v):
#     visited = set()
#     queue = deque()
#     visited.add(v)
#     queue.append(v)
#     while len(queue) > 0:
#         current = queue.popleft()
#         print("current node:", current)
#         for neighbour in g[current]:
#             if neighbour not in visited:
#                 visited.add(neighbour)
#                 queue.append(neighbour)

# print(bfs(graph, "A"))

# def bfs(g, v):
#     visited = set()
#     queue = deque()
#     visited.add(v)
#     queue.append(v)
#     while len(queue) > 0:
#         current = queue.popleft()
#         print("current node:", current)
#         for neighbour in g[current]:
#             if neighbour not in visited:
#                 visited.add(neighbour)
#                 queue.append(neighbour)

# print(bfs(graph, "E"))

# def bfs(g, v):
#     visited = set()
#     queue = deque()
#     visited.add(v)
#     queue.append(v)
#     while len(queue) > 0:
#         current = queue.popleft()
#         print("current node:", current)
#         for neighbour in g[current]:
#             if neighbour not in visited:
#                 visited.add(neighbour)
#                 queue.append(neighbour)

# def bfs(g, v):
#     visited = set()
#     queue = deque()
#     visited.add(v)
#     queue.append(v)
#     while len(queue) > 0:
#         current = queue.popleft()
#         print("current node:", current)
#         for neighbour in g[current]:
#             if neighbour not in visited:
#                 visited.add(neighbour)
#                 queue.append(neighbour)

# print(bfs(graph, "B"))

# def bfs(g, v):
#     visited = set()
#     queue = deque()
#     visited.add(v)
#     queue.append(v)
#     while len(queue) > 0:
#         current = queue.popleft()
#         print("current node:", current)
#         for neighbour in g[current]:
#             if neighbour not in visited:
#                 visited.add(neighbour)
#                 queue.append(neighbour)

# def bfs(g, v):
#     visited = set()
#     queue = deque()
#     visited.add(v)
#     queue.append(v)
#     while len(queue) > 0:
#         current = queue.popleft()
#         print("current node:", current)
#         for neighbour in g[current]:
#             if neighbour not in visited:
#                 visited.add(neighbour)
#                 queue.append(neighbour)

# print(bfs(graph, "B"))

# def bfs(g, v):
#     visited = set()
#     queue = deque()
#     visited.add(v)
#     queue.append(v)
#     while len(queue) > 0:
#         current = queue.popleft()
#         print("current node:", current)
#         for neighbour in g[current]:
#             if neighbour not in visited:
#                 visited.add(neighbour)
#                 queue.append(neighbour)

# print(bfs(graph, "B"))

# def bfs(g, v):
#     visited = set()
#     queue = deque()
#     visited.add(v)
#     deque.append(v)
#     while len(queue) > 0:
#         current = queue.popleft()
#         print("current node:", current)
#         for neighbour in g[current]:
#             if neighbour not in visited:
#                 visited.add(neighbour)
#                 queue.append(neighbour)

# def bfs(g, v):
#     visited = set()
#     queue = deque()
#     visited.add(v)
#     queue.append(v)
#     while len(queue) > 0:
#         current = queue.popleft()
#         print("current node:", current)
#         for neighbour in g[current]:
#             if neighbour not in visited:
#                 visited.add(neighbour)
#                 queue.append(neighbour)

# print(bfs(graph, "B"))

# def bfs(g, v):
#     visited = set()
#     queue = deque()
#     visited.add(v)
#     queue.append(v)

#     while len(queue) > 0:
#         current = queue.popleft()
#         print("current node:", current)
#         for neighbour in g[current]:
#             if neighbour not in visited:
#                 visited.add(neighbour)
#                 queue.append(neighbour)

# def bfs(g, v):
#     visited = set()
#     queue = deque()
#     visited.add(v)
#     queue.append(v)
    
#     while len(queue) > 0:
#         current = queue.popleft()
#         print("current node:", current)

#         for neighbour in g[current]:
#             if neighbour not in visited:
#                 visited.add(neighbour)
#                 queue.append(neighbour)

# print(bfs(graph, "A"))

# def bfs(g, v):
#     visited = set()
#     queue = deque()
#     visited.add(v)
#     queue.append(v)

#     while len(queue) > 0:
#         current = queue.popleft()
#         print("current node:", current)
#         for neighbour in g[current]:
#             if neighbour not in visited():
#                 visited.add(neighbour)
#                 queue.append(neighbour)


# def bfs(g, v):
#     visited = set()
#     queue = deque()
#     visited.add(v)
#     queue.append(v)

#     while len(queue) > 0:
#         current = queue.popleft()
#         print("current node:", current)

#         for neighbour in g[current]:
#             if neighbour not in visited:
#                 visited.add(neighbour)
#                 queue.append(neighbour)

# print(bfs(graph, "A"))

# def bfs(g, v):
#     visited = set()
#     queue = deque()
#     visited.add(v)
#     queue.append(v)
#     while len(queue) > 0:
#         current = queue.popleft()
#         print("current:", current)

#         for neighbour in g[current]:
#             if neighbour not in visited:
#                 visited.add(neighbour)
#                 queue.append(neighbour)

# def bfs(g, v):
#     visited = set()
#     queue = deque()
#     visited.add(v)
#     queue.append(v)

#     while len(queue) > 0:
#         current = queue.popleft()
#         print("current node:", current)

#         for neighbour in g[current]:
#             if neighbour not in visited:
#                 visited.add(neighbour)
#                 queue.append(neighbour)

def bfs(g, v):
    visited = set()
    queue = deque()
    visited.add(v)
    queue.append(v)

    while len(queue) > 0:
        current = queue.popleft()
        print("current:", current)

        for neighbour in g[current]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)