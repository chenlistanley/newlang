
class Person
	def initialize(name, age)
		@name = name
		@age = age
	end

	def say()
		puts "#{@name} #{@age}"
	end
end

class Student < Person
	def initialize(name, age, grade)
		super(name, age)
		@grade = grade
	end

	def say()
		puts "#{@name} #{@age} #{@grade}"
	end
end

def test()
	a = Student.new("Stanley", 20, 8)
	a.say()
end
