def tvCommand(command="toggle"):
	import cec
	cec.init()
	tv = cec.Device(cec.CECDEVICE_TV)
	if command == "power_on":
		while tv.power_on() != True:
			pass
		else:
			return True
	elif command == "standby":
		while tv.standby() != True:
			pass
		else:
			return True
	elif command == "toggle":
		if tv.is_on():
			while tv.standby() != True:
				pass
			else:
				return True
		else:
			while tv.power_on() != True:
				pass
			else:
				return True
