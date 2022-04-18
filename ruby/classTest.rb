
class Person
	def initialize(name, age)
		@name = name
		@age = age
	end

	def say()
		puts "#{@name} #{@age}"
	end
end

def test()
	a = Person.new("Stanley", 20)
	a.say()
end