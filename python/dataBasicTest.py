
def test():
	a0 = 10
	a1 = 10.25
	a2 = "apple"
	a3 = True
	a4 = 10+3j

	print(a0, type(a0), isinstance(a0, int))
	print(a1, type(a1), isinstance(a1, float))
	print(a2, type(a2), isinstance(a2, str))
	print(a3, type(a3), isinstance(a3, bool))
	print(a4, type(a4), isinstance(a4, complex))

test()