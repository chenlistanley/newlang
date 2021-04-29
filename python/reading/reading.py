import json

json_file = "record.json"

def load_record():
	a = {}
	with open(json_file, mode='r') as f:
		a = json.load(f)
	return a

def save_record(k, v):
	a = load_record()
	with open(json_file, mode='w') as f:
		a[k] = v
		json.dump(a, f)

def read(file, start, end):
	a = []
	with open(file, mode='r', encoding="utf-8") as f:
		num = 0
		for line in f:
			num += 1
			if num < start or num >= end:
				continue
			a.append(line)
	return a

def manage(file, size):
	a = load_record()
	start = a.get(file)
	if not start:
		start = 1
	end = start + size
	b = read(file, start, end)
	if len(b) == 0:
		start = 1
		end = start + size
		b = read(file, start, end)
	for k in b:
		print(k)
	save_record(file, end)


def test():
	filename = str("%s.txt" %input("File name: "))
	# linenum = int(input("Line num: "))
	linenum = 1
	manage(filename, linenum)

test()