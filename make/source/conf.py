# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Langscore'
copyright = '2023, BreezeSinfonia'
author = 'BreezeSinfonia'
release = '0.8.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.mathjax', 'sphinx.ext.todo', 'sphinx.ext.githubpages']

templates_path = ['_templates']
exclude_patterns = []

language = 'ja'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'nature'
html_static_path = ['_static']
html_css_files = ['custom.css']

html_build_dir = '.'

html_sidebars = {
   '**': ['globaltoc.html', 'relations.html', 'searchbox.html']
}
