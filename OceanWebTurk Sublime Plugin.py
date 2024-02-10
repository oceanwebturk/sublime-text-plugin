import sublime
import sublime_plugin
from .oceanwebturk_commands import *

if __name__ == '__main__':
   sublime.Window.register_command("oceanwebturk_commands",OceanWebTurkCommands)