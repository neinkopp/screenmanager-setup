import os
import sys
import json
import cec
from screen.screen_time import current_screentime, setScreenTime
from config import writeConfig

cec.init()

config = writeConfig()

try:
	THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
	config_path = "config.json"
	config_path = os.path.join(THIS_FOLDER, config_path)

	with open(config_path, "r") as configfile:
		screen_settings = json.load(configfile)['screen_settings']
except IOError as e:
	sys.exit(e)

sys.exit("SC-Code ist: " + str(screen_settings['SCREEN_TIME']))

screen_time = setScreenTime(int(screen_settings['SCREEN_TIME']))

if not config or not screen_time:
	from datetime import datetime
	import os
	log_path = "../error.log"
	THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
	log_file = os.path.join(THIS_FOLDER, log_path)
	with open(log_file, "w") as f:
		print("[ERROR][" + str(datetime.now()) + "][" + str(os.path.abspath(__file__)) + "]: " +
		      "Write to Config: " + str(config) + ", Write Screen Time: " + str(screen_time), file=f)
