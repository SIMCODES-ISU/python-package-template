import os
import sys
sys.path.insert(0, os.path.abspath('../src'))

project = '{{cookiecutter.repo_name | replace("-", " ") | title}}'
copyright = '2024, {{cookiecutter.full_name}}'
author = '{{cookiecutter.full_name}}'
release = '{{cookiecutter.version}}'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon'
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']