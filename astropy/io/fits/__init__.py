# Licensed under a 3-clause BSD style license - see PYFITS.rst

"""
A package for reading and writing FITS files and manipulating their
contents.

A module for reading and writing Flexible Image Transport System
(FITS) files.  This file format was endorsed by the International
Astronomical Union in 1999 and mandated by NASA as the standard format
for storing high energy astrophysics data.  For details of the FITS
standard, see the NASA/Science Office of Standards and Technology
publication, NOST 100-2.0.
"""

import os

from astropy import setup_helpers
if setup_helpers.is_in_build_mode():
    pass
else:
    from . import py3compat

    # Public API compatibility imports
    from . import card
    from . import column
    from . import convenience
    from . import hdu
    from .card import *
    from .column import *
    from .convenience import *
    from .fitsrec import FITS_record, FITS_rec
    from .hdu import *

    from .hdu.groups import GroupData
    from .hdu.hdulist import fitsopen as open
    from .hdu.image import Section
    from .hdu.table import new_table
    from .header import Header

    # Additional imports used by the documentation (some of which should be
    # restructured at some point)
    from .verify import VerifyError

    from ...config import ConfigurationItem

    # Set module-global boolean variables
    # TODO: Make it possible to set these variables via environment variables
    # again, once support for that is added to Astropy
    EXTENSION_NAME_CASE_SENSITIVE = ConfigurationItem(
        'extension_name_case_sensitive', False,
        'If True, extension names (i.e. the EXTNAME keyword) should be '
        'treated as case-sensitive.')

    USE_MEMMAP = ConfigurationItem(
        'use_memmap', True,
        'If True, use memory-mapped file access to read/write the data in '
        'FITS files. This generally provides better performance, especially '
        'for large files, but may affect performance in I/O-heavy '
        'applications.')

    ENABLE_RECORD_VALUED_KEYWORD_CARDS = ConfigurationItem(
        'enabled_record_valued_keyword_cards', True,
        'If True, enable support for record-valued keywords as described by '
        'FITS WCS Paper IV. Otherwise they are treated as normal keywords.')


    __all__ = (card.__all__ + column.__all__ + convenience.__all__ +
               hdu.__all__ +
               ['FITS_record', 'FITS_rec', 'GroupData', 'open', 'Section',
                'new_table', 'Header', 'VerifyError',
                'EXTENSION_NAME_CASE_SENSITIVE', 'USE_MEMMAP',
                'ENABLE_RECORD_VALUED_KEYWORD_CARDS'])
