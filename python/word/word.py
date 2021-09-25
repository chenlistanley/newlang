import random

def read(file):
	words = []
	with open(file, mode='r', encoding="utf-8") as f:
		for k in f:
			word = k.strip()
			if word == "":
				continue
			words.append(word)
	return words

def save(file, words):
	with open(file, mode='w', encoding="utf-8") as f:
		for k in words:
			f.write("%s\n" %k)

def pick(src, excludes, size):
	a = []
	srcLen = len(src)
	for k in range(srcLen):
		b = src[random.randint(0, srcLen)]
		if b not in excludes:
			a.append(b)
		if len(a) >= size:
			break
	return a

def test():
	words = read("word.txt")
	remembers = read("remember.txt")
	practises = read("practise.txt")
	size = 50
	left = size - len(practises)
	if left > 0:
		practises += pick(remembers, practises, left >> 1)

	left = size - len(practises)
	if left > 0:
		practises += pick(words, remembers + practises, left)

	for k in tuple(practises):
		print("\n%s" %k)
		s = input("")
		while s != k:
			s = input("")
		s = input("Remember (Y/y): ")
		if s == "Y" or s == 'y':
			remembers.append(k)
			practises.remove(k)
		elif k in remembers:
			remembers.remove(k)
	
	save("remember.txt", remembers)
	save("practise.txt", practises)

test()