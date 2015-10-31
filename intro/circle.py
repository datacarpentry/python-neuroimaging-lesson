"""
circle.py

This is what it does

"""

import numpy as np

FACTOR = 1000. 


def area(r):
    return np.pi * (r ** 2)


def circumference(r):
    return np.pi * 2 * r


class Circle():

