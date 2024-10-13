import numpy as np
from random import randint


def grid_gen(row=randint(4, 40), col=randint(4, 40)) -> np.ndarray:
    grid = np.stack([[max(randint(0, 1), randint(0, 1), randint(0, 1)) for _ in range(col)] for _ in range(row)])
    return grid


def point_gen(grid:np.ndarray) -> tuple:
    shape = grid.shape
    row = shape[0]
    col = shape[1]

    return randint(0, row-1), randint(0, col-1)
