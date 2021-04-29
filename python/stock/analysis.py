from os import listdir
from json import load
from math import ceil
import os

def look_file(days):
	a=[]
	files = listdir("./")
	for k in files:
		if k.endswith(".json"):
			a.append(k)
	return a[-days:]

def look_data(file):
	a = {}
	with open(file, 'r') as f:
		data=load(f)
		for k in data:
			a.update(k)
		return a

def lookup(days):
	a = {}
	files = look_file(days)
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

def all_up(a):
	for k in a:
		b = a[k].copy()
		b.sort()
		if a[k] == b:
			print(k, a[k])

def half_up(a):
	h = ceil(len(a)/2)
	a1 = a[:h]
	a2 = a[-h:]
	a3 = a[h:]
	if sum(a1) >= sum(a2):
		return False
	if len(a3) > 1:
		return half_up(a3)
	return True

def simple_up(a):
	for k in a:
		b = a[k]
		if min(b) > 20 or min(b) < 5:
			continue
		if not half_up(b):
			continue
		if len(b) < 2 or b[-2] / b[-1] < 0.91:
			continue
		print(k, b)

def check(a, code):
	if code in a:
		print(code, a[code])

def test():
	os.chdir("data")
	a = lookup(5)
	simple_up(a)
	print("------")
	a = lookup(10)
	check(a, "601988")
	check(a, "600036")
	check(a, "601166")
	check(a, "600016")

test()