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
		config_path = "./config/config.json"

		try:
			with open(config_path, 'w') as configfile:
				json.dump(config_skeleton, configfile, indent=4)

			config_skeleton['access_key'] = json.loads(r.text)['access_key']

			with open(config_path, 'w') as configfile:
				json.dump(config_skeleton, configfile, indent=4)
		except IOError as e:
			return e

		return writeConfig()
	else:
		return False
