#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from crontab import CronTab
def setScreenTime(code):
	if isinstance(code, int) != True or not code <= 2 or not code >= 0:
		return False

	if code == 0:
		pass
