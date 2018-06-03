.. image:: https://img.shields.io/pypi/v/http-okapi.svg
   :target: https://pypi.org/project/http-okapi

.. image:: https://img.shields.io/pypi/pyversions/http-okapi.svg

.. image:: https://img.shields.io/travis/jaraco/http-okapi/master.svg
   :target: https://travis-ci.org/jaraco/http-okapi

.. .. image:: https://img.shields.io/appveyor/ci/jaraco/http-okapi/master.svg
..    :target: https://ci.appveyor.com/project/jaraco/http-okapi/branch/master

.. .. image:: https://readthedocs.org/projects/http-okapi/badge/?version=latest
..    :target: https://http-okapi.readthedocs.io/en/latest/?badge=latest

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
