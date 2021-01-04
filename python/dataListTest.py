
def test():
	a=["apple", "banana"]
	for x in a:
		print(x)

def test2():
	a=["apple", "banana"]
	a.insert(1, "pear")
	a.append("orange")
	a.extend(("guava", "longan"))
	print(a)

def test3():
	a=["apple", "banana"]
	if "apple" in a:
		a.remove("apple")
	print(a)

def test4():
	a=["apple", "banana"]
	a[0]="orange"
	del a[1]
	print(a)

def test5():
	a=["apple", "banana"]
	a.clear()
	print(a)

def test6():
	a=["apple", "banana"]
	print(len(a))
	print(a.index("apple"))
	print(a.count("apple"))

def test7():
	a=["apple", "banana", "pear", "orange", "longan", "guava"]
	a.sort()
	print(a)

def test8():
	a=["apple", "banana"]
	a.reverse()
	print(a)

def test9():
	a=["apple", "banana"]
	a.pop()
	print(a)

def test10():
	a=["apple", "banana", "pear", "orange", "longan", "guava"]
	print(a.copy())
	print(a[1:])
	print(a[:-1])

def test11():
	a=list()
	print(a)

def test12():
	a=list(("apple", "banana"))
	print(a)

def test13():
	a=list({"apple", "banana"})
	print(a)

def test14():
	a=["apple", "banana"]
	b=["apple", "orange"]
	print(a + b)

def test15():
	a=[1, 3, 5, 7, 9]
	print(min(a))

def test16():
	a=[1, 3, 5, 7, 9]
	print(max(a))

test3()