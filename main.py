import numpy as np
from packages import a_star
from packages.grid_gen import grid_gen, point_gen


def main():
    # Define the grid (1 for unblocked, 0 for blocked)
    grid = grid_gen()

    # Define the source and destination
    src = point_gen(grid)
    dest = point_gen(grid)

    # Run the A* search algorithm
    a_star.a_star_search(grid, src, dest)


if __name__ == "__main__":
    for _ in range(1000):
        main()

"""
based on code from https://www.geeksforgeeks.org/a-search-algorithm-in-python/
"""
