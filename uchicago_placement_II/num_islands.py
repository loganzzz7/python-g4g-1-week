from collections import defaultdict, deque


class Connection:
    """
    A connection between two places, with a mode of transport
    (either "road" or "boat"). The connection is undirected,
    meaning that if there is a connection from src to dst,
    there is also a connection from dst to src.
    """
    def __init__(self, src: str, dst: str, mode: str):
        self.src = src
        self.dst = dst
        self.mode = mode

def num_islands(places: list[str],
                connections: list[Connection],
                start: str) -> int:
    """
    Given a list of places and a list of connections between them,
    this function computes the number of distinct islands that can be
    reached from a starting place using the connections, subject to
    the constraints described in the problem statement.

    Args:
        places (list[str]): A list of place names.
        connections (list[Connection]): A list of connections between places.
        start (str): The starting place from which to count reachable islands.

    Returns: the number of distinct islands reachable from the start place.
    """
    # TODO: Implement this function.
    # use a bfs soln to count islands like num_islands leetcode
    # construct graph
    same_island_road = defaultdict(list)
    diff_island_boat = defaultdict(list)
    
    # make graph for diff islands and also graph for how islands connect
    for con in connections:
        if con.mode == "road":
            same_island_road[con.src].append(con.dst)
            same_island_road[con.dst].append(con.src)
        elif con.mode == "boat":
            diff_island_boat[con.src].append(con.dst)
            diff_island_boat[con.dst].append(con.src)
    
    # bfs to transform graph into islands
    visited = set()
    islands = []
    place_to_island_map = {}
    
    for place in places:
        if place in visited:
            continue
        
        queue = deque()
        queue.append(place)
        curr_island = set()
        
        # map out entire island == connected by road
        while len(queue) > 0:
            curr = queue.popleft()
            if curr in visited:
                continue
            visited.add(curr)
            curr_island.add(curr)
            for neighbour in same_island_road[curr]:
                queue.append(neighbour)
        
        # index the islands (places on one island mapped to same idx)
        island_idx = len(islands)
        for p in curr_island:
            place_to_island_map[p] = island_idx
        # add connected by road island to island []
        islands.append(curr_island)
            
            
    # after done map -> use start to check boat routes from start island
    start_idx = place_to_island_map[start]
    
    can_reach_ids = set()
    
    # itr places on start island and check for boat routes
    for place in islands[start_idx]:
        for boat_des in diff_island_boat[place]:
            target_island_id = place_to_island_map[boat_des]
            if target_island_id != start_idx:
                can_reach_ids.add(target_island_id)
    
    # num of reachable islands
    return len(can_reach_ids)

def mk_connections_3islands() -> list[Connection]:
    """
    Create a list of connections for the three-island test case.
    """
    return [
        Connection("A", "B", "road"),
        Connection("B", "C", "boat"),
        Connection("C", "D", "road"),
        Connection("D", "E", "boat"),
        Connection("E", "F", "road"),
        Connection("F", "G", "road")
    ]

def mk_connections_5islands() -> list[Connection]:
    """
    Create a list of connections for the five-island test case.
    """
    return [
        Connection("A", "B", "road"),
        Connection("B", "C", "road"),
        Connection("C", "D", "road"),
        Connection("B", "D", "road"),

        Connection("F", "G", "road"),
        Connection("G", "H", "road"),
        Connection("F", "H", "road"),

        Connection("I", "J", "road"),

        Connection("K", "L", "road"),
        Connection("L", "M", "road"),
        Connection("M", "N", "road"),

        Connection("D", "E", "boat"),
        Connection("E", "F", "boat"),
        Connection("G", "N", "boat"),
        Connection("H", "I", "boat"),
        Connection("I", "L", "boat"),
        Connection("J", "M", "boat")
    ]