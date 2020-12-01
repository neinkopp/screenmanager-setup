from crontab_mgr import setScreenTime
from crontab_mgr import current_screentime

code = input("Timecode: ")
print(setScreenTime(int(code)))
