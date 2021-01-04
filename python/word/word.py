
def load(file, size):
	a = []
	with open(file, mode='r', encoding="utf-8") as f:
		for k in f:
			word = k.strip()
			if word == "":
				continue
			a.append(word)
			if len(a) == size:
				break
	return a

def save(file, words):
	with open(file, mode='a', encoding="utf-8") as f:
		for k in words:
			f.write("%s\n" %k)

def delete(file, words):
	a = []
	with open(file, mode='r', encoding="utf-8") as f:
		for k in f:
			word = k.strip()
			if word not in words:
				a.append(word)
	
	with open(file, mode='w', encoding="utf-8") as f:
		for k in a:
			f.write("%s\n" %k)

def test():
	s = input("Please key number of size: ")
	s = int(s)
	a = load("toSave.txt", s)
	b = []
	for k in a:
		print(k)
		s = input("Please key 'Y' if remember: ")
		if s == "Y" or s == 'y':
			b.append(k)
	save("saved.txt", b)
	delete("toSave.txt", b)


test()