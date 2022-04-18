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

def test(){
	a = new Person("Stanley", 20)
	a.say()
} 