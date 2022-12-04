# 오늘 날짜

import datetime as dt

soulTime = dt.datetime.today()

print("{}-{}-{}".format(soulTime.year, str(soulTime.month).zfill(2), str(soulTime.day).zfill(2)))