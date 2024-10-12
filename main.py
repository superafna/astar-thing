import numpy as np
from packages import a_star


def main():
    # Define the grid (1 for unblocked, 0 for blocked)
    grid = np.stack([
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 0, 1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
        [0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
        [1, 0, 1, 1, 1, 1, 0, 1, 0, 0],
        [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 0, 0, 0, 1, 0, 0, 1]
    ])

    # Define the source and destination
    src = np.array([8, 0])
    dest = np.array([0, 0])

    # Run the A* search algorithm
    a_star.a_star_search(grid, src, dest)


if __name__ == "__main__":
    main()

"""
based on code from https://www.geeksforgeeks.org/a-search-algorithm-in-python/
"""
