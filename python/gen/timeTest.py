import time
import calendar

print(time.time())
print(time.ctime(time.time()))
print(time.localtime())
print(time.localtime(time.time()))
print(time.asctime(time.localtime(time.time())))
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))
print(time.strptime('2019-11-18 08:21:39','%Y-%m-%d %H:%M:%S'))
print(time.mktime(time.strptime('2019-11-18 08:21:39','%Y-%m-%d %H:%M:%S')))

print(calendar.month(2019,11))