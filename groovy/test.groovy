
interface Sayer{
	def say()
}

class Person<R, S> implements Sayer{
	R name
	S age

	Person(R name, S age){
		this.name = name
		this.age = age
	}

	def say(){
		println("$name $age")
	}
}

class Student<R, S, T> extends Person<R, S>{
	T grade

	Student(R name, S age, T grade){
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

test()
