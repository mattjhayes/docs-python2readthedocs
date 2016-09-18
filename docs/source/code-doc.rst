#################
Autodoc Your Code
#################

The Sphinx autodoc extension (see:
`<http://www.sphinx-doc.org/en/stable/ext/autodoc.html>'_) converts docstrings
from your code into the final documentation format at Sphinx build-time.

.. code-block:: text

  .. automodule:: nmeta
    :members:
    :undoc-members:
    :private-members:
    :show-inheritance:

The reStructuredText files in your docs/source directory do not contain
the docstrings. Instead they just contain directives on how to build the
resulting page.

This is very useful, but may not work out of the box.

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

Create requirements.txt file in root of project. Here is an example
requirements.txt file to install the dpkt library:

.. code-block:: text

  #*** Install dpkt with pip:
  dpkt

Replace dpkt with the name(s) of the programs to install with pip.

Fixing Missing Imports with Mock
--------------------------------

Code can be added to docs/source/conf.py to mock troublesome imports so that
Read the Docs Sphinx doesn't error trying to load them.

Sub-modules must be listed after their parent module and there must be full
listing from the top level module, i.e.:

.. code-block:: python

  import mock

  MOCK_MODULES = [
      'ryu',
      'ryu.base',
      'ryu.base.app_manager']

  for mod_name in MOCK_MODULES:
      sys.modules[mod_name] = mock.Mock()



