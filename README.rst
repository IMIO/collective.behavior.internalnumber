.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on pypi or github. It is a comment.

==============================================================================
collective.behavior.internalnumber
==============================================================================

This product adds a plone behavior for dexterity content.
The behavior adds a text field containing an internal number.

Features
--------

- Optional uniqueness validation
- Optional default value
- Global or type by type configuration
- A configuration page can manage by portal type:

  * a uniqueness option
  * an optional prefix, added in the index, to separate indexed values type by type
  * a default value tal expression
  * an incremented counter

Examples
--------


Translations
------------

This product has been translated into

- French (thanks the author)


Installation
------------

Install collective.behavior.internalnumber by adding it to your buildout::

    [buildout]

    ...

    eggs =
        collective.behavior.internalnumber


and then running ``bin/buildout``


Contribute
----------

- Issue Tracker: https://github.com/collective/collective.behavior.internalnumber/issues
- Source Code: https://github.com/collective/collective.behavior.internalnumber
- Documentation: https://docs.plone.org/foo/bar


License
-------

The project is licensed under the GPLv2.
