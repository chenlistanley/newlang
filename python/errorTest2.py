
class MyError(Exception):
	def __init__(self, code, message):
		self.code=code
		self.message=message

	def __str__(self):
		return str("%s %s" %(self.code, self.message))

def test():
	raise MyError("S800", "testing error")

def test2():
	try:
		raise MyError("S800", "testing error")
	except MyError as e:
		print("error", e)

test2()