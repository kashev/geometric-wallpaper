#!/usr/bin/env python
# geometric-wallpaper
# Kashev Dalmia | @kashev | kashev.dalmia@gmail.com

import math


def cover_in_squares(canvas_size, num_across):
    """ Given a canvas_size, and a number of squares used to cover the major
        axis, yield tuples of coordinates of the verticies of a tiling which
        covers the whole canvas in squares.
    """
    canvas_x = canvas_size[0]
    canvas_y = canvas_size[1]

    canvas_max = max(canvas_x, canvas_y)

    side_length = canvas_max / num_across

    for row in range(num_across):
        for col in range(num_across):
            x = (canvas_max / num_across) * col
            y = (canvas_max / num_across) * row
            top_left = (x, y)
            top_right = (x + side_length, y)
            bottom_right = (x + side_length, y + side_length)
            bottom_left = (x, y + side_length)

            yield (top_left, top_right, bottom_right, bottom_left)


def cover_in_diamonds(canvas_size, num_across):
    canvas_x = canvas_size[0]
    canvas_y = canvas_size[1]

    canvas_max = max(canvas_x, canvas_y)

    half_diag_length = ((canvas_max / num_across) / 2)

    for row in range((2 * num_across) + 1):
        for col in range(num_across + 1):
                y = (canvas_max / (2 * num_across)) * row

                x = (canvas_max / num_across) * col
                if row % 2 != 0:
                    x += half_diag_length

                top = (x, y - half_diag_length)
                right = (x + half_diag_length, y)
                bottom = (x, y + half_diag_length)
                left = (x - half_diag_length, y)

                yield (top, right, bottom, left)

def cover_in_half_diamonds(canvas_size, num_across):
    for diamond in cover_in_diamonds(canvas_size, num_across):
        top, right, bottom, left = diamond
        yield (top, right, bottom)
        yield (bottom, left, top)


def cover_in_hexagons(canvas_size, num_across):
    """ Given a canvas_size, and a number of hexagons used to cover the major
        axis, yield tuples of coordinates of the verticies of a tiling which
        covers the whole canvas in hexagons.
    """
    # Reference: http://www.redblobgames.com/grids/hexagons/
    from . import geometry

    canvas_x = canvas_size[0]
    canvas_y = canvas_size[1]

    canvas_max = max(canvas_x, canvas_y)

    hex_width = canvas_max / num_across
    hex_size = hex_width / math.sqrt(3)
    hex_height = hex_size * 2
    num_down = int(canvas_max / (hex_size * (3 / 2) )) + 1

    for row in range(num_down + 1):
        for col in range(num_across + 1):
            y = (canvas_max / num_down) * row

            x = (canvas_max / num_across) * col
            if row % 2 != 0:
                x += (hex_width / 2)

            center = (x, y)

            yield list(geometry.hex_corner(center, hex_size, i)
                       for i in range(6))


def cover_in_shapes(shape, canvas_size, num_across):
    """ Given a shape string, yield from a generator which covers the
        canvas_size in the given shape.
    """
    if shape == "square":
        yield from cover_in_squares(canvas_size, num_across)
    elif shape == "diamond":
        yield from cover_in_diamonds(canvas_size, num_across)
    elif shape == "half-diamond":
        yield from cover_in_half_diamonds(canvas_size, num_across)
    elif shape == "hexagon":
        yield from cover_in_hexagons(canvas_size, num_across)
    else:
        raise "Unsupported shape!"
