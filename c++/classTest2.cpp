#include <iostream>

using namespace std;

class Person{
	string name;
	int age;

public:
	Person(string name, int age);
	void say();
};
Person::Person(string name, int age){
	this->name=name;
	this->age=age;
}
void Person::say(){
	cout << this->name << endl << this->age << endl;
}

void test(){
	Person p=Person("Stanley", 20);
	p.say();
}

int main(){
	test();
	return 0;
}