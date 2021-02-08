import json

def record(file, size):
	with open("record.json", mode='r+') as f:
		a = json.load(f)
		start = a.get(file)
		if not start:
			start = 1
		end = start + size
		a[file] = end
		f.seek(0)
		json.dump(a, f)
		return (start, end)

def read(file, size):
	a = record(file, size)
	with open(file, mode='r', encoding="utf-8") as f:
		num = 0
		for line in f:
			num += 1
			if num < a[0] or num >= a[1]:
				continue
			print(line)
			

def test():
	read("daoDejing.txt", 3)

test()
