from __future__ import absolute_import

try:
	import importlib.resources
except ImportError:
	import importlib
	importlib.resources = importlib.import_module('importlib_resources')

import cherrypy


class Server:
	@cherrypy.expose
	def index(self):
		"""
		>>> srv = Server()
		>>> srv.index()
		b'...'
		"""
		cherrypy.response.headers['Content-Type'] = 'text/html'
		doc = importlib.resources.read_text(__package__, 'okapi.html')
		return doc.encode('utf-8')

	@cherrypy.expose
	def okapibg_png(self):
		return importlib.resources.read_binary(__package__, 'okapibg.png')
