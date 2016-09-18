#################
Autodoc Your Code
#################

The Sphinx autodoc extension (see:
`<http://www.sphinx-doc.org/en/stable/ext/autodoc.html>'_) converts docstrings
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

  .. automodule:: nmeta
    :members:
    :undoc-members:
    :private-members:
    :show-inheritance:

See `<example_module.html>`_ for an example of
the html that this generates.

There is a script that you can run to create a directive file per Python
module. You should only run this command once to set up the *.rst files.

In the docs directory, run this command to create rst files that document
your python modules (Note that the -f option tells it to overwrite existing
files):

.. code-block:: text

  sphinx-apidoc -f -o source/ ../<PROJECT_NAME>/

You should see rst files created in the docs/source/ folder



