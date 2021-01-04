#include <iostream>

using namespace std;

class Person{
	string name;
	int age;

public:
	Person(string name, int age){
		this->name=name;
		this->age=age;
	}
	void say(){
		cout << this->name << endl << this->age << endl;
	}
};

void test(){
	Person p = Person("Stanley", 20);
	p.say();
}

void test2(){
	Person p("Stanley", 18);
	p.say();
}

int main(){
	test2();
	return 0;
}