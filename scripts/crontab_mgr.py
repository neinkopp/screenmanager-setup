#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from crontab import CronTab
import re
import cec

cec.init()
tv = cec.Device(cec.CECDEVICE_TV)  # CEC initialisieren


def current_screentime():
	cron = CronTab()

	# finde Cronjob mit "CEC" im Comment
	iter = cron.find_comment(re.compile('CEC'))
	for job in iter:
		if job:
			return 1  # wenn es einen solchen Cronjob gibt, muss eine Bildschirmzeit existieren

	if(tv.is_on()):  # wenn der Fernseher an ist, muss er zwl. kontinuierlich eingeschaltet sein
		return 2
	else:  # wenn nicht, dann muss er kontinuierlich ausgeschaltet sein
		return 0


def setScreenTime(code):
	if isinstance(code, int) != True or not code <= 2 or not code >= 0:
		return False
	elif(current_screentime() == code):
		return True

	cron = CronTab

	if code == 0:
		cron.remove_all(comment='CEC')
		return tv.standby()

	if code == 1:
		start = cron.new(command="echo 'on 0' | cec-client -s -d 1",
		                 comment="CEC", user=True)
		end = cron.new(command="echo 'standby 0' | cec-client -s -d 1",
		               comment="CEC", user=True)
		from datetime import datetime
 		now = datetime.now()
 		starttime = now.replace(hour=7, minute=30, second=0, microsecond=0)
 		endtime = now.replace(hour=16, minute=30, second=0, microsecond=0)
		if now < starttime or now > endtime:
			return tv.standby()
		else:
			return tv.power_on()

	if code == 2:
		cron.remove_all(comment='CEC')
		return tv.power_on()
