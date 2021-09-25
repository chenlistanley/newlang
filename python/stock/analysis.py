from os import listdir,chdir
from json import load

names = []

def look_file(count, interval, skip):
	a=[]
	files = listdir("./")
	step = interval
	start = 1 + skip * step
	end = min((count + skip) * step, len(files)) + 1
	for k in range(start, end, step):
		a.insert(0, files[-k])
	return a

def look_data(file):
	a = {}
	with open(file, encoding="utf-8", mode='r') as f:
		data=load(f)
		for k in data:
			a.update(k)
	return a

def lookup(files):
	a = {}
	for f in files:
		d = look_data(f)
		for k in d.keys():
			v = d[k]
			if "-" == v:
				continue
			if k in a:
				a[k].append(v)
			else:
				a[k]=[v]
	return a

def half_up(a):
	if a[0] < 10 or a[0] > 30:
		return False
	b = a[0]
	c = a[0]
	for k in range(1, len(a)):
		b = b * (1 + 0.03)
		c = c * (1 + 0.04)
	if a[-1] >= b and a[-1] <= c:
		return True
	return False

def simple_up(a):
	m = {}
	for k in a:
		b = a[k]
		if not half_up(b):
			continue
		m[k] = b
	for k in m:
		print(k, names[k], m[k])

def check(a, *codes):
	for code in codes:
		if code in a:
			print(code, names[code], a[code])

def test():
	global names
	names = look_data("name.json")
	chdir("data")
	print("---daily---")
	files = look_file(10, 1, 0)
	a = lookup(files)
	simple_up(a)
	print("---check---")
	check(a, "601988", "600036", "601166", "600016")

test()