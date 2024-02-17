# Import Librarys
import os
import json
import sublime,sublime_api, sublime_plugin
from .oceanwebturk import *

#  Configration Varibles
project_data = sublime.active_window().project_data()
project_folder = project_data['folders'][0]['path']
current_project_folder = project_folder+"/"
current_project_config_file = project_folder+"/oceanwebturk.json"

if os.path.exists(current_project_config_file):
  oceanwebturk_configs = json.loads(open(current_project_config_file, 'r').read()) 
else:
  oceanwebturk_configs = {}

OceanWebTurk.load({
 "current_project_folder": current_project_folder,
 "current_project_config_file": current_project_config_file,
 "configs": oceanwebturk_configs,
 "project_data": project_data,
 "sublime_configs": "OceanWebTurk.sublime-settings"
})
OceanWebTurk.boot()

if __name__ == '__main__':
   sublime.Window.register_command("oceanwebturk_commands",OceanWebTurkCommands)