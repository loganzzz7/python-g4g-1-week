from tile import Tile


def sum_tiles(matrix: list[list[int]], tiles: list[Tile]) -> int:
    """
    Return the sum of the tile values.

    Inputs:
      matrix: the matrix of values
      tiles: a list of Tiles.

    Return: the sum of the tile values.
    """
    # TODO: complete this function.
    sum_of_tile = 0
    matrix_r = len(matrix) - 1
    matrix_c = len(matrix[0]) - 1

    for tile in tiles:
        for row in range(tile.r0, tile.r1 + 1):
            for col in range(tile.c0, tile.c1 + 1):
                if row > matrix_r or col > matrix_c:
                    tile_val = 0
                else:
                    tile_val = matrix[row][col]
                sum_of_tile = sum_of_tile + tile_val
    return sum_of_tile

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9,10,11,12]
]

tiles = [
    Tile(0, 0, 0, 0),
    Tile(0, 0, 1, 1),
    Tile(0, 0, 2, 2),
]

print(sum_tiles(matrix, tiles))