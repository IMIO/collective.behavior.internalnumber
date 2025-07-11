# -*- coding: utf-8 -*-
"""Installer for the collective.behavior.internalnumber package."""

from setuptools import find_packages
from setuptools import setup


long_description = "\n\n".join(
    [
        open("README.rst").read(),
        open("CONTRIBUTORS.rst").read(),
        open("CHANGES.rst").read(),
    ]
)


setup(
    name="collective.behavior.internalnumber",
    version="0.5.dev0",
    description="Configurable internal number plone behavior",
    long_description=long_description,
    # Get more from https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: Addon",
        "Framework :: Plone :: 4.3",
        "Framework :: Plone :: 5.2",
        "Framework :: Plone :: 6.0",
        "Framework :: Plone :: 6.1",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.13",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords="Python Plone",
    author="Stephan Geulette",
    author_email="support@imio.be",
    # url='https://pypi.python.org/pypi/collective.behavior.internalnumber',
    project_urls={
        "PyPI": "https://pypi.python.org/pypi/collective.behavior.internalnumber",
        "Source": "https://github.com/collective/collective.behavior.internalnumber",
    },
    license="GPL version 2",
    packages=find_packages("src", exclude=["ez_setup"]),
    namespace_packages=["collective", "collective.behavior"],
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "plone.api",
        "Products.GenericSetup>=1.8.2",
        "setuptools",
        "collective.behavior.talcondition",
        "collective.z3cform.datagridfield",
    ],
    extras_require={
        "test": [
            "plone.app.testing",
            "plone.testing>=5.0.0",
            "plone.app.contenttypes",
            "plone.app.robotframework[debug]",
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
