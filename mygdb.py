import sublime, sublime_plugin

class MyGdbCommand(sublime_plugin.WindowCommand):
	def run(self):
		self.window.run_command('set_layout', {
			"cols":[0.0, 0.5, 1.0],
			"rows":[0.0, 0.8, 1.0],
			"cells":[[0, 0, 1, 1], [1, 0, 2, 1], [0, 1, 2, 2]]
		})
		self.window.run_command('repl_open', {
			"type": "subprocess",
			"encoding": "utf8",
			"cmd": ["gdb", "-i", "-u", "$file_path/a.out"],
			"cwd": "$file_path",
			#"syntax": "Packages/Python/Python.tmLanguage",
			"external_id": "gdb"
		})
		self.window.run_command('move_to_group', { "group": 2 })
