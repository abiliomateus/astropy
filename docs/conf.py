# -*- coding: utf-8 -*-
# Licensed under a 3-clause BSD style license - see LICENSE.rst
#
# Astropy documentation build configuration file, created by
# sphinx-quickstart on Tue Jul 26 02:59:34 2011.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import os
import sys

#some of the docs require the autodoc special-members option, in 1.1
needs_sphinx = '1.1'

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.abspath('..'))

# Load all of the global Astropy configuration
from astropy.sphinx.conf import *

# The intersphinx_mapping in astropy.sphinx.conf refers to astropy for
# the benefit of affiliated packages who want to refer to objeects in
# the astropy core.  However, we don't want to cyclically reference
# astropy in its own build so we remove it here.
del intersphinx_mapping['astropy']


# -- General configuration -----------------------------------------------------

# General information about the project.
project = u'Astropy'
copyright = u'2011, The Astropy Team, Erik Tollerud, Thomas Robitaille, and Perry Greenfield'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.

import astropy

# The short X.Y version.
version = astropy.__version__.split('-', 1)[0]
# The full version, including alpha/beta/rc tags.
release = astropy.__version__

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []


# -- Options for HTML output ---------------------------------------------------

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = 'logo/astropylogo.png'

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = 'astropyicon.ico'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static','logo/astropyicon.ico']

# Output file base name for HTML help builder.
htmlhelp_basename = 'Astropydoc'


# -- Options for LaTeX output --------------------------------------------------

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
  ('index', 'Astropy.tex', u'Astropy Documentation',
   u'Erik Tollerud, Thomas Robitaille, Perry Greenfield, and the Astropy Collaboration', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None


# -- Options for manual page output --------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'astropy', u'Astropy Documentation',
     [u'Erik Tollerud, Thomas Robitaille, Perry Greenfield, and the Astropy Collaboration'], 1)
]

# This is added to the end of RST files - a good place to put substitutions to
# be used globally.
rst_epilog += """
"""

# -- Options for linkcheck --------------------------------------------

# A timeout value, in seconds, for the linkcheck builder
linkcheck_timeout = 60
