
def test():
	a={"apple", "banana"}
	for x in a:
		print(x)

def test2():
	a={"apple", "banana"}
	a.add("orange")
	print(a)

def test3():
	a={"apple", "banana"}
	a.update({"orange"})
	print(a)

def test4():
	a={"apple", "banana"}
	if "apple" in a:
		a.remove("apple")
	print(a)

def test5():
	a={"apple", "banana"}
	a.discard("apple")
	print(a)

def test6():
	a={"apple", "banana"}
	a.pop()
	print(a)

def test7():
	a={"apple", "banana"}
	a.clear()
	print(a)

def test8():
	a=set()
	print(a)

def test9():
	a=set("apple")
	print(a)

def test10():
	a=set(["apple", "banana"])
	print(a)

def test11():
	a=set(("apple", "banana"))
	print(a)

def test12():
	a={"apple", "banana"}
	print(len(a))

def test13():
	a={"apple", "banana"}
	b={"apple", "orange"}
	print(a.union(b))

def test14():
	a={"apple", "banana"}
	b={"apple", "orange"}
	print(a.intersection(b))

def test15():
	a={"apple", "banana"}
	b={"apple", "orange"}
	print(a.difference(b))

def test16():
	a={"apple", "banana"}
	b={"apple", "orange"}
	print(a.symmetric_difference(b))

def test17():
	a={1, 3, 5, 7, 9}
	print("min: %d" % min(a))
	print("max: %d" % max(a))

test12()
