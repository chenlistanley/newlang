import zlib

def test():
	a=b'hello world hello world hello world hello world'
	b=zlib.compress(a)
	print(len(a) - len(b))

def test2():
	a=b'hello world hello world hello world hello world'
	b=zlib.compress(a)
	c=zlib.decompress(b)
	print(a==c)

def test3():
	a=b'hello world hello world hello world hello world'
	b=zlib.crc32(a)
	print(b)

test3()