##############
Create Content
##############

You should consider creating project documentation in
addition to the auto-generated module documentation. While, it's good surfacing
your docstrings as nicely formatted pages, you should still have some
general pages that introduce your project and add extra context such
as diagrams.

******************
Updating the Index
******************

The file docs/source/index.rst is the landing page for your projects
documentation.

Initially it will look something like this:

.. code-block:: text

  Welcome to <PROJECT_NAME>'s documentation!
  =======================================================

  Contents:

  .. toctree::
     :maxdepth: 2

  Indices and tables
  ==================

  * :ref:`genindex`
  * :ref:`modindex`
  * :ref:`search`

The rst files for autodoc are in the docs/source directory so it is a good
idea for reasons of tidiness and to avoid name collisions to create a
subdirectory for your content.

In this example, there is a subdirectory called *userguide*

Add the names of your additional RST files, without file extension, one line
below the ':maxdepth: 2'. Prefix with the subdirectory if using, example:

.. code-block:: text

      userguide/introduction

Be sure to preserve the 3-space indent.

See:
`Example <https://raw.githubusercontent.com/mattjhayes/docs-python2readthedocs/master/docs/source/index.rst>`_
