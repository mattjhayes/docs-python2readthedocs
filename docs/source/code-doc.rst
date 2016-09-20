#################
Autodoc Your Code
#################

The Sphinx autodoc extension
(see `<http://www.sphinx-doc.org/en/stable/ext/autodoc.html>`_ )
converts docstrings
from your code into the final documentation format at Sphinx build-time.

This is very useful, but may not work out of the box.

**********************************
Tell autodoc how to Find your Code
**********************************
Autodoc probably can't find your code without a little help. Edit the
docs/source/conf.py file. Uncomment:

.. code-block:: python

  import os
  import sys

Uncomment and edit this line (adjust path as appropriate):

.. code-block:: python

  sys.path.insert(0, os.path.abspath('../../<PROJECT_NAME>'))

********************************
reStructuredText file directives
********************************

The reStructuredText files in your docs/source directory do not contain
the docstrings. Instead they just contain directives on how to build the
resulting page.

You need reStructuredText files with directives to build
the documentation from particular Python modules in your project. Example:

.. code-block:: text

  example_module module
  =====================

  .. automodule:: example_module
      :members:
      :undoc-members:
      :show-inheritance:

Example from this project (reStructuredText, Python and auto-generated HTML):

  `example_module.rst <https://raw.githubusercontent.com/mattjhayes/docs-python2readthedocs/master/docs/source/example_module.rst>`_

  `example_module.py <https://github.com/mattjhayes/docs-python2readthedocs/blob/master/docs-python2readthedocs/example_module.py>`_

  `example_module.html <example_module.html>`_

There is a script that you can run to create a directive file per Python
module. You should only run this command once to set up the \*.rst files.

In the docs directory, run this command to create rst files that document
your python modules (Note that the -f option tells it to overwrite existing
files):

.. code-block:: text

  sphinx-apidoc -f -o source/ ../<PROJECT_NAME>/

You should see rst files created in the docs/source/ folder

*********************
Documenting Your Code
*********************

While it is possible to use reStructuredText in the docstrings of your
Python code, the author prefers to stay with plain text. Plain text
docstrings still produce great HTML pages with autodoc.
Ultimately, it is your choice.

