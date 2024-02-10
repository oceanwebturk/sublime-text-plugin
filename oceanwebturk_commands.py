import sublime
import sublime_plugin

class OceanWebTurkCommands(sublime_plugin.WindowCommand):
    def __init__(self, *arg, **kwargs):
        super(OceanWebTurkCommands, self).__init__(*arg, **kwargs)
        self.arg = arg
        self.settings = sublime.load_settings("OceanWebTurk.sublime-settings")     
        