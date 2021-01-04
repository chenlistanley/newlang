#include <iostream>

using namespace std;


class Person
{
	string name;
	int age;

public:
	Person(string name, int age){
		this->name=name;
		this->age=age;
	}
	void say(){
		cout << this->name << endl;
		cout << this->age << endl;
	}
};

class Student: Person{
	int grade;

public:
	Student(string name, int age, int grade):Person(name, age){
		this->grade=grade;
	}
	void say(){
		Person::say();
		cout << this->grade << endl;
	}
};

void test(){
	Student s = Student("Stanley", 20, 8);
	s.say();
}

int main(){
	test();
	return 0;
}