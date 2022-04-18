import random,record

def read(file):
	words = []
	with open(file, mode='r', encoding="utf-8") as f:
		for k in f:
			word = k.strip()
			if word == "" or word in words:
				continue
			words.append(word)
	return words

def pick(src, excludes, size):
	dst = []
	srcLen = len(src)
	for k in range(srcLen):
		srcIndex = random.randint(0, srcLen)
		if srcIndex >= srcLen:
			srcIndex = 0
		b = src[srcIndex]
		if b not in excludes and b not in dst:
			dst.append(b)
		if len(dst) >= size:
			break
	return dst

def manage(file, size):
	words = read(file)
	records = record.get(file)
	remembers = records.get('remembers')
	if not remembers:
		remembers = []
	practises = records.get('practises')
	if not practises:
		practises = []
	remain = size - len(practises)
	if remain > 0:
		practises += pick(remembers, practises, remain >> 1)

	remain = size - len(practises)
	if remain > 0:
		practises += pick(words, remembers + practises, remain)

	for k in set(practises):
		print("\n%s" %k, end=" ")
		s = input("")
		while s != k:
			s = input("")
		s = input("Remember (y/n): ")
		if s == "Y" or s == 'y':
			remembers.append(k)
			practises.remove(k)
		elif k in remembers:
			remembers.remove(k)
	
	print(str("completed %s" %(len(practises))))
	records.update({"remembers": remembers})
	records.update({"practises": practises})
	record.update(file, records)

def test():
	manage("word.txt", 50)

test()