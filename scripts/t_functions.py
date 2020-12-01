def toggle():
	import cec
	cec.init()
	tv = cec.Device(cec.CECDEVICE_TV)
	if tv.is_on():
		return tv.standby()
	else:
		return tv.power_on()


def powerOn():
	import cec
	cec.init()
	tv = cec.Device(cec.CECDEVICE_TV)
	return tv.power_on()


def standby():
	import cec
	cec.init()
	tv = cec.Device(cec.CECDEVICE_TV)
	return tv.standby()
