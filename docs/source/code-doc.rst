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

See `<http://nmeta.readthedocs.io/en/latest/nmeta.html>`_ for an example of
the html that this generates.

There is a script that you can run to

In the docs directory, run this command to create rst files that document
your python modules:

.. code-block:: text

  sphinx-apidoc -f -o source/ ../<PROJECT_NAME>/

You should see rst files created in the docs/source/ folder
Note that the -f option tells it to overwrite existing files.
You should only run this command once to set up the *.rst files.




********************************************
Autodoc Fix for External Module Dependancies
********************************************

Read the Docs runs Sphinx autodoc against your code in its environment.
So, while autodoc may run fine in your own environment, it may fail in
ReadtheDocs, due to imported modules not being present.

There are a couple of ways to fix this if it is a problem.

Fixing Missing Imports with virtualenv
======================================

In this fix, we tell ReadtheDocs to install module dependancies via pip in a
virtual environment, and then run Sphinx autodoc.

Enable virtualenv in Read the Docs
----------------------------------

Log into Read the Docs and go into Settings -> Profile -> <PROJECT_NAME>

Go into Admin -> Advanced Settings and tick the
'Install your project inside a virtualenv using setup.py install' box

Fill in the 'Requirements file:' box with requirements.txt

Click 'Submit'

Create a requirements.txt file
------------------------------

Create requirements.txt file in root of project. Here is an example
requirements.txt file to install the dpkt library:

.. code-block:: text

  #*** Install dpkt with pip:
  dpkt

Replace dpkt with the name(s) of the programs to install with pip.

Fixing Missing Imports with Mock
================================

If the virtualenv solution isn't fully working from you then consider using
mock. Code can be added to docs/source/conf.py to mock troublesome imports
so that Read the Docs Sphinx doesn't error trying to load them.

Sub-modules must be listed after their parent module and there must be full
listing from the top level module. Example that mocks ryu.base.app_manager:

.. code-block:: python

  import mock

  MOCK_MODULES = [
      'ryu',
      'ryu.base',
      'ryu.base.app_manager']

  for mod_name in MOCK_MODULES:
      sys.modules[mod_name] = mock.Mock()



