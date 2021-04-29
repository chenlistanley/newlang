
def test():
	try:
		a=2/0
	except ZeroDivisionError:
		print("error")

def test2():
	try:
		a=2/0
	except ZeroDivisionError as e:
		print("error", e)

def test3():
	try:
		a=2/0
	except Exception as e:
		print("error", e)

def test4():
	try:
		a=2/2
	except Exception as e:
		print("error", e)
	else:
		print(a)

def test5():
	try:
		a=2/2
	except Exception as e:
		print("error", e)
	else:
		print(a)
	finally:
		print(a, a)

def test6():
	try:
		a=2/0
	except Exception as e:
		print("error", e)
		a=-1
	else:
		print(a)
	finally:
		print(a, a)

def test7():
	try:
		raise Exception("testing error")
	except Exception as e:
		print("error", e)
		a=-1
	else:
		print(a)
	finally:
		print(a, a)

test7()