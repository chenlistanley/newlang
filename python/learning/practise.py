import json,record
from datetime import date

domain='practise'

def loadjson(file):
	a = {}
	with open(file, mode='r') as f:
		a = json.load(f)
	return a

def choose(records, subject, frequence):
	if subject in records:
		delta = date.today() - date.fromisoformat(records[subject])
		if 'yearly' == frequence:
			return delta.days >= 365
		elif 'monthly' == frequence:
			return delta.days >= 30
		elif 'weekly' == frequence:
			return delta.days >= 7
		else:
			return delta.days >= 1
	return True

def update(records, subject):
	records.update({subject: date.today().isoformat()})
	record.update(domain, records)

def manage(file):
	subjects = loadjson(file)
	records = record.get(domain)

	for frequence in ("yearly", "monthly", "weekly", "daily"):
		if frequence in subjects:
			for subject in subjects[frequence]:
				if choose(records, subject, frequence):
					update(records, subject)
					print(subject)
					return

def test():
	file = str("%s.json" %input("File name: "))
	manage(file)

test()