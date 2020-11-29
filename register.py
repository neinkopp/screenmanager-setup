#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import requests
import sys
import time
import csv
import random
import string
from scripts.colorify import colorify
from scripts.registration import register

print("\033c")
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
result = register(val)

if result != True:
    sys.exit(
        colorify("red_bold", True,
                 "\tERR_034: Der Bildschirm mit der angegebenen Identifikationsnummer wurde nicht gefunden.\n")
    )
else:
    print(
        colorify("green", True, "Die Einrichtung des Bildschirms wurde gefunden.\n\nBefindet sich die Einrichtungswebsite für diesen Bildschirm bereits vor Ihnen?\n")
    )
    choice = "False"
    while (choice.lower() != "ja") and (choice.lower() != "nein"):
        choice = input("Ja/Nein: ")
    if choice.lower() == "ja":
        print(
            colorify("blue_bold", True,
                     "\nDrücken Sie auf der Einrichtungsseite des Bildschirms bitte auf 'Registrierung überprüfen'.")
        )
        input("Fortfahren (Eingabetaste)...")
    else:
        print(
            colorify("blue_bold", True,
                     "\nRufen Sie bitte die Einrichtungswebsite für diesen Bildschirm auf.")
        )
        input("Anschließend drücken Sie bitte hier die Eingabetaste...")

print("\033c")
print(
    colorify("blue_bold", True,
             "Geben Sie nun in das Eingabefeld auf der Seite den folgenden Bestätigungscode ein (Groß- und Kleinschreibung beachten!):\n")
)
print(colorify("magenta_bold", True, ''.join(random.choices(
    string.ascii_letters + string.digits, k=7)) + "\n"))

print(colorify("blue_bold", True, "Anschließend drücken Sie bitte auf 'Bestätigen'."))

input("Drücken Sie die Eingabetaste, um fortzufahren...")
