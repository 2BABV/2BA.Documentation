# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = '2BA.SphinxDemo'
copyright = '2024, TTT'
author = 'Quincy Tromp'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx_rtd_theme']

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

import sphinx_rtd_theme

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']


html_context = {
    'theme_logo_only': True,
    'theme_display_version': True,
}

html_logo = "_static/logo.svg"
html_favicon = "_static/favicon.ico"

httpexample_scheme = 'https'

autosectionlabel_prefix_document = True