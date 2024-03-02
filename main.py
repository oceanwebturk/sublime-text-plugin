NAME = "OceanWebTurk"
VERSION = "1.0"

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
current_project_config_folder = project_folder+"/.oceanwebturk/"

oceanwebturk_configs={
 "current_project_folder": current_project_folder,
 "current_project_config_file": current_project_config_file,
 "project_data": project_data,
 "sublime_configs" : "OceanWebTurk.sublime-settings"
}

if os.path.exists(current_project_config_file):
  oceanwebturk_configs.update(json.load(open(current_project_config_file,'r')))

OceanWebTurk.load(oceanwebturk_configs)
OceanWebTurk.boot()

if __name__ == '__main__':
   sublime.Window.register_command("oceanwebturk_commands",OceanWebTurkCommands)