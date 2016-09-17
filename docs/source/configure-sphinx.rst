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

Run the sphinx-quickstart script in the docs folder of the project to do the
one-time set-up for the project:

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


UNDER CONSTRUCTION
