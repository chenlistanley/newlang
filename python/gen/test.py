import re

def test():
	a = "apple banana"
	a = re.search("c", a).group()
	print(a)

test() 
