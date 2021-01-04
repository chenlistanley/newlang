import os, sys, shutil, re

def test():
	path = "d:/test"
	dest = path + "/a"
	os.chdir(path)
	# os.rmdir(dest)
	os.mkdir(dest)
	a = os.listdir("d:/test")
	for k in a:
		if k == "1.txt":
			shutil.copy2(k, dest)
		print(k)

test()