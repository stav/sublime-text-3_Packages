import json
import demjson
# import sublime
import sublime_plugin


class PrettyJsonCommand(sublime_plugin.TextCommand):
    """
    view.run_command("pretty_json")
    """
    def run(self, edit):
        """
        self.view.insert(edit, 0, "Hello, World!")
        sel = self.view.sel()[0]
        line = self.view.line(sel)
        [row, currentColumn] = self.view.rowcol(line.end())
        while (currentColumn < 80):
            self.view.insert(edit, self.view.text_point(row, currentColumn), "-")
            currentColumn = currentColumn + 1
        """
        # sel = self.view.sel()[0]
        # line = self.view.line(sel)
        # self.view.insert(edit, 0, str(line))
        self.view.run_command('select_all')
        sel = self.view.sel()
        json_text = self.view.substr(sel[0])
        python_object = demjson.decode(json_text)
        formatted_text = json.dumps(python_object, sort_keys=True, indent=4)
        new_view = self.view.window().new_file()
        new_view.insert(edit, 0, formatted_text)
