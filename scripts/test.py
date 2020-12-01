from crontab_mgr import setScreenTime
from crontab_mgr import current_screentime
import t_functions

func = input("func: ")

if func == "toggle":
	print(toggle())
elif func == "powerOn":
	print(powerOn())
elif func == "standby":
	print(standby())
