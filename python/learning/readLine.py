import json,record

domain="readLine"

def read(file, begin, end):
	a = []
	with open(file, mode='r', encoding="utf-8") as f:
		num = 0
		for line in f:
			num += 1
			if num < begin or num >= end:
				continue
			a.append(line)
	return a

def manage(file, size):
	records = record.get(domain)
	begin = records.get(file)
	if not begin:
		begin = 1
	end = begin + size
	lines = read(file, begin, end)
	if len(lines) == 0:
		begin = 1
		end = begin + size
		lines = read(file, begin, end)
	for line in lines:
		print(line)
	records.update({file: end})
	record.update(domain, records)

def test():
	file = str("%s.txt" %input("File name: "))
	manage(file, 1)

test()