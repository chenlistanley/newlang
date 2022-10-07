import re

def test():
	a = re.match("\\S*a\\S*", "apple banana")
	if a:
		print(a.group())

def test2():
	a = re.search("\\S*a\\S*", "apple banana")
	if a:
		print(a.group())

def test3():
	a = re.sub("\\S*a\\S*", "orange", "apple banana")
	print(a)

def test4():
	a = re.sub("\\S*a\\S*", lambda a: a.group()[:3]  , "apple banana")
	print(a)

def test5():
	a = re.findall("\\S*a\\S*", "apple banana")
	print(a)

def test6():
	a = re.finditer("\\S*a\\S*", "apple banana")
	for k in a:
		print(k.group())

def test7():
	a = re.split("\\W", "apple banana")
	print(a)

def test8():
	a = re.compile("\\S*a\\S*").match("apple banana")
	if a:
		print(a.group())

def test9():
	a=re.compile("\\S*a\\S*").search("apple banana")
	if a:
		print(a.group())

def test10():
	a=re.compile("\\S*a\\S*").sub("orange", "apple banana")
	print(a)

def test11():
	a=re.compile("\\S*a\\S*").findall("apple banana")
	print(a)

def test12():
	a=re.compile("\\S*a\\S*").finditer("apple banana")
	for k in a:
		print(k.group())

test()
