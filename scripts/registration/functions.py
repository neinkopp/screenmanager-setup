def setupPass(setup_key, confirm_key):
	import requests
	import json
	payload = {
		"setup_key": setup_key,
		"confirm_key": confirm_key
	}
	r = requests.post("http://192.168.178.74/ui/api.php?register", data=payload)
	if r.status_code == 201:
		return json.loads(r.text)["name"]
	else:
		return False


def initialize(setup_key, confirm_key):
	import os
	import requests
	import json
	from pathlib import Path
	from config.config import writeConfig

	payload = {
		"setup_key": setup_key,
		"confirm_key": confirm_key
	}
	r = requests.post(
		"http://192.168.178.74/ui/api.php?get_access_key", data=payload)
	if r.status_code == 200:
		config_skeleton = {
			"access_key": "",
			"screen_settings": {

			}
		}

		THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

		config_path = "../../config/config.json"
		config_path = os.path.join(THIS_FOLDER, config_path)

		try:
			with open(config_path, 'w') as configfile:
				json.dump(config_skeleton, configfile, indent=4)

			config_skeleton['access_key'] = json.loads(r.text)['access_key']

			with open(config_path, 'w') as configfile:
				json.dump(config_skeleton, configfile, indent=4)
		except IOError as e:
			return e

		res = writeConfig()

		if not res:
			return print("Failed. Result:", res)

		with open(config_path, "r") as configfile:
			screen_settings = json.loads(configfile)['screen_settings']

		from scripts.execute.screen_time import setScreenTime
		if setScreenTime(screen_settings['SCREEN_TIME']):
			return True
		else:
			return "Fehler beim Einstellen des ST-Codes"

	else:
		return False
