a = "apple BANANA"

def test():
	print(a.upper())

def test2():
	print(a.lower())

def test3():
	print(a.capitalize())

def test4():
	print(a.title())

def test5():
	print(a.swapcase())

def test6():
	a = " apple"
	print(a.lstrip())

def test7():
	a = "apple "
	print(a.rstrip())
	
def test8():
	a = " apple "
	print(a.strip())

def test9():
	print(a.replace('B','b'))

def test10():
	print(a.zfill(20))

def test11():
	a = "apple \n apple"
	print(a.splitlines())

def test12():
	print(a.split(' '))

def test13():
	print(a.find('p'))

def test14():
	print(a.rfind('p'))

def test15():
	print(a.index('p'))

def test16():
	print(a.rindex('p'))

def test17():
	print(a.startswith('app'))

def test18():
	print(a.endswith('NA'))

def test19():
	print(a.isalpha())

def test20():
	print(a.isalnum())

def test21():
	a="000"
	print(a.isdigit())

def test22():
	a="000"
	print(a.isnumeric())

def test23():
	print(a.islower())

def test24():
	print(a.isupper())

def test25():
	print(max(a))

def test26():
	print(min(a))

def test27():
	print(set(a))

def test28():
	print(list(a))

def test29():
	print(tuple(a))

def test30():
	print(a * 2)

def test31():
	print(a + a)

test11()