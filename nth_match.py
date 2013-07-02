import sublime_plugin


class MyNthMatchCommand(sublime_plugin.WindowCommand):
    def run(self):
        self.window.show_input_panel("Pattern:", "",
                                     self.got_pattern, None, None)

    def got_pattern(self, text):
        self.pattern = text
        self.window.show_input_panel("Number of match:", "",
                                     self.got_match, None, None)

    def got_match(self, text):
        # find pattern
        view = self.window.active_view()
        num = int(text)
        match = view.find_all("^$")[num - 1]

        # move cursor to match
        view.sel().clear()
        view.sel().add(match)
        view.show(match)
