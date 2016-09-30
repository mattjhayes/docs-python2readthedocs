###############
Troubleshooting
###############

********************
Static Page Problems
********************

Why isn't my page showing up in the contents menu?
==================================================

Check that you page is correctly
listed in the index.rst file (check indent!)
`example <https://raw.githubusercontent.com/mattjhayes/docs-python2readthedocs/master/docs/source/index.rst>`_
.

Check that you're looking at the right branch in Read the Docs

Why isn't my page loading / display correctly?
==============================================

Check the source reStructuredText file for issues with rstcheck.

Install rstcheck (if you don't already have it) to check syntax of rst code:

.. code-block:: text

  sudo pip install rstcheck

Run it against a particular file:

.. code-block:: text

  rstcheck <file>

Or run it against all reStructuredText files in a directory:

.. code-block:: text

  rstcheck *.rst

The reStructuredText is good if no results are returned.

****************
Autodoc Problems
****************

Module files missing or incomplete
==================================

Check Read the Docs to see if there has been an import problem as per
`example-of-import-problem <readthedocs.html#example-of-import-problem>`_

If your code has submodules (i.e. code is in more than one level of directory)
then you may need to
`alter your path statement <code-doc.html#submodules>`_.

