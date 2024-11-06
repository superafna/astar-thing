import numpy as np
from random import randint


def grid_gen(row=randint(50, 100), col=randint(50, 100)) -> np.ndarray:
    """
    Generate a two-dimensional numpy array of the specified size, filled randomly with 1's and 0's.
    Parameters are random, if not specified.
    :param row: number of rows in grid.
    :param col: number of columns in grid.
    :return: numpy ndarray of grid.
    """
    grid = np.stack([[max(randint(0, 1), randint(0, 1), randint(0, 1)) for _ in range(col)] for _ in range(row)])
    return grid


def point_gen(grid:np.ndarray) -> tuple[int, int]:
    """
    Randomly generate a point within a 2d grid.
    :param grid: used to check the limits of the grid.
    :return: coordinates as tuple of ints.
    """
    shape = grid.shape
    row = shape[0]
    col = shape[1]

    return randint(0, row-1), randint(0, col-1)


def true_point_gen() -> tuple[int, int]:
    """
    Randomly generate a point with 2 coordinates.
    :return: coordinates as tuple of ints between 0 and 99.
    """

    return randint(0, 99), randint(0, 99)
