using System;

class Person{
	private string name;
	private int age;

	public Person(string name, int age){
		this.name = name;
		this.age = age;
	}

	public void say(){
		Console.WriteLine("{0} {1}", this.name, this.age);
	}
}

class Test{
	static void Main(string[] args){
		Person a = new Person("Stanley", 20);
		a.say();
	}
}
