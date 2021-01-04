#include <iostream>
using namespace std;

template<class T, class T2>
class Person{
	T name;
	T2 age;
public:
	Person(T name, T2 age){
		this->name=name;
		this->age=age;
	}
	void say(){
		cout << this->name << endl;
		cout << this->age  << endl;
	}
};

void test(){
	Person<string, int> p=Person<string, int>("Stanley", 20);
	p.say();
}

void test2(){
	Person<string, int> p("Stanley", 20);
	p.say();
}


int main()
{
	test2();
    return 0;
}