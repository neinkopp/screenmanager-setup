#!/usr/bin/env python
# -*- coding: UTF-8 -*-
def colorify(color, escape, text):
	colors = {
		"blue": "\033[34m",
		"blue_bold": "\033[1;34m",
		"cyan": "\033[1;36m",
		"green": "\033[32m",
		"green_bold": "\033[1;32m",
		"red_bold": "\033[1;91m",
		"magenta": "\033[35m",
		"magenta_bold": "\033[1;35m",
		"escape": "\033[0m"
	}

	if escape == True:
		escape_char = colors["escape"]
	else:
		escape_char = ""

	return colors[color] + text + escape_char
