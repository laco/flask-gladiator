
__version__ = "0.1"


def get_version():
    return __version__


def next_version():
    _v = __version__.split('.')
    _v[-1] = str(int(_v[-1]) + 1)
    return '.'.join(_v)
