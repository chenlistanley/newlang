
def test():
	a={"A":"apple", "B":"banana"}
	for k in a.keys():
		print(k, a[k])

def test2():
	a={"A":"apple", "B":"banana"}
	a["O"]="orange"
	print(a)

def test3():
	a={"A":"apple", "B":"banana"}
	if 'A' in a:
		del a["A"]
	print(a)

def test4():
	a={"A":"apple", "B":"banana"}
	a.clear()
	print(a)

def test5():
	a={"A":"apple", "B":"banana"}
	print(len(a))

def test6():
	a={}
	print(a)

def test7():
	a=dict()
	print(a)

def test8():
	a={"A":"apple", "B":"banana"}
	for v in a.values():
		print(v)

test5()