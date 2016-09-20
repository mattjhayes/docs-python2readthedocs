###############
Troubleshooting
###############

*******************
Static Page Problem
*******************

My page isnt' showing up in the contents menu
=============================================

If a page isn't displaying in the contents then check that it is correctly
listed in the index.rst file (check indent!)
`example <https://raw.githubusercontent.com/mattjhayes/docs-python2readthedocs/master/docs/source/index.rst>`_
.

My page doesn't load / display correctly
========================================

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

**********************************
Module files missing or incomplete
**********************************

Check Read the Docs to see if there has been an import problem as per
`example-of-import-problem <readthedocs.html#example-of-import-problem>`_


