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
	a = set(src).difference(set(excludes))
	return list(a)[:size]

def manage(file, rememberCount, practiseCount, count):
	words = read(file)
	records = record.get(file)
	remembers = []
	practises = []
	if 'remembers' in records:
		remembers = records['remembers']
	if 'practises' in records:
		practises = records['practises']
	work = pick(practises, [], practiseCount)
	work.extend(pick(remembers, work, rememberCount))
	work.extend(pick(words, work, count))
	work = set(work)
	print(len(work))
	for k in work:
		print("\n%s" %k, end=" ")
		s = input("")
		while s != k:
			s = input("")
		s = input("Remember (y/n): ")
		if s == "Y" or s == 'y':
			if k not in remembers:
				remembers.append(k)
			if k in practises:
				practises.remove(k)
		else:
			if k in remembers:
				remembers.remove(k)
			if k not in practises:
				practises.append(k)
	records={"remembers": remembers, "practises": practises}
	record.update(file, records)

def test():
	manage("word.txt", 2, 5, 3)
test()