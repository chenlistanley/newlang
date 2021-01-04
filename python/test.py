import re

def test1():
	a0 = 10
	a1 = 10.99
	a2 = True
	a3 = "apple"
	a4 = 'apple'
	print(a0, a1, a2, a3, a4)

def test2():
	a = ["apple", "banana"]
	a.append("orange")
	for k in a:
		print(k)

def test3():
	a = {"apple", "banana"}
	a.add("apple")
	for k in a:
		print(k)

def test4():
	a = {"A":"apple", "B":"banana"}
	a["O"] = "orange"
	for k in a.keys():
		print(k, a[k])

def test5():
	a = ("apple", "banana")
	for k in a:
		print(k)

def test6():
	try:
		a = 1/0
	except Exception as e:
		print(e)

def test7():
	try:
		raise Exception("apple")
	except Exception as e:
		print(e)

def test8():
	class Person:
		def __init__(self, name, age):
			self.name = name
			self.age = age

		def say(self):
			print(self.name, self.age)

	a = Person("Stanley", 20)
	a.say()

def test9():
	class Person:
		def __init__(self, name, age):
			self.name = name
			self.age = age

		def say(self):
			print(self.name, self.age)

	class Student(Person):
		def __init__(self, name, age, glade):
			Person.__init__(self, name, age)
			self.glade = glade
		def say(self):
			Person.say(self)
			print(self.glade)

	a = Student("Stanley", 20, 8)
	a.say()

def test10():
	class Ne(Exception):
		def __init__(self, code, message):
			self.code = code
			self.message = message

		def __str__(self):
			return str("%s %s"%(self.code, self.message))

	try:
		raise Ne("S998", "apple")
	except Ne as e:
		print(e)
	finally:
		print("orange")

def test11():
	a = re.match("apple", "apple")
	if a:
		print(a.group())
	else:
		print("NG")

def test12():
	a = re.search("apple", "banana apple orange")
	if a:
		print(a.group())

def test13():
	a = re.findall("apple", "apple banana orange apple")
	print(a)

def test14():
	a = re.finditer("apple", "apple banana orange apple")
	for k in a:
		print(k.group())

def test15():
	a = re.sub("apple", "pear", "apple banana orange apple")
	print(a)

def test16():
	a = re.sub("apple", lambda a : a.group()[:3], "apple banana orange apple")
	print(a)

def test17():
	a = re.split(" ", "apple banana orange apple")
	print(a)

def test18():
	def fa(*a):
		print(a)
	fa("apple", "banana")

def test19():
	def fa(**a):
		print(a)
	fa(a="apple", b="banana")

def test20():
	def fa(a, *, b):
		print(a, b)
	fa(a="apple", b="orange")

def test():
	fa = lambda a, b : print(a, b)
	fa("apple", "orange")

test()