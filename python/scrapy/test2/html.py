import json
import re

def read():
	a = []
	with open('test.json', mode='r', encoding="utf-8") as f:
		a = json.load(f)
		# a = re.sub(",", "<br/>", "apple,")
	write(a)

def write(a):
	a = sorted(a, key=lambda k: re.search("\\d+", str(k)).group())
	with open('test.html', mode='w', encoding="utf-8") as f:
		for k in a:
			f.write(str("<p>%s</p>" %k))

def test():
	read()

test()