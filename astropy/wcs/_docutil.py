"""
astropy.wcs-specific utilities for generating boilerplate in docstrings.
"""

from __future__ import division  # confidence high


__all__ = ['TWO_OR_THREE_ARGS', 'RETURNS', 'ORIGIN', 'RA_DEC_ORDER']


def _fix(content, indent=0):
    lines = content.split('\n')
    indent = '\n' + ' ' * indent
    return indent.join(lines)


def TWO_OR_THREE_ARGS(naxis, indent=0):
    return _fix(
"""args : flexible
    Either two or three arguments may be provided.

        - 2 arguments: An *N* x *{0}* array of *x*- and
          *y*-coordinates, and an *origin*.

        - 3 arguments: 2 one-dimensional arrays of *x* and *y*
          coordinates, and an *origin*.

    Here, *origin* is the coordinate in the upper left corner of the
    image.  In FITS and Fortran standards, this is 1.  In Numpy and C
    standards this is 0.
""".format(naxis), indent)


def RETURNS(out_type, indent=0):
    return _fix("""result : array
    Returns the {0}.  If the input was a single array and
    origin, a single array is returned, otherwise a tuple of arrays is
    returned.""".format(out_type), indent)


def ORIGIN(indent=0):
    return _fix(
"""
origin : int
    Specifies the origin of pixel values.  The Fortran and FITS
    standards use an origin of 1.  Numpy and C use array indexing with
    origin at 0.
""", indent)


def RA_DEC_ORDER(indent=0):
    return _fix(
"""
ra_dec_order : bool, optional
    When `True` will ensure that sky coordinates are always given and
    returned in as (*ra*, *dec*) pairs, regardless of the order of the
    axes specified by the in the ``CTYPE`` keywords.
""", indent)
