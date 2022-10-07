
def format(line):
	s = line.strip()
	s = s.split(" ")
	print(str("'%s'" %s[1]), end=", ")

def test():
	a=open("a.txt", encoding="utf-8")
	for line in a:
		print(str('"%s"' %line.strip()), end=", ")
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
	with open("a.txt", encoding="utf-8") as a:
		for line in a:
			format(line)

test5()

