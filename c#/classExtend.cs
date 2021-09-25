using System;

class Person{
	private string name;
	private int age;

	public Person(string name, int age){
		this.name = name;
		this.age = age;
	}

	public virtual void say(){
		Console.WriteLine("{0} {1}", this.name, this.age);
	}
}

class Student:Person{
	private int grade;

	public Student(string name, int age, int grade):base(name, age){
		this.grade = grade;
	}

	public override void say(){
		base.say();
		Console.WriteLine("{0}", this.grade);
	}
}

class Test{
	static void Main(string[] args){
		Student a = new Student("Stanley", 20, 8);
		a.say();
	}
}
