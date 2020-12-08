#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import sys
import time
import os
import csv
import random
import string
from files.tools.colorify import colorify
from files.registration import setupPass
from files.registration import initialize

if os.geteuid() != 0:
	sys.exit(colorify("red_bold", True,
                   "Sie müssen root-Berechtigungen haben, um diese Datei auszuführen. Geben Sie vor dem Befehl 'sudo' ein. (sudo python3 [...])"))

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

# if not initialize(val, confirm_key):
# 	sys.exit(
#             colorify("red_bold", True,
#                      "\tFEHLER: Konnte Bildschirm nicht initialisieren. Bitte setzen Sie Ihr System neu auf.\n")
#         )
# else:
# 	colorify("green", True,
# 	         "Bildschirm wurde erfolgreich eingerichtet und sollte nun nach Plan funtionieren.")
# 	sys.exit()

print(initialize(val, confirm_key))
