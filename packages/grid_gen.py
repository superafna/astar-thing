import numpy as np
from random import randint


def grid_gen(row=randint(4, 40), col=randint(4, 40)) -> np.ndarray:
    grid = np.stack([[randint(0, 1) for _ in range(col)] for _ in range(row)])
    return grid


def point_gen(grid:np.ndarray) -> ((int, int), (int, int)):
    shape = grid.shape
    row = shape[0]
    col = shape[1]

    point_a = (randint(0, row-1), randint(0, col-1))
    point_b =(randint(0, row-1), randint(0, col-1))

    while point_a != point_b:
        point_b = (randint(0, row - 1), randint(0, col - 1))

    return point_a, point_b
