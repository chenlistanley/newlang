
def test():
	a=open("data/test.txt", encoding="utf-8")
	for line in a:
		print(line, end="")
	a.close()

def test2():
	a=open("data/test.txt", mode='w')
	for k in ("Apple", "Banana", "Orange"):
		a.write(k + "\n")
	a.close()

def test3():
	a=open("data/test.txt", mode='a')
	for k in ("Pear", "Guava", "Grape"):
		a.write(k + "\n")
	a.close()

def test4():
	a=open("data/test.txt")
	print(a.read())
	a.close()

def test5():
	with open("data/test.txt") as a:
		for line in a:
			print(line)

test5()

