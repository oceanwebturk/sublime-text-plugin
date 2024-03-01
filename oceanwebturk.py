NAME = "OceanWebTurk"
VERSION = "1.0"

import os
import json
import sublime,sublime_api, sublime_plugin

class OceanWebTurk(object):
	def __init__(self, arg):
		super(OceanWebTurk, self).__init__()
		self.arg = arg

	def load(config):
	   global init
	   init=config 

	def loadReturns():
		return init

	def boot():
	  global sublime_configs
	  sublime_configs = sublime.load_settings(init.get("sublime_configs"))
	  

class OceanWebTurkCommands():
	def __init__(self, arg):
		super(OceanWebTurkCommands, self).__init__()
		self.arg = arg
		self.oceanwebturk=OceanWebTurk()
		self.config=self.oceanwebturk.loadReturns()
	
	def run():
	    print(self.config)