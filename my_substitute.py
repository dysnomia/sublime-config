import sublime_plugin
import re


# get selection and replace the strings in 'from' with
# the strings in 'to'
class MySubstituteCommand(sublime_plugin.TextCommand):
    def run(self, edit, **args):
        for region in self.view.sel():
            cur = self.view.substr(region)
            src = args['from']
            dest = args['to']
            for i in range(0, len(src)):
                cur = re.sub(src[i], dest[i], cur)
            self.view.replace(edit, region, cur)
