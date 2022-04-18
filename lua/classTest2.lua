Person={}
function Person:new(name, age)
	self.name = name
	self.age = age
	return self
end

function Person:say()
	print(self.name, self.age)
end

Student=Person:new(name, age)
function Student:new(name, age, grade)
	self.name = name
	self.age = age
	self.grade = grade
	return self
end

function Student:say()
	print(self.name, self.age, self.grade)
end

function test()
	a = Student:new("Stanley", 20, 8)
	a:say()
end