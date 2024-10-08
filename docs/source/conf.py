# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys

# Add the path to your SDK source code
sys.path.insert(0, os.path.abspath('../../'))

project = 'CalculatorSDK'
copyright = '2024, Sandeep Shetty'
author = 'Sandeep Shetty'
release = '1.2'



# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'autoapi.extension',
]
autoapi_dirs = ['../../']  # Specify the directory where your SDK source code is located
autoapi_generate_api_docs = True
templates_path = ['_templates']
autoapi_ignore = ["*conf.py"]
exclude_patterns = []
# AutoAPI options to exclude certain members
autoapi_options = [
    "members",
    "undoc-members",            # Include undocumented members
    "show-inheritance",
    "special-members=False",    # Exclude special methods like __init__, __aenter__, etc.
    "private-members=False",    # Exclude private members (those starting with '_')
]

# Custom autodoc options
autodoc_default_options = {
    'members': True,                       # Include public members
    'undoc-members': False,                # Do not include undocumented members
    'private-members': False,              # Exclude members starting with '_'
    'special-members': False,              # Exclude special members (__init__, __aenter__, etc.)
    'exclude-members': '',  # Exclude specific members
}


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']
