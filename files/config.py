def writeConfig():
	import os
	import json
	import requests
	import sys
	from pathlib import Path

	THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

	config_path = "config.json"
	config_path = os.path.join(THIS_FOLDER, config_path)

	if Path(config_path).exists():
		with open(config_path, "r") as configfile:
			config_content = json.load(configfile)
	else:
		return False
	access_key = config_content['access_key']

	r = requests.get(
		"http://192.168.178.74/ui/api.php?config&access_key=" + access_key)

	if r.status_code != 200:
		return str(r.status_code)

	rjson = json.loads(r.text)

	if rjson != config_content['screen_settings']:
		config_content['screen_settings'] = rjson
		with open(config_path, "w") as configfile:
			json.dump(config_content, configfile, indent=4)
			return True
	else:
		return True
