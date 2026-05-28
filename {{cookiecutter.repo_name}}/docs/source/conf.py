import os
import sys

sys.path.insert(0, os.path.abspath("../src"))

project = '{{cookiecutter.repo_name | replace("-", " ") | title}}'
copyright = "2024, {{cookiecutter.full_name}}"
author = "{{cookiecutter.full_name}}"
release = "{{cookiecutter.version}}"


# ---

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

current_directory = os.path.dirname(__file__)

# Autodoc extension needs to know where the modules are
sys.path.insert(0, os.path.join(current_directory, "../../src"))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = '{{cookiecutter.repo_name | replace("-", " ") | title}}'
copyright = "2026, {{cookiecutter.full_name}}"
author = "{{cookiecutter.full_name}}"
release = "{{cookiecutter.version}}"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
]

templates_path = ["_templates"]
exclude_patterns = ["Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
