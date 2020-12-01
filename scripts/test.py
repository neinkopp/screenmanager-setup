from crontab_mgr import setScreenTime
from crontab_mgr import current_screentime
from t_functions import toggle
from t_functions import powerOn
from t_functions import standby

func = input("func: ")

if func == "toggle":
	print(toggle())
elif func == "powerOn":
	print(powerOn())
elif func == "standby":
	print(standby())
