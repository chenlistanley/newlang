from os import listdir,chdir
from json import load
import numpy

stockNames={}
stockCodes=[]

def getFiles(count, interval, skip):
	a=[]
	files = listdir("./")
	step = interval
	start = 1 + skip * step
	end = min((count + skip) * step, len(files)) + 1
	for k in range(start, end, step):
		a.insert(0, files[-k])
	return a

def getFileData(file):
	a = {}
	with open(file, encoding="utf-8", mode='r') as f:
		data=load(f)
		for k in data:
			a.update(k)
	return a

def collectData(files):
	a = {}
	for f in files:
		d = getFileData(f)
		for k in d.keys():
			v = d[k]
			if "-" == v:
				continue
			if k in a:
				a[k].append(v)
			else:
				a[k]=[v]
	return a

def checkDiff(d):
	d1=numpy.diff(d)
	d2=numpy.diff(d1)
	return d1[-1] >= 0 and d2[-1] >= 0

def analysisData(a):
	for k in a:
		b = a[k]
		if len(b) < 3 or max(b) > 40 or numpy.median(b) > b[-1] or not checkDiff(b):
			continue
		stockCodes.append(k)

def printData(a, codes):
	for code in codes:
		if code in a and code in stockNames:
			print(code, stockNames[code], a[code][-8:])

def check(a, code):
	data = a[code]
	d1 = numpy.diff(data)
	d2 = numpy.diff(d1)
	print(d1)
	print(d2)

def test():
	stockNames.update(getFileData("name.json"))
	chdir("data")
	a = collectData(getFiles(30, 1, 0))
	analysisData(a)
	stockCodes.extend(["600036", "601166", "301187"])
	printData(a, stockCodes)

	# check(a, "301187")

test()