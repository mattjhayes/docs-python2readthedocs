#########
UI Tweaks
#########

Here are some minor changes that you may want to consider to change
the user interface (UI) look and feel:

Themes
------

Themes are used by Sphinx to control how the documentation looks when
exported to the final formats.

I prefer the Read the Docs theme over the Alabaster theme, which Sphinx
installation has configured, so I update it in docs/source/conf.py.

Original line:

.. code-block:: text

  html_theme = 'alabaster'

Change it to:

.. code-block:: text

  html_theme = 'default'

Other Sphinx built-in themes include:
- classic
- sphinxdoc
- scrolls
- agogo
- traditional
- nature
- haiku

Sidebar
-------
The local site sidebar is a bit limited, however works
fine in Read the Docs. If you want a better sidebar for the local build then
try this update. Edit the docs/source/conf.py file. Find this stanza:

.. code-block:: text

  # Custom sidebar templates, maps document names to template names.
  #
  # html_sidebars = {}

Replace the last line of this stanza so it reads:

.. code-block:: text

  # Custom sidebar templates, maps document names to template names.
  #
  html_sidebars = { '**': ['globaltoc.html', 'relations.html', 'sourcelink.html', 'searchbox.html'], }
