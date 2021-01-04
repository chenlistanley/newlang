
class Person:
	def __init__(self, name, age):
		self.name=name
		self.age=age

	def say(self):
		print("name:%s age:%s" %(self.name, self.age))

class Student(Person):
	def __init__(self, name, age, grade):
		Person.__init__(self, name, age)
		self.grade=grade

	def say(self):
		Person.say(self)
		print("%s" %self.grade)

def test():
	p=Person("Stanley", 20)
	p.say()

def test2():
	s=Student("Stanley", 20, 3)
	s.say()

test2()