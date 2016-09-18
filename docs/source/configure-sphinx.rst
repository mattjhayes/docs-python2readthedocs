################
Configure Sphinx
################

This guide is for configuring Sphinx on Ubuntu.

In the root directory of your project (replace <PROJECT_NAME> where needed),
create a folder for the documentation (if it doesn't already exist)
called docs:

.. code-block:: text

  cd
  cd <PROJECT_NAME>
  mkdir docs
  cd docs

*****************
sphinx-quickstart
*****************

The sphinx-quickstart script does a one-time set-up for the project. If you
haven't already configured Sphinx for the project then run it with:

.. code-block:: text

  sphinx-quickstart

Accept the default for root path:

.. code-block:: text

  Enter the root path for documentation.
  > Root path for the documentation [.]:

Override the default to have separate source and build directories:

.. code-block:: text

  You have two options for placing the build directory for Sphinx output.
  Either, you use a directory "_build" within the root path, or you separate
  "source" and "build" directories within the root path.
  > Separate source and build directories (y/n) [n]: y

Accept the default for name prefix:

.. code-block:: text

  > Name prefix for templates and static dir [_]:

Enter the name of your project, and your name:

.. code-block:: text

  The project name will occur in several places in the built documentation.
  > Project name: <PROJECT_NAME>
  > Author name(s): <AUTHOR_NAME>

Enter version and release numbers for the project:

.. code-block:: text

  Sphinx has the notion of a "version" and a "release" for the
  software. Each version can have multiple releases. For example, for
  Python the version is something like 2.5 or 3.0, while the release is
  something like 2.5.1 or 3.0a1.  If you don't need this dual structure,
  just set both to the same value.
  > Project version: <X.Y>
  > Project release [0.2]: <X.Y.Z>

Choose language (English is default):

.. code-block:: text

  > Project language [en]:

You need to make a decision about the file suffix for your restructuredText.
ReadtheDocs recommend using .txt extension
(see: `<http://documentation-style-guide-sphinx.readthedocs.io/>`_ ), however
I personally prefer to use the .rst extension so that it is clear what
format the files are in. Your choice:

.. code-block:: text

  The file name suffix for source files. Commonly, this is either ".txt"
  or ".rst".  Only files with this suffix are considered documents.
  > Source file suffix [.rst]:

Accept the default for epub:

.. code-block:: text

  Sphinx can also add configuration for epub output:
  > Do you want to use the epub builder (y/n) [n]:

Choose to enable autodoc if you have Python code to auto-document:

.. code-block:: text

  Please indicate if you want to use one of the following Sphinx extensions:
  > autodoc: automatically insert docstrings from modules (y/n) [n]: y

Accept defaults, apart from Windows (unless you need it):

.. code-block:: text

  > doctest: automatically test code snippets in doctest blocks (y/n) [n]:
  > intersphinx: link between Sphinx documentation of different projects (y/n) [n]:
  > todo: write "todo" entries that can be shown or hidden on build (y/n) [n]:
  > coverage: checks for documentation coverage (y/n) [n]:
  > imgmath: include math, rendered as PNG or SVG images (y/n) [n]:
  > mathjax: include math, rendered in the browser by MathJax (y/n) [n]:
  > ifconfig: conditional inclusion of content based on config values (y/n) [n]:
  > viewcode: include links to the source code of documented Python objects (y/n) [n]:
  > githubpages: create .nojekyll file to publish the document on GitHub pages (y/n) [n]:

  A Makefile and a Windows command file can be generated for you so that you
  only have to run e.g. `make html' instead of invoking sphinx-build
  directly.
  > Create Makefile? (y/n) [y]:
  > Create Windows command file? (y/n) [y]: n

Output:

  Creating file ./source/conf.py.
  Creating file ./source/index.rst.
  Creating file ./Makefile.

  Finished: An initial directory structure has been created.

  You should now populate your master file ./source/index.rst and create
  other documentation source files. Use the Makefile to build the docs,
  like so:
  make builder
  where "builder" is one of the supported builders, e.g. html, latex or
  linkcheck.

The initial configuration of Sphinx is now complete, keep reading as there are
more tasks that still need to be done.

*************
Look and Feel
*************

Themes
------

TBD

Sidebar
-------
The local site sidebar is a bit limited, however works
fine in Read the Docs. If you want a better sidebar for the local build then
try this update. Edit the docs/source/conf.py file. Find this stanza:

.. code-block:: text

  # Custom sidebar templates, maps document names to template names.
  #
  # html_sidebars = {}

Replace the last line of this stanza so it reads:

.. code-block:: text

  # Custom sidebar templates, maps document names to template names.
  #
  html_sidebars = { '**': ['globaltoc.html', 'relations.html', 'sourcelink.html', 'searchbox.html'], }

