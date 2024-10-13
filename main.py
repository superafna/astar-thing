import numpy as np
from packages.a_star import a_star_search
from packages.grid_gen import grid_gen, point_gen


def test_random():
    """
    Randomly generate the parameters, and run a_star_search
    """
    grid = grid_gen()

    # Define the source and destination
    src = point_gen(grid)
    dest = point_gen(grid)

    print(src, dest)

    # Run the A* search algorithm
    a_star_search(grid, src, dest)


def test_fixed():
    """
    fixed test to check for strange behavior.
    """
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
    src = (8, 0)
    dest = (0, 0)

    # Run the A* search algorithm
    a_star_search(grid, src, dest)


def main():
    for _ in range(100):
        test_random()


if __name__ == "__main__":
    main()

"""
based on code from https://www.geeksforgeeks.org/a-search-algorithm-in-python/
"""
