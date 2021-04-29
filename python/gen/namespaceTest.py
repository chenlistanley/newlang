
a=1

def change():
	a=100

def change2():
	global a
	a=100

def change3():
	a=100
	def change():
		a=200
		print(a)
	change()
	print(a)

def change4():
	a=100
	def change():
		nonlocal a
		a=200
		print(a)
	change()
	print(a)

def test():
	change()
	print(a)

def test2():
	change2()
	print(a)

def test3():
	change3()
	print(a)

def test4():
	change4()
	print(a)

test4()
