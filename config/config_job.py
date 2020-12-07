from config.config import writeConfig
from scripts.execute.screen_time import current_screentime, setScreenTime

config = writeConfig()

screen_time = setScreenTime(current_screentime())

if not config or not screen_time:
	from datetime import datetime
	import os
	log_path = "../error.log"
	THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
	log_file = os.path.join(THIS_FOLDER, log_path)
	with open(log_file, "w") as f:
		print("[ERROR][" + str(datetime.now()) + "][" + str(os.path.abspath(__file__)) + "]: " +
		      "Write to Config: " + str(config) + ", Write Screen Time: " + str(screen_time), file=f)
