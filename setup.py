#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import subprocess
import time
import sys
from scripts.colorify import colorify

print("\033c", end="")
print(colorify("blue_bold", True, "Nachfolgend wird Ihr Raspberry Pi aktualisiert. \nAußerdem wird Ihr System konfiguriert und wichtige Programme werden installiert.\nDies dauert in der Regel einige Minuten. Am Ende wird der Raspberry Pi neugestartet."))
input("Zum Fortfahren drücken Sie bitte die Eingabetaste, zum Abbrechen Strg + C...")
print("Bitte warten...\n")

returncode = 0
step = 0

if returncode == 0:
	cmd = subprocess.run(["sudo", "apt-get", "update", "-qq"])
	returncode = cmd.returncode
	print(colorify("magenta_bold", True, "Schritt 1/7 abgeschlossen."))
	step = step + 1

if returncode == 0:
	cmd = subprocess.run(["sudo", "apt-get", "dist-upgrade", "-qq"])
	returncode = cmd.returncode
	print(colorify("magenta_bold", True, "Schritt 2/7 abgeschlossen."))
	step = step + 1

if returncode == 0:
	cmd = subprocess.run(["sudo", "timedatectl", "set-timezone", "Europe/Berlin"])
	returncode = cmd.returncode
	print(colorify("magenta_bold", True, "Schritt 3/7 abgeschlossen."))
	step = step + 1

if returncode == 0:
	cmd = subprocess.run(
		["sudo", "dpkg-reconfigure", "--frontend", "noninteractive", "tzdata"])
	returncode = cmd.returncode
	print(colorify("magenta_bold", True, "Schritt 4/7 abgeschlossen."))
	step = step + 1

if returncode == 0:
	cmd = subprocess.run(["sudo", "apt-get", "install", "cec-utils", "-qq"])
	returncode = cmd.returncode
	print(colorify("magenta_bold", True, "Schritt 5/7 abgeschlossen."))
	step = step + 1

if returncode == 0:
	cmd = subprocess.run(["sudo", "apt-get", "install", "python3-crontab", "-qq"])
	returncode = cmd.returncode
	print(colorify("magenta_bold", True, "Schritt 6/7 abgeschlossen."))
	step = step + 1

if returncode == 0:
	cmd = subprocess.run(["sudo", "apt", "autoremove", "-y"])
	returncode = cmd.returncode
	print(colorify("magenta_bold", True, "Schritt 7/7 abgeschlossen."))
	step = step + 1

if returncode == 0 and step == 7:
	print(colorify("blue_bold", True,
                "Alle Schritte wurden erfolgreich abgeschlossen. Starte in 10 Sekunden neu..."))
	time.sleep(10)
	subprocess.run(["sudo", "reboot"])
else:
	print(returncode)
	print(step)
	sys.exit(colorify("red_bold", True,
                   "Es ist mindestens ein Fehler aufgetreten. Kontaktieren Sie bitte den Administrator."))
