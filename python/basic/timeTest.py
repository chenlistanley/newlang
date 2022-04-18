import time
import calendar
from datetime import date

def test():
	print(time.time())
	print(time.ctime(time.time()))
	print(time.localtime())
	print(time.localtime(time.time()))
	print(time.asctime(time.localtime(time.time())))
	print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))
	print(time.strptime('2019-11-18 08:21:39','%Y-%m-%d %H:%M:%S'))
	print(time.mktime(time.strptime('2019-11-18 08:21:39','%Y-%m-%d %H:%M:%S')))

	print(calendar.month(2019,11))

def test2():
	print(date.today())
	a = date.today() - date.fromisoformat('2022-03-16')
	print(a.days)

test2()