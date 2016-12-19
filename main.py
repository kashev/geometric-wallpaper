#!/usr/bin/env python
# geometric-wallpaper
# Kashev Dalmia | @kashev | kashev.dalmia@gmail.com

import argparse

from PIL import Image, ImageDraw

import geowall as gw


four_k_size = (3840, 2160)
instagram_size = (500, 500)


def main():
    """ Create a geometric wallpaper. """
    parser = argparse.ArgumentParser(
        description="A program to generate geometric wallpaper.")

    parser.add_argument("-s", "--shape",
                        help="the name of shapes to generate",
                        type=str,
                        choices=("hexagon",
                                 "square",
                                 "diamond",
                                 "half-diamond"),
                        default="hexagon")

    parser.add_argument("-n", "--num-across",
                        help="the number of shapes across the canvas to create",
                        type=int,
                        default=10)

    parser.add_argument("--size",
                        help="the size of the created image",
                        type=int,
                        nargs=2,
                        default=instagram_size)

    parser.add_argument("-o", "--outfile",
                        help="name of the created file",
                        type=str)

    args = parser.parse_args()

    # Create the image.
    im = Image.new('RGB', args.size)
    draw = ImageDraw.Draw(im)

    for shape in gw.shapes.cover_in_shapes(args.shape, im.size,
                                           args.num_across):
        draw.polygon(shape, fill=gw.colors.palette_chooser())

    # Save the image.
    if args.outfile:
        im.save(args.outfile)
    else:
        im.save("{}_{}_{}x{}.png".format(args.shape, args.num_across,
                                         args.size[0], args.size[1]),
                "PNG")


if __name__ == '__main__':
    main()
