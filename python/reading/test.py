import re

def read():
	with open("a.txt", encoding="utf-8") as f:
		for line in f:
			if line.strip() == "":
				continue
			s = line
			s = re.sub("【[^】]*】", "", s)
			write(s)

def write(s):
	with open("b.txt", mode="a", encoding="utf-8") as f:
		f.write(s)

def test():
	read()

test()
