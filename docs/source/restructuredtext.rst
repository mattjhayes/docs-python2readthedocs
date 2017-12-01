################
reStructuredText
################

There are a lot of guides on how reStructuredText works, and this is not a
substitute for them. It is just a brief sample of common formatting options
that work with Read the Docs for those in a hurry.

****************************
reStructuredText Conventions
****************************

Here are some basic pointers on how to create documentation pages in
reStructuredText.

Line length
===========

The length of a line in reStructuredText shouldn't be more than 79 characters

********
Headings
********

Headings are:

**
H1
**

A row of #'s above and below the line of text.
There should only one H1 in the document.
Example:

.. code-block:: text

  ###############
  Heading Level 1
  ###############

**
H2
**

A row of \*'s above and below the line of text.
Example:

.. code-block:: text

  ***************
  Heading Level 2
  ***************

**
H3
**

A row of ='s below the line of text.
Example:

.. code-block:: text

  Heading Level 3
  ===============

**
H4
**

A row of -'s below the line of text.
Example:

.. code-block:: text

  Heading Level 4
  ---------------

**
H5
**

A row of ^'s below the line of text.
Example:

.. code-block:: text

  Heading Level 5
  ^^^^^^^^^^^^^^^

**
H6
**

A row of "'s below the line of text.
Example:

.. code-block:: text

  Heading Level 6
  """""""""""""""

**********
Formatting
**********

Italics
=======

Surround word(s) with single *asterisks*:

.. code-block:: text

  *italics*

bold
====

Surround word(s) with double **asterisks**:

.. code-block:: text

  **bold**

literal
=======

Surroud word(s) with double backticks:

.. code-block:: text

  ``double back-quotes``

*****
Lists
*****

Lists must always be preceded by a blank line.

Numbered Lists
==============

Numbered lists are numbers or letters followed by ".", right bracket ")"
or surrounded by brackets "( )" 

.. code-block:: text

  This is a numbered list:
  
  1) Item 1
  2) Item 2
  
Displays as:

This is a numbered list:
  
1) Item 1
2) Item 2

Bullet Points
=============

Bullet point lines start with "-", "+" or "*"

.. code-block:: text

  This is a bullet point list:
  
  * Item 1
  * Item 2

Displays as:

This is a bullet point list:

* Item 1
* Item 2

***********
Code Blocks
***********

Use the code-block directive to display code as it appears, including
syntax highlighting if desired.

Command Line
============

Use this directive for text such as command line input and output
(note 2 space indent for the code):

.. code-block:: text

  .. code-block:: text

    code here...

Python
======

Use this directive for Python (note 2 space indent for the code):

.. code-block:: text

  .. code-block:: python

    code here...

**********
Hyperlinks
**********

Simple link
===========

(note the backticks, angle brackets and trailing underscore)

.. code-block:: text

  `<http://www.python.org/>`_

Link with name
==============

.. code-block:: text

  `Python <http://www.python.org/>`_

Link to local page
==================

.. code-block:: text

  `Local Page <local_page.html>`_

******
Images
******

.. code-block:: text

  .. image:: images/build1.png


