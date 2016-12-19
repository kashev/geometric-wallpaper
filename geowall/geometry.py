#!/usr/bin/env python
# geometric-wallpaper
# Kashev Dalmia | @kashev | kashev.dalmia@gmail.com

import math

def middle(shape):
    """ Given the 2D vertices of a shape, return the coordinates of the middle
        of the shape.
    """
    return (sum(p[0] for p in shape) / len(shape),
            sum(p[1] for p in shape) / len(shape))


def hex_corner(center, size, i, pointy=True):
    """ Given a center, and a size, and a number, return the 2D coordinates of
        that vertex of a hexagon.

        Reference: http://www.redblobgames.com/grids/hexagons/
    """
    angle_deg = 60 * i  + (30 * pointy)
    angle_rad = math.pi / 180 * angle_deg
    return (center[0] + size * math.cos(angle_rad),
            center[1] + size * math.sin(angle_rad))
