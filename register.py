#!/usr/bin/python3
# -*- coding: UTF-8 -*-

def mainMenu():
	import sys
	from files.tools.colorify import colorify
	from files.registration import setupPass
	from files.registration import initialize
	from files.registration import getCecCompatibility
	from files.registration import register
	import os
	import json

	THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
	config_path = os.path.join(THIS_FOLDER, "registrationProgress.jsonc")
	try:
		with open(config_path, "r") as cfile:
			config_file = json.load(cfile)
	except EnvironmentError as e:
		sys.exit(e)

	def terminal_size():
		import fcntl
		import termios
		import struct
		h, w, hp, wp = struct.unpack('HHHH', fcntl.ioctl(
			0, termios.TIOCGWINSZ, struct.pack('HHHH', 0, 0, 0, 0)))
		return w, h

	print("\033[2J" + "\033[H", end="")

	for x in range(terminal_size()[0]):
		print("\u2500", end="")

	print(colorify("cyan", True, "screenmanager-setup / register"))

	for x in range(terminal_size()[0]):
		print("\u2500", end="")

	print(colorify("magenta", False, ""))

	if config_file['isCecCompatible'] == 0:
		print(colorify("cyan", True, "Führe CEC-Kompatibilitätstest durch. Achten Sie darauf, dass Ihr Bildschirm mit dem Raspberry Pi verbunden ist."))
		input("Drücken Sie die Eingabetaste, um fortzufahren...")
		getCecCompatibility()
	elif config_file['regComplete'] == 0:
		print("1: Bildschirm registrieren")
		print("2: Programm beenden")
		print(colorify("magenta", True, ""))
		val = ""
		while not val.isnumeric() or int(val) < 1 or int(val) > 2:
			val = input("Wählen Sie eine Option: ")
		if int(val) == 1:
			if config_file['isCecCompatible'] == False:
				register(screenTime=False)
			else:
				register(screenTime=True)
		elif int(val) == 2:
			sys.exit(colorify("red", True, "Programm beendet."))
	else:
		print("1: Registrierung zurücksetzen (NICHT FUNKTIONAL)")
		print("2: Programm beenden")
		print(colorify("magenta", True, ""))
		val = ""
		while not val.isnumeric() or int(val) < 1 or int(val) > 2:
			val = input("Wählen Sie eine Option: ")
		if int(val) == 1:
			print("DIESE OPTION HAT KEINE FUNKTION.")
			mainMenu()
		elif int(val) == 2:
			sys.exit(colorify("red", True, "Programm beendet."))
