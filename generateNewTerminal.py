#!/home/gamzer/anaconda3/bin/python

import subprocess
import re

output = subprocess.check_output('xdotool search --onlyvisible --classname Gnome-terminal || echo "not found" ', shell=True)
output = output.decode('ascii').strip()

if "not found" in output:
	subprocess.call('gnome-terminal', shell=True)
else:
	if "\n" in output:
		code = output.split("\n")[0]
	else:
		code = output

	reg = re.compile('^[0-9]+$')

	if reg.match(code):
		# check if the current window is already the terminal
		currentWindowId = subprocess.check_output('xdotool getactivewindow || echo "no current window"', shell=True)
		currentWindowId = currentWindowId.decode('ascii').strip()
		if "no current window" not in currentWindowId:
			if code == currentWindowId:
				subprocess.call('xdotool search "Google Chrome" windowactivate', shell=True)
				exit(0)

		subprocess.call('xdotool windowactivate --sync {}'.format(code), shell=True)
