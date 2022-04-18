
Person = {}

function Person:new(name, age)
	self.name = name
	self.age = age
	return self
end

function Person:say()
	print(self.name, self.age)
end

function test()
	a = Person:new("Stanley", 20)
	a:say()
end
