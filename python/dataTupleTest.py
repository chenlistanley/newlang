
def test():
	a=("apple", "banana")
	for x in a:
		print(x)

def test2():
	a=("apple", "banana")
	if "apple" in a:
		print("apple")

def test3():
	a=tuple("apple")
	print(a)

def test4():
	a=tuple(["apple", "banana"])
	print(a)

def test5():
	a=tuple({"apple", "banana"})
	print(a)

def test6():
	a=("apple", "banana", "orange", "pear")
	print(a[0])
	print(a[1:])
	print(a[:-1])

def test7():
	a=("apple", "banana", "orange", "banana")
	print(len(a))
	print(a.index("banana"))
	print(a.count("banana"))

def test10():
	a=(1, 3, 5, 7)
	print("min: %d" % min(a))
	print("max: %d" % max(a))

test7()