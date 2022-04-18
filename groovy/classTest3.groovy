
interface Sayer{
	def say()
}

class Person implements Sayer{
	String name
	int age

	Person(String name, int age){
		this.name = name
		this.age = age
	}

	def say(){
		println("$name $age")
	}
}

class Student extends Person{
	int grade

	Student(String name, int age, int grade){
		super(name, age)
		this.grade = grade
	}

	def say(){
		super.say()
		println(" $grade")
	}
}

def test(){
	a = new Student("Stanley", 20, 8)
	a.say()
} 
