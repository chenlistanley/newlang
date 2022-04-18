import json
from datetime import date

recordFile = "record.json"

def read():
	try:
		with open(recordFile, mode='r') as f:
			return json.load(f)
	except:
		return {}

def write(records):
	with open(recordFile, mode='w') as f:
		json.dump(records, f)

def get(domain):
	records = read()
	domains = {}
	if domain in records:
		domains = records[domain]
	return domains

def update(domain, domains):
	records = read()
	records.update({domain: domains})
	write(records)
