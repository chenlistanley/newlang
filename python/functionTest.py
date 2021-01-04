
def test():
	def f():
		return 1
	print(f())

def test2():
	def f(a):
		return a + 1
	print(f(2))

def test3():
	def f(a, b):
		return a + b
	print(f(2, 3))

def test4():
	def f(*a):
		s=0
		for x in a:
			s += x
		return s
	print(f(2, 3, 4, 5))

def test5():
	def f(**a):
		s=0
		for v in a.values():
			s += v
		return s
	print(f(a=2, b=4, x=6, y=8))

def test6():
	def f(a,*,b):
		return a + b
	print(f(a=2, b=4))

def test7():
	f = lambda a, b : a + b
	print(f(1,2))

test7()
