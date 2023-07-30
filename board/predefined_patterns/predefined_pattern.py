import random

block = [
    [True, True],
    [True, True]
]

beehive = [
    [False, True, True, False],
    [True, False, False, True],
    [False, True, True, False]
]

loaf = [
    [False, True, True, False],
    [True, False, False, True],
    [False, True, False, True],
    [False, False, True, False]
]

boat = [
    [True, True, False],
    [True, False, True],
    [False, True, False]
]

blinker = [
    [True, True, True]
]

toad = [
    [False, True, True, True],
    [True, True, True, False]
]

beacon = [
    [True, True, False, False],
    [True, True, False, False],
    [False, False, True, True],
    [False, False, True, True]
]


pulsar = [
    [False, False, True, True, True, False, False, False, True, True, True, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False, False],
    [True, False, False, False, False, True, False, True, False, False, False, False, True],
    [True, False, False, False, False, True, False, True, False, False, False, False, True],
    [True, False, False, False, False, True, False, True, False, False, False, False, True],
    [False, False, True, True, True, False, False, False, True, True, True, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, True, True, True, False, False, False, True, True, True, False, False],
    [True, False, False, False, False, True, False, True, False, False, False, False, True],
    [True, False, False, False, False, True, False, True, False, False, False, False, True],
    [True, False, False, False, False, True, False, True, False, False, False, False, True],
    [False, False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, True, True, True, False, False, False, True, True, True, False, False]
]

glider = [
    [False, True, False],
    [False, False, True],
    [True, True, True]
]

lwss = [
    [False, True, True, True, True],
    [True, False, False, False, True],
    [False, False, False, False, True],
    [True, False, False, True, False]
]

gosper_glider_gun = [
    [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, True, True, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, True, False, False, True, False, False, False, False, False, False],
    [False, False, False, False, False, False, True, False, True, True, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
]

def create_random_pattern(rows, cols):
    pattern = [[random.choice([True, False]) for _ in range(cols)] for _ in range(rows)]
    return pattern
