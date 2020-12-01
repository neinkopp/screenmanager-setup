def toggle():
	import cec
	cec.init()
	tv = cec.Device(cec.CECDEVICE_TV)
	if tv.is_on():
		return tv.standby()
	else:
		return tv.power_on()
