def setupPass(setup_key, confirm_key):
	import requests
	import json
	payload = {
		"setup_key": setup_key,
		"confirm_key": confirm_key
	}
	r = requests.post("https://infoscreen.ahfs.de/api.php?register", data=payload)
	if r.status_code == 201:
		return json.loads(r.text)["name"]
	else:
		return False


def initialize(setup_key, confirm_key, screenTime=True):
	import os
	import requests
	import json
	from pathlib import Path
	from files.config import writeConfig

	payload = {
		"setup_key": setup_key,
		"confirm_key": confirm_key
	}
	r = requests.post(
		"https://infoscreen.ahfs.de/api.php?get_access_key", data=payload)
	if r.status_code == 200:
		config_skeleton = {
			"access_key": "",
			"screen_settings": {

			}
		}

		THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

		config_path = "config.json"
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
			screen_settings = json.load(configfile)['screen_settings']

		import urllib.parse
		import subprocess

		website = "https://infoscreen.ahfs.de/screens/?"
		params = {"access_key": config_skeleton['access_key']}
		query_string = urllib.parse.urlencode(params)
		url = website + query_string

		writefpos_path = os.path.join(THIS_FOLDER, "write_fpos.py")

		fpostxt_path = "/boot/fullpageos.txt"
		fprocess = subprocess.run(["sudo", "python3", writefpos_path, url])
		if fprocess.returncode != 0:
			return fprocess.returncode

		if screenTime == True:
			from files.screen.screen_time import setScreenTime
			if setScreenTime(int(screen_settings['SCREEN_TIME'])):

				from crontab import CronTab

				cron = CronTab(user=True)
				cron.remove_all(comment="CONFIG")

				config = cron.new(command="python3 " + os.path.join(
					os.getcwd(), "screenmanager-setup/files/config_job.py"), comment="CONFIG")
				config.minute.every(1)

				cron.write()

				return True
			else:
				return "Fehler beim Einstellen des ST-Codes"
		else:
			return True
	else:
		return False


def getCecCompatibility():
	import cec
	from files.tools.colorify import colorify
	import sys
	import os
	import json
	cec.init()
	tv = cec.Device(cec.CECDEVICE_TV)
	try:
		print(tv.is_on())
	except OSError as e:
		print(e)
		print(colorify("red_bold", True,
                 "Der Energiestatus des Bildschirms konnte nicht ermittelt werden."))
		print(colorify("magenta", False, ""))
		print("1: Bildschirm ohne Automatische Ein- oder Ausschaltung betreiben")
		print("2: Erneut versuchen (Neustart)")
		print("3: Programm beenden")
		print(colorify("magenta", True, ""), end="")

		val = ""
		while not val.isnumeric() or int(val) < 1 or int(val) > 3:
			val = input("Wählen Sie eine Option: ")

		if int(val) == 1:

			THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
			config_path = os.path.join(THIS_FOLDER, "registrationProgress.jsonc")

			try:
				with open(config_path, "r") as cfile:
					config = json.load(cfile)

				config["isCecCompatible"] = False

				with open(config_path, "w") as cfile:
					json.dump(config, cfile, indent=4)
			except EnvironmentError as e:
				sys.exit(e)
			else:
				sys.exit(colorify("green", True, "Konfiguration wurde erfolgreich bearbeitet."))
		elif int(val) == 2:
			import subprocess
			print(colorify("magenta", True, "Starte System neu..."))
			subprocess.run(["sudo", "reboot"])
		elif int(val) == 3:
			sys.exit(colorify("red_bold", True, "Programm beendet."))
	else:
		print(colorify("green", True, "Der Status des Fernsehers konnte ermittelt werden."))
		import os
		import json

		THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
		config_path = os.path.join(THIS_FOLDER, "registrationProgress.jsonc")

		try:
			with open(config_path, "r") as cfile:
				config = json.load(cfile)

			config["isCecCompatible"] = True

			with open(config_path, "w") as cfile:
				json.dump(config, cfile, indent=4)
		except EnvironmentError as e:
			sys.exit(e)
		else:
			sys.exit(colorify("green", True, "Konfiguration wurde erfolgreich bearbeitet."))


def register(screenTime):
	from files.tools.colorify import colorify
	import sys
	import time
	import random
	import string
	print("\033c", end="")
	print(
		colorify("blue_bold", True,
                    "Geben Sie bitte die Identifikationsnummer des einzurichtenden Bildschirms ein:\n")
	)
	val = input(colorify("green", False, "> "))
	print("\033[0m")

	print("Identifikationsnummer wird überprüft. Bitte warten", end="")
	for i in reversed(range(1, 4)):
		print(".", end=""),
		sys.stdout.flush()
		time.sleep(1)
	print("\n")

	# Überprüfen
	confirm_key = ''.join(random.choices(
		string.ascii_letters + string.digits, k=7))

	result = setupPass(val, confirm_key)

	if result == False:
		sys.exit(
			colorify("red_bold", True,
                            "\tFEHLER: Der Bildschirm mit der angegebenen Identifikationsnummer wurde nicht gefunden / die Registrierung ist vorher bereits abgeschlossen worden.\n")
		)

	print("\033c")
	print(
		colorify("green", True, "Der Bildschirm mit dem Namen '") + colorify("magenta", True,
                                                                       result) + colorify("green", True, "' wurde gefunden und kann nun eingerichtet werden.")
	)
	print(
		colorify("blue_bold", True,
                    "Geben Sie bitte in das Eingabefeld auf der Einrichtungswebseite den folgenden Bestätigungscode ein (Groß- und Kleinschreibung beachten!):\n")
	)

	print(colorify("magenta_bold", True, confirm_key + "\n"))

	print(colorify("blue_bold", True, "Anschließend drücken Sie bitte auf 'Registrierung abschließen' und folgen den weiteren Anweisungen.\n\nSobald Sie damit fertig sind, können Sie hier mit der Einrichtung fortfahren."))

	input("Drücken Sie (nach abgeschlossener Konfiguration) die Eingabetaste, um fortzufahren...")

	if not initialize(val, confirm_key, screenTime):
		sys.exit(
                    colorify("red_bold", True,
                             "\tFEHLER: Konnte Bildschirm nicht initialisieren. Bitte setzen Sie Ihr System neu auf.\n")
                )
	else:
		import os
		colorify("green", True,
                    "Bildschirm wurde erfolgreich eingerichtet und sollte nun nach Plan funtionieren. Starte in 5 Sekunden neu, um Änderungen zu übernehmen...")
		time.sleep(5)
		os.system('sudo reboot')
		sys.exit()
