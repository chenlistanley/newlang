
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

def test(){
	a = new Person("Stanley", 20)
	a.say()
} 

test()
