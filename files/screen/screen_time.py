#!/usr/bin/python3
# -*- coding: UTF-8 -*-

def tvCommand(command="toggle"):
	import cec
	if init:
		cec.init()
	tv = cec.Device(cec.CECDEVICE_TV)
	if command == "power_on":
		return tv.power_on()
	elif command == "standby":
		return tv.standby()
	elif command == "toggle":
		if tv.is_on():
			return tv.standby()
		else:
			return tv.power_on()


def current_screentime():
	from crontab import CronTab
	import cec

	cec.init()
	tv = cec.Device(cec.CECDEVICE_TV)  # CEC initialisieren
	cron = CronTab(user=True)

	# finde Cronjob mit "CEC" im Comment
	iter = cron.find_comment('CEC')
	for job in iter:
		if job:
			return 1  # wenn es einen solchen Cronjob gibt, muss eine Bildschirmzeit existieren

	try:
		if(tv.is_on()):  # wenn der Fernseher an ist, muss er zwangsl. kontinuierlich eingeschaltet sein
			return 2
		else:  # wenn nicht, dann muss er kontinuierlich ausgeschaltet sein
			return 0
	except OSError:
		return False


def setScreenTime(code):
	from crontab import CronTab

	if isinstance(code, int) != True or not code <= 2 or not code >= 0:
		return False
	print("First Block")

	cron = CronTab(user=True)

	if code == 0:
		cron.remove_all(comment='CEC')
		cron.write()
		print("Second Block")
		return tvCommand("standby")

	if code == 1:
		cron.remove_all(comment='CEC')
		start = cron.new(command="echo 'on 0' | cec-client -s -d 1",
		                 comment="CEC", user=True)
		end = cron.new(command="echo 'standby 0' | cec-client -s -d 1",
		               comment="CEC", user=True)
		start.hour.on(7)
		start.minute.on(30)

		end.hour.on(16)
		end.minute.on(30)

		cron.write()
		from datetime import datetime
		now = datetime.now()
		starttime = now.replace(hour=7, minute=30, second=0, microsecond=0)
		endtime = now.replace(hour=16, minute=30, second=0, microsecond=0)
		if now < starttime or now > endtime:
			return tvCommand("standby")
		else:
			return tvCommand("power_on")

	if code == 2:
		cron.remove_all(comment='CEC')
		cron.write()
		return tvCommand("power_on")
