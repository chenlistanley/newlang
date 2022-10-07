from PIL import Image
import os

def test():
	os.chdir("C:/Users/stanley/Downloads")
	a = Image.open("陈松睿.jpg")
	x = int(26 * 800/25.4)
	y = int(32 * 800/25.4)
	print(x, y)
	out = a.resize((x, y), Image.ANTIALIAS)
	out.save("a.jpg")

test()