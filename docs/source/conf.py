# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'reStructuredPython'
copyright = '2025, Rihaan Meher'
author = 'Rihaan Meher'
release = '0.4.0'
html_favicon = "_static/icon.png"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']

# Define the sidebars
#html_sidebars = {
#    '**': ['searchbox.html', 'globaltoc.html', 'relations.html', 'sourcelink.html'],
#}
