###############
Troubleshooting
###############

*******************
Static Page Problem
*******************

If a page isn't displaying in the contents then check that it is correctly
listed in the index.rst file (check indent!).

If a static page (i.e. not one that auto-generates content) is missing or
displaying incorrectly then start by checking the source
reStructuredText file for issues.

Install rstcheck (if you don't already have it) to check syntax of rst code:

.. code-block:: text

  sudo pip install rstcheck

Run it against a particular file:

.. code-block:: text

  rstcheck <file>

Or run it against all reStructuredText files in a directory:

.. code-block:: text

  rstcheck <file>

The reStructuredText is good if no results are returned.

**********************************
Module files missing or incomplete
**********************************

Check Read the Docs to see if there has been an import problem as per
`example-of-import-problem <readthedocs.html#example-of-import-problem>`_


