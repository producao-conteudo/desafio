"""Configuration file for the Sphinx documentation builder."""

# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

from pathlib import Path
from sys import path

# -- Path setup --------------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent.parent

path.append(str(BASE_DIR / 'source'))


# -- Project information -----------------------------------------------------

project = 'insights'
copyright = '2022, Gabriel Farias Caccaos'  # noqa: VNE003
author = 'Gabriel Farias Caccaos'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.intersphinx',
    'sphinx.ext.inheritance_diagram',
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'furo'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = []


# -- Other options -----------------------------------------------------------

nitpicky = True

intersphinx_mapping = {'python': ('https://docs.python.org/3', None)}

inheritance_graph_attrs = {
    'rankdir': 'TB',
}

inheritance_node_attrs = {'color': 'darkgray'}

inheritance_edge_attrs = {'color': 'darkgray'}
