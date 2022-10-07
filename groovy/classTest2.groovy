
class Person{
	String name
	int age

	Person(name, age){
		this.name = name
		this.age = age
	}

	def say(){
		println("$name $age")
	}
}

class Student extends Person{
	int grade

	Student(name, age, grade){
		super(name, age)
		this.grade = grade
	}

	def say(){
		println("$name $age $grade")
	}
}

def test(){
	a = new Student("Stanley", 20, 8)
	a.say()
} 

test()
