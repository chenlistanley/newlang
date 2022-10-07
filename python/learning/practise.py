import json,record
from datetime import date

domain='practise'

def loadjson(file):
	a = {}
	with open(file, mode='r') as f:
		a = json.load(f)
	return a

def choose(records, frequence, subjects):
	if len(subjects) == 0:
		return
	daySubject = {}
	for subject in subjects:
		if subject not in records:
			return subject
		delta = date.today() - date.fromisoformat(records[subject])
		daySubject.update({delta.days: subject})
	days = max(daySubject.keys())
	subject = daySubject[days]
	if 'yearly' == frequence and days >= 365:
		return subject
	elif 'monthly' == frequence and days >= 30:
		return subject
	elif 'weekly' == frequence and days >= 7:
		return subject
	elif 'daily' == frequence:
		return subject

def update(records, subject):
	records.update({subject: date.today().isoformat()})
	record.update(domain, records)

def manage(file):
	subjects = loadjson(file)
	records = record.get(domain)
	for frequence in ('yearly', 'monthly', 'weekly', 'daily'):
		subject = choose(records, frequence, subjects[frequence])
		if subject:
			update(records, subject)
			print(subject)
			return

def test():
	file = str("%s.json" %input("File name: "))
	manage(file)

test()