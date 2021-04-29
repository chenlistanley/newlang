
def check(a=''):
	if a == 'a':
		print('Apple')
	elif a == 'b':
		print('Banana')
	elif a == 'o':
		print('Orange')
	else:
		print('others')

def test():
	check('a')

def test2():
	check('b')

def test3():
	check('o')

def test4():
	check()

def test5():
	a=['Apple','Banana','Orange']
	if 'Apple' in a:
		print('Yes, I would like one')
	else:
		print("No, thanks")

def test6():
	if 'a' in "Banana":
		print("Yes")
	else:
		print("No")

test6()