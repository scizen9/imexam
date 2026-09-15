# Licensed under a 3-clause BSD style license - see LICENSE.rst
try:
    _ASTROPY_SETUP_
except NameError:
    import builtins
    builtins._ASTROPY_SETUP_ = False

try:
    from .version import version as __version__
except ImportError:
    __version__ = ''

try:
    from .version import githash as __githash__
except ImportError:
    __githash__ = ''

__all__ = ['__version__', '__githash__']