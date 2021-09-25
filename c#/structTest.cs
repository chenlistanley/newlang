using System;

struct Person{
	public string name;
	public int age;
}

class Test{
	static void Main(string[] args){
		Person a;
		a.name = "Stanley";
		a.age = 20;
		Console.WriteLine("{0} {1}", a.name, a.age);
	}
}