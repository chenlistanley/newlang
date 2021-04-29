import json
import re

def read():
	a = []
	with open('test.json', mode='r', encoding="utf-8") as f:
		a = json.load(f)
	write(a)

def write(a):
	if "unitPrice" in a[0]:
		a = sort(a)
	with open('test.html', mode='w', encoding="utf-8") as f:
		for k in a:
			f.write(str("<p>%s</p>" %k))

def sort(a):
	return sorted(a, key=lambda k: int(re.search("\\d+", k['unitPrice']).group()))

def test():
	read()

test()