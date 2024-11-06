import heapq
import numpy as np

from dataclasses import dataclass, field


DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0),
              (1, 1), (1, -1), (-1, 1), (-1, -1)]


@dataclass
class Cell:
    """
    used to store the information of cells.
    """
    parent:np.ndarray = field(default=np.array([0, 0]))
    final_f:float = float('inf')
    cost_g:float = float('inf')
    heuristic_h:int = 0


def is_valid(coordinates:tuple[int, int], size:tuple[int, int], ) -> bool:
    """
    Check if the coordinates are within the grid, by making sure both are within [0, size)
    :param coordinates: coordinates as a tuple of positive ints.
    :param size: size of grid as a tuple of positive ints.
    :return: the coordinates exist within the grid.
    """
    return 0 <= coordinates[0] < size[0] and \
           0 <= coordinates[1] < size[1]


def is_unblocked(grid:np.ndarray, cell:tuple[int, int]) -> bool:
    """
    Check if the cell is unblocked.
    :param grid: 2d grid as numpy ndarray, an unblocked cell is signified by 1.
    :param cell: coordinates of the cell as a tuple of positive ints.
    :return: The cell is unblocked.
    """
    return grid[cell] == 1


def is_destination(src:tuple[int, int], dest:tuple[int, int]) -> bool:
    """
    Checks if the cells are the same.
    :param src: coordinates of the source as a tuple of positive ints.
    :param dest: coordinates of the destination as a tuple of positive ints.
    :return: The cells share the same coordinates.
    """
    return src[0] == dest[0] and src[1] == dest[1]


def calculate_h_value(src:tuple[int, int], dest:tuple[int, int]) -> float:
    """
    Calculate the arithmetic distance to the destination cell
    :param src: coordinates of the source as a tuple of positive ints.
    :param dest: coordinates of the destination as a tuple of positive ints.
    :return: heuristic estimate.
    """
    return ((src[0] - dest[0]) ** 2 + (src[1] - dest[1]) ** 2) ** 0.5


def trace_path(cell_details:np.ndarray, dest:tuple[int, int]) -> None:
    """
    Trace the path from the destination cell back to the source, then print it.
    :param cell_details: ndarray that stores Cell-s.
    :param dest: coordinates of the destination cell, as a tuple of positive ints.
    """
    print("The Path is ")
    path = []
    coordinates = dest

    while not (cell_details[coordinates].parent[0] == coordinates[0] and cell_details[coordinates].parent[1] == coordinates[1]):
        # Loop until the cell has itself as it's parent, marking the source cell.
        # append the current cell to the path, then move on to the next parent.
        path.append(coordinates)
        temp_node = cell_details[coordinates].parent
        coordinates = temp_node

    path.append(coordinates)   # Add the source cell to the path
    path.reverse()  # Reverse the path to get the path from source to destination

    # Print the path
    for i in path:
        print("->", i, end=" ")
    print()


def a_star_search(grid:np.ndarray, src:tuple[int, int], dest:tuple[int, int]) -> None:
    """
    A* implementation, that calculates the shortest path between the source and destination cells
    within a 2d grid of blocked and unblocked cells, and prints out the cells that make it.
    :param grid: the grid, as a numpy array. 1 represents an unblocked cell.
    :param src: the coordinates of the source cell, as a positive tuple of ints.
    :param dest: the coordinates of the destination cell, as a positive tuple of ints.
    """
    shape = grid.shape
    row = shape[0]
    col = shape[1]

    size = (row, col)   # size of the grid.

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
    cell_details[src].final_f = 0
    cell_details[src].cost_g = 0
    cell_details[src].heuristic_h = 0
    cell_details[src].parent = src

    # Initialize the open list (cells to be visited) with the start cell
    open_list = []
    heapq.heappush(open_list, (0.0, src))

    # Initialize the flag for whether destination is found
    found_dest = False

    # Main loop of A* search algorithm
    while len(open_list) > 0:
        # Pop the cell with the smallest f value from the open list
        p = heapq.heappop(open_list)

        # Mark the cell as visited
        src = p[1]
        closed_list[src] = True

        # For each direction, check the successors
        for dirs in DIRECTIONS:
            # Calculate the successor using the current direction
            new_src = src[0] + dirs[0], src[1] + dirs[1]

            # If the successor is valid, unblocked, and not visited
            if is_valid(new_src, size) and is_unblocked(grid, new_src) and not closed_list[new_src]:
                # If the successor is the destination
                if is_destination(new_src, dest):
                    # Set the parent of the destination cell
                    cell_details[new_src].parent = src
                    print("The destination cell is found")

                    # Trace and print the path from source to destination
                    trace_path(cell_details, dest)
                    found_dest = True
                    break
                else:
                    # Calculate the new f, g, and h values
                    g_new = cell_details[src].cost_g + 1.0
                    h_new = calculate_h_value(new_src, dest)
                    f_new = g_new + h_new

                    # If the cell is not in the open list or the new f value is smaller
                    if cell_details[new_src].final_f == float('inf') or cell_details[new_src].final_f > f_new:
                        # Add the cell to the open list
                        heapq.heappush(open_list, (f_new, new_src))
                        # Update the cell details
                        cell_details[new_src].final_f = f_new
                        cell_details[new_src].cost_g = g_new
                        cell_details[new_src].heuristic_h = h_new
                        cell_details[new_src].parent = src

    # If the destination is not found after visiting all cells
    if not found_dest:
        print("Failed to find the destination cell")

