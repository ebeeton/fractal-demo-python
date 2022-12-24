""" Scaling functions. """


def scale(val, minx, maxx, minscale, maxscale):
    """ Scales a value in one range to another. """

    # https://stackoverflow.com/a/5295202
    return (maxscale - minscale) * (val - minx) / maxx - minx + minscale
