import sys
with open("/boot/fullpageos.txt", "w+") as file:
	file.write(sys.argv[1])
