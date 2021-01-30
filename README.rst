.. image:: https://img.shields.io/pypi/v/http-okapi.svg
   :target: `PyPI link`_

.. image:: https://img.shields.io/pypi/pyversions/http-okapi.svg
   :target: `PyPI link`_

.. _PyPI link: https://pypi.org/project/http-okapi

.. image:: https://github.com/jaraco/http-okapi/workflows/tests/badge.svg
   :target: https://github.com/jaraco/http-okapi/actions?query=workflow%3A%22tests%22
   :alt: tests

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
   :alt: Code style: Black

.. .. image:: https://readthedocs.org/projects/skeleton/badge/?version=latest
..    :target: https://skeleton.readthedocs.io/en/latest/?badge=latest

A simple HTTP API tool.

The Tool
========

The tool is an HTML page with a background image. These resources are
presented as package resources of the ``http_okapi`` package. The
resource filenames are ``okapi.html`` and ``okapibg.png``. The HTML
page references ``okapibg.png`` by name, so the two files are meant
to be served from the same path.

CherryPy Handler
================

This package also presents a server implementation for CherryPy. To
use it, simply bind the ``http_okapi.cherrypy.Server`` somewhere in
your handler tree::

    class MyServer:
        okapi = http_okapi.cherrypy.Server()

Then, the okapi tool will be available at that path.
