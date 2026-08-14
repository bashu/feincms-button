Changes
-------

26.8.0 (2026-08-14)
~~~~~~~~~~~~~~~~~~

* Required FeinCMS 26+ and updated ``ButtonContent.render()`` for FeinCMS's
  ``AutoRenderTuple``-based render API (FeinCMS 22.x+), replacing the removed
  ``feincms._internal.ct_render_to_string``.
* Dropped Python < 3.10 and Django < 5.2 support; added Django 6.0 / 6.1 support.
* Migrated the rendered button markup and default styles/sizes from Bootstrap 3
  to Bootstrap 5.

2.0.1 (2021-11-28)
~~~~~~~~~~~~~~~~~~

* Added ru translation.

2.0.0 (2021-11-27)
~~~~~~~~~~~~~~~~~~

* Added Django 3+ support.
* Dropped Python 2.7 support.
* Dropped Django 1.10 / 1.11 support.
