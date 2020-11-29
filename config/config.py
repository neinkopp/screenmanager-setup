import json
import requests
import sys

r = requests.get("http://localhost/ui/api.php")
r.json()
if r.status_code != 200:
	sys.exit('ERROR: STATUS_CODE IS ' + str(r.status_code))
rjson = json.loads(r.text)

config_path = "./config/config.json"

with open(config_path, "r") as configfile:
	config_content = json.load(configfile)

if rjson['screen_settings'] != config_content['screen_settings']:
	config_content['screen_settings'] = rjson['screen_settings']
	with open(config_path, "w") as configfile:
		json.dump(config_content, configfile, indent=4)
		print("Modified config!")
else:
	print('Continue.')
