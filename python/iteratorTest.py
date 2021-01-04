import sys

def test():
	a=(1,3,7,2,12)
	b=iter(a)
	while True:
		try:
			print(next(b))
		except StopIteration:
			sys.exit()

def test2():
	a=(1,3,7,2,12)
	b=iter(a)
	for x in b:
		print(x)

test2()