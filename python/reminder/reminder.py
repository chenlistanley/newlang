import time

def test():
	today = time.strftime('%Y-%m-%d',time.localtime())
	with open('reminder.txt', encoding='utf-8') as s:
		for a in s:
			if today in a:
				print(a)
	
test()