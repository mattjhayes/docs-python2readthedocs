############
Introduction
############

This guide is for anyone who has a Python project and wants to improve
their documentation by integrating it with ReadtheDocs.

There are a number of advantages to having your project documentation on
Read the Docs, generated from reStructuredText files stored in your project
file structure:

- Your documentation is specific to your code version. Add a new feature in
  your develop branch, update the documentation page, commit, update develop
  on GitHub and within a short amount of time the documentation for the
  develop branch has been updated on ReadtheDocs, but critically, master
  branch on ReadtheDocs still shows the previous documentation.

- You don't have to worry about hosting a website for the documentation,
  including all the hastles of making it searchable etc.

- Docstrings from your Python code are automatically
  converted into nice looking documentation pages in ReadtheDocs.

This guide is generated using the principles outlined here. It is a
project on GitHub (`<https://github.com/mattjhayes/docs-python2readthedocs>`_)
and has a webhook for auto-rebuild of Read the Docs pages on project commits.

The project on which the guide is built also has some simple Python programs
to demonstrate the autodoc functionality.
