#include <iostream>
using namespace std;

class Sayer{
	virtual void say()=0;
	virtual void say(string words)=0;
};

class Person: Sayer{
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
	void say(string words){
		cout << words << endl;
	}
};

void test(){
	Person p = Person("Stanley", 20);
	p.say();
	p.say("apple");
}

int main(){
	test();
    return 0;
}