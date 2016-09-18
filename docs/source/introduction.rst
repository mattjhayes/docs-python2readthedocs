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
  including all the hassles of making it searchable etc.

- Docstrings from your Python code are automatically
  converted into nice looking documentation pages in ReadtheDocs.

This guide is built entirely from a Python project on GitHub, using the
techniques outlined here. The project on GitHub
(`<https://github.com/mattjhayes/docs-python2readthedocs>`_) can be used
as an example of the configuration. It uses a webhook for
auto-rebuild of Read the Docs pages on project commits.

A couple of simple Python programs
to demonstrate the autodoc functionality are included in the project.
