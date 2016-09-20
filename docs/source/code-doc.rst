#################
Autodoc Your Code
#################

The Sphinx autodoc extension
(see `<http://www.sphinx-doc.org/en/stable/ext/autodoc.html>`_ )
converts docstrings
from your Python code into the final documentation format at Sphinx build-time.

This is very useful, but may not work out of the box. Here are some steps
to set it up properly:

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

******************
autodoc directives
******************

The reStructuredText files for your Python modules in docs/source do not
contain the docstrings. Instead they just contain directives on how to build
the corresponding page.

They contain reStructuredText with directives to build
the documentation from a particular Python module in your project. Example:

.. code-block:: text

  example_module module
  =====================

  .. automodule:: example_module
      :members:
      :undoc-members:
      :show-inheritance:

Example from this project, showing source RST and Python with resulting HTML:

  reStructuredText:
    `example_module.rst <https://raw.githubusercontent.com/mattjhayes/docs-python2readthedocs/master/docs/source/example_module.rst>`_

  Python:
    `example_module.py <https://github.com/mattjhayes/docs-python2readthedocs/blob/master/docs-python2readthedocs/example_module.py>`_

  Auto-generated HTML:
    `example_module.html <example_module.html>`_

Here are some additional directives that you may wish to add include:

- Include private members, i.e. ones that start with an underscore

  .. code-block:: text

    :private-members:

- Include special members, i.e. ones that start and end with two underscores,
  such as __init__

  .. code-block:: text

   :special-members:

Example using these extra directives:

  reStructuredText:
    `example_module2.rst <https://raw.githubusercontent.com/mattjhayes/docs-python2readthedocs/master/docs/source/example_module2.rst>`_

  Python:
    `example_module2.py <https://github.com/mattjhayes/docs-python2readthedocs/blob/master/docs-python2readthedocs/example_module2.py>`_

  Auto-generated HTML:
    `example_module2.html <example_module2.html>`_

*****************************
One-Off Creation of RST Files
*****************************

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

