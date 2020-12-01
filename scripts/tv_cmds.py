def tvCommand(command="toggle"):
	import cec
	cec.init()
	tv = cec.Device(cec.CECDEVICE_TV)
	# if command == "power_on":
	# 	return tv.power_on()
	# elif command == "standby":
	# 	return tv.standby()
	# elif command == "toggle":
	# 	if tv.is_on():
	# 		return tv.standby()
	# 	else:
	# 		return tv.power_on()
	return cec.list_devices()
