import json

def test():
	a={'name':'Bill', 'age':18}
	print(a)
	print(repr(a))
	print(str(a))

def test2():
	a={'name':'Bill', 'age':18}
	print(json.dumps(a))

def test3():
	a={'name':'Bill', 'age':18}
	b=json.dumps(a)
	print(json.loads(b))

def test4():
	a={'name':'Bill', 'age':18}
	with open('data/person.json','w') as f:
	    json.dump(a, f)

def test5():
	with open('data/person.json','r') as f:
	    a=json.load(f)
	    print(a)
	    print(json.dumps(a))

test5()