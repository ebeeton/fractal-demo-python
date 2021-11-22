""" Scaling functions. """

def scale(x, minx, maxx, minscale, maxscale):
    """ Scales a value in one range to another. """ 

    # https://stackoverflow.com/a/5295202
    return (maxscale - minscale) * (x - minx) / maxx - minx + minscale
