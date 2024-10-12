import heapq
import numpy as np

from dataclasses import dataclass, field
from itertools import count

# a global
TIEBREAKER = count()

@dataclass
class Cell:

    parent:np.ndarray = field(default=np.array([0, 0]))
    f:float = float('inf')
    g:float = float('inf')
    h:int = 0


def is_valid(coords:np.ndarray, size:np.ndarray) -> bool:
    return np.all(coords >= 0) and (coords < size).all()


def is_unblocked(grid:np.ndarray, coords:np.ndarray) -> bool:
    return grid[tuple(coords)] == 1


def is_destination(start:np.ndarray, dest:np.ndarray) -> bool:
    return (start == dest).all()


def calculate_h_value(coords:np.ndarray, dest:np.ndarray) -> bool:
    return ((coords[0] - dest[0]) ** 2 + (coords[1] - dest[1]) ** 2) ** 0.5


def trace_path(cell_details:np.ndarray, dest:np.ndarray):
    print("The Path is ")
    path = []
    node = dest

    # Trace the path from destination to source using parent cells
    while not (cell_details[tuple(node)].parent == node).all():
        path.append(node)
        temp_node = cell_details[tuple(node)].parent
        node = temp_node

    # Add the source cell to the path
    path.append(node)
    # Reverse the path to get the path from source to destination
    path.reverse()

    # Print the path
    for i in path:
        print("->", i, end=" ")
    print()

# Implement the A* search algorithm


def a_star_search(grid:np.ndarray, src:np.ndarray, dest:np.ndarray):
    shape = grid.shape
    row = shape[0]
    col = shape[1]

    size = np.array([row, col])

    # Check if the source and destination are valid
    if not is_valid(src, size) or not is_valid(dest, size):
        print("Source or destination is invalid")
        return

    # Check if the source and destination are unblocked
    if not is_unblocked(grid, src) or not is_unblocked(grid, dest):
        print("Source or the destination is blocked")
        return

    # Check if we are already at the destination
    if is_destination(src, dest):
        print("We are already at the destination")
        return

    # Initialize the closed list (visited cells)
    closed_list = np.stack([[False for _ in range(col)] for _ in range(row)])
    # Initialize the details of each cell
    cell_details = np.stack([[Cell() for _ in range(col)] for _ in range(row)])

    # Initialize the start cell details
    cell_details[tuple(src)].f = 0
    cell_details[tuple(src)].g = 0
    cell_details[tuple(src)].h = 0
    cell_details[tuple(src)].parent = src

    # Initialize the open list (cells to be visited) with the start cell
    open_list = []
    heapq.heappush(open_list, (0.0, 0, src))

    # Initialize the flag for whether destination is found
    found_dest = False

    # Main loop of A* search algorithm
    while len(open_list) > 0:
        # Pop the cell with the smallest f value from the open list
        p = heapq.heappop(open_list)

        # Mark the cell as visited
        src = p[2]
        closed_list[tuple(src)] = True

        # For each direction, check the successors
        directions = np.stack([(0, 1), (0, -1), (1, 0), (-1, 0),
                      (1, 1), (1, -1), (-1, 1), (-1, -1)])

        for dir in directions:

            new_src = src + dir


            # If the successor is valid, unblocked, and not visited
            if is_valid(new_src, size) and is_unblocked(grid, new_src) and not closed_list[tuple(new_src)]:
                # If the successor is the destination
                if is_destination(new_src, dest):
                    # Set the parent of the destination cell
                    cell_details[tuple(new_src)].parent = src
                    print("The destination cell is found")
                    # Trace and print the path from source to destination
                    trace_path(cell_details, dest)
                    found_dest = True
                    return
                else:
                    # Calculate the new f, g, and h values
                    g_new = cell_details[tuple(src)].g + 1.0
                    h_new = calculate_h_value(new_src, dest)
                    f_new = g_new + h_new

                    # If the cell is not in the open list or the new f value is smaller
                    if cell_details[tuple(new_src)].f == float('inf') or cell_details[tuple(new_src)].f > f_new:
                        # Add the cell to the open list
                        heapq.heappush(open_list, (f_new, next(TIEBREAKER), new_src))
                        # Update the cell details
                        cell_details[tuple(new_src)].f = f_new
                        cell_details[tuple(new_src)].g = g_new
                        cell_details[tuple(new_src)].h = h_new
                        cell_details[tuple(new_src)].parent = src

    # If the destination is not found after visiting all cells
    if not found_dest:
        print("Failed to find the destination cell")

