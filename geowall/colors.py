#!/usr/bin/env python
# geometric-wallpaper
# Kashev Dalmia | @kashev | kashev.dalmia@gmail.com

import itertools
import random

hexagon_palette = (
    ( 24, 103, 133),  # Dark Blue
    (103,  86, 138),  # Dark Purple
    (143,  86, 131),  # Light Purple
    (242, 106, 120),  # Dark Orange
    (252, 151, 109),  # Light Orange
    (252, 151, 109),  # Light Orange
    (244, 289,  99),  # Orangish Yellow
    ( 74, 221, 211),  # Teal
    ( 28, 175, 253),  # Light Blue
)


def palette_chooser(colors=hexagon_palette):
    return random.choice(colors)

def random_color():
    """ Returns a random RGB color. """
    return (int(255 * random.random()),
            int(255 * random.random()),
            int(255 * random.random()))
