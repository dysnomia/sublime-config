import sublime
import sublime_plugin


class MyNthMatchCommand(sublime_plugin.WindowCommand):
    def run(self):
        self.window.show_input_panel("Pattern:", "",
                                     self.got_pattern, None, None)

    def got_pattern(self, pattern):
        self.pattern = pattern
        self.window.show_input_panel("Number of match:", "",
                                     self.got_match, None, None)

    def got_match(self, num):
        try:
            # get entered match number
            num = int(num)

            # find pattern
            view = self.window.active_view()
            matches = view.find_all(self.pattern)
            if num < 1 or num > len(matches):
                raise ValueError('Too few matches.')
            match = matches[num - 1]

            # move cursor to match position
            view.sel().clear()
            view.sel().add(match)
            view.show(match)
        except ValueError as e:
            sublime.status_message(str(e))
