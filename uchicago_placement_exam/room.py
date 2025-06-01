def clean_room(room: list[list[str]],
    start_loc: tuple[int, int],
    init_fuel: int) -> int:
    """
    Return the total number of vacuumed locations the robot sees
    while cleaning the room

    Inputs:
      room: the matrix of single characters. A "v" represents a
        cleaned location and "d" represents a dirty location.
      start_loc: the starting location for the robot 
      init_fuel: the initial fuel amount for the robot

    Return: the total number of vacuumed locations the robot sees
      while cleaning the room
    """
    # TODO: complete this function.
    # stop when:
    # It has depleted its fuel amount f.
    # It cannot move because all neighboring spaces have been previously visited.

    # move order:
    # Right neighbor
    # Up neighbor
    # Left neighbor
    # Down neighbor

    r, c = start_loc
    row_len = len(room) - 1
    col_len = len(room[0]) - 1
    vac_count = 0
    cleaned = set()
    moves = [(0, 1), (-1, 0), (0, -1), (1, 0)]

    while init_fuel > 0:
        if (r, c) not in cleaned:
            cleaned.add((r, c))
            if room[r][c] == "d":
                room[r][c] = "v"
                vac_count += 1
        
        has_moved = False
        for row_dir, col_dir in moves:
            new_row = r + row_dir
            new_col = c + col_dir
            move_row_in_bound = 0 <= new_row <= row_len
            move_col_in_bound = 0 <= new_col <= col_len

            if move_row_in_bound and move_col_in_bound and (new_row, new_col) not in cleaned:
                r = new_row
                c = new_col
                has_moved = True
                init_fuel -= 1
                break
        
        if not has_moved:
            break

    return vac_count

test_room = [
    ["d", "d", "v"],
    ["v", "d", "d"],
    ["d", "v", "d"]
]

start = (0, 0)
fuel = 10

print(clean_room(test_room, start, fuel))