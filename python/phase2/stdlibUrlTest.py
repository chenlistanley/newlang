from urllib.request import urlopen

def test():
	for line in urlopen("https://www.runoob.com/python3/python3-tutorial.html"):
		line=line.decode("utf-8")
		if "Hello" in line or "World" in line:
			print(line)

test()