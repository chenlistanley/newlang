from os import listdir,chdir
from json import load
import numpy

stockNames={}
stockCodes=[]

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

def simple_up(a):
	for k in a:
		b = a[k]
		if len(b) < 3 or b[-1] < numpy.percentile(b, 90):
			continue
		stockCodes.append(k)

def check(a, codes):
	for code in codes:
		if code in a:
			print(code, stockNames[code], a[code][-8:])

def test():
	stockNames.update(look_data("name.json"))
	chdir("data")
	a = lookup(look_file(15, 1, 0))
	simple_up(a)
	stockCodes.extend(["601988", "600036", "601166", "600016"])
	check(a, stockCodes)

test()