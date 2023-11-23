import copy
import numpy as np


def normalize_helper(gesture, x_extrema, y_extrema):
    gesture[:, 0] = (gesture[:, 0] - x_extrema[0]) / (x_extrema[1] - x_extrema[0])
    gesture[:, 1] = (gesture[:, 1] - y_extrema[0]) / (y_extrema[1] - y_extrema[0])


def normalize(gesture1, gesture2):
    g1 = copy.deepcopy(gesture1)
    g2 = copy.deepcopy(gesture2)

    normalize_helper(g1, [np.min(g1[:, 0]), np.max(g1[:, 0])],
                         [np.min(g1[:, 1]), np.max(g1[:, 1])])
    normalize_helper(g2, [np.min(g2[:, 0]), np.max(g2[:, 0])],
                         [np.min(g2[:, 1]), np.max(g2[:, 1])])

    return g1, g2


def process(gesture):
    for i in range(len(gesture) - 1, -1, -1):
        gesture[i] -= gesture[0]
