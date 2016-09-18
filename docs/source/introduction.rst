############
Introduction
############

This guide is for anyone who has a Python project and wants to improve
their documentation by integrating it with ReadtheDocs.

There are a number of advantages to having your project documentation
included in your project file structure and written in reStructuredText:

- Your documentation is specific to your code version. Add a new feature in
  your develop branch, update the documentation page, commit, update develop
  on GitHub and within a short amount of time the documentation for the
  develop branch has been updated on ReadtheDocs, but critically, master
  branch on ReadtheDocs still shows the previous documentation.

- You don't have to worry about hosting a website for the documentation,
  including all the hastles of making it searchable etc.

- The docstrings that you write in your Python code are automatically
  converted into nice documentation pages in ReadtheDocs.

