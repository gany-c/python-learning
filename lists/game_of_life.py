"""
The Problem: Game of Life
Goal: Given an $M \times N$ grid of cells, where each cell is either 1 (live) or 0 (dead), update the board to its next state based on these four rules:
- Underpopulation: Any live cell with fewer than 2 live neighbors dies.
- Survival: Any live cell with 2 or 3 live neighbors lives on.
- Overpopulation: Any live cell with more than 3 live neighbors dies.
- Reproduction: Any dead cell with exactly 3 live neighbors becomes a live cell.

Requirement: The transitions happen simultaneously. You can't update a cell and then use its new value to calculate its neighbor's status.
Example
Input:
[0,1,0]
[0,0,1]
[1,1,1]
[0,0,0]

Output:
[0,0,0]
[1,0,1]
[0,1,1]
[0,1,0]


APPROACH 1:
1. Input - > copy it to a state grid
2. Update each cell of the input based on the state m by n loop
    check for underpopulation etc, all 4 conditions
3. return output

Approach 2: Optimization

1. we keep track of only the neighbors in the state.
2. We have to some how keep track of the older values as the state moves

:

map-old - <x,y> key => <old-value> pre-updated value

every time I move the pointer, I do a clean up of the map
The cleanup, will remove what is unnecessary for the current computation.

suppose I'm doing the computation for 3,4 = the earliest value I'll need will be 2,3.
whatever falls to the left or top of that, which will be max 1 cell away, I remove that from the map

clean_up(x, y):
  remove (x-2, y-1)

FINAL APPROACH - encoding based, implemented below:

  2 as formerly 0 and currently 1
  3 as formerly 1 and now 0


  and once the entire computation is done, change all 2s to 1
  andll 3s to 0

"""

_sum_neighbors_by_types(input: list[list[int]], neighbors: list[(int, int)]) -> (int, int):
    """
    0 and 2 - 0 sum
    1 and 3 - 1 sum
    """
    pass

def _filter_by_dimensions(list_of_neighbors, x, y, m, n) -> list[(int, int)]:
    """
    filter the indexes that are out of bounds
    """
    pass


def _get_num_of_neighbors(input: list[list[int]], x: int, y: int) -> (int, int):

    list_of_neighbors = [(x-1, y-1), (x, y-1), (x+1, y-1), (x-1, y), (x +1, y), (x -1, y+1), (x, y+1), (x +1, y +1)]
    _filter_by_dimensions(list_of_neighbors, x, y, m, n)
    num_dead, num_alive = _sum_neighbors_by_types(input, list_of_neighbors)




def game_of_life(input: list[list[int]]) -> list[list[int]]:

    for row in input:
        for i in row:
            _get_num_of_neighbors()
            check for all 4 conditions





if __name__ == '__main__':
    input_matrix = [
        [0, 0, 1],
        [0, 1, 0],
        [1, 0, 0]
    ]

    game_of_life(input_matrix)
