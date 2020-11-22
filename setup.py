import requests
import sys
import time
import csv
from scripts.registration import register

print("\033c")
print(
    "\033[1;34mGeben Sie bitte die Identifikationsnummer des einzurichtenden Bildschirms ein:\033[0m\n"
)
val = input("\033[32m> ")
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
        "\033[1;91m\tERR_034: Der Bildschirm mit der angegebenen Identifikationsnummer wurde nicht gefunden. \033[0m\n"
    )
else:
    print(
        "\033[32mDie Einrichtung des Bildschirms wurde gefunden.\n\nBefindet sich die Einrichtungswebsite für diesen Bildschirm bereits vor Ihnen?\033[0m\n"
    )
    choice = "False"
    while (choice.lower() != "ja") and (choice.lower() != "nein"):
        choice = input("Ja/Nein: ")
    if choice.lower() == "ja":
        print(
            "\n\033[1;34mDrücken Sie auf der Einrichtungsseite des Bildschirms bitte auf 'Registrierung überprüfen'.\033[0m"
        )
        input("Fortfahren (Eingabetaste)...")
        print("\033c")
    else:
        print(
            "\n\033[1;34mRufen Sie bitte nun auf einem externen Endgerät die Einrichtungswebsite für diesen Bildschirm auf.\033[0m"
        )
        input("Anschließend drücken Sie bitte hier die Eingabetaste...")
        print("\033c")

print(
    "\n\033[1;34mGeben Sie nun in das Eingabefeld auf der Seite den folgenden Bestätigungscode ein:\033[0m\n"
)
print("\033[1;35mS8AS37F\033[0m\n")

print("\033[1;34mAnschließend drücken Sie bitte auf 'Bestätigen'.\033[0m\n")

input("Drücken Sie die Eingabetaste, um fortzufahren...")
