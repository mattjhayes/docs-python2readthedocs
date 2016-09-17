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



UNDER CONSTRUCTION
