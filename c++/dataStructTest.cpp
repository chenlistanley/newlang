#include <iostream>

using namespace std;

struct Person{
	string name;
	int age;
};

void test(){
	Person p;
	p.name="Stanley";
	p.age=18;
	cout << p.name << endl << p.age;
}

void test2(){
	Person p = Person{name: "Stanley", age: 20};
	cout << p.name << endl << p.age;
}

void test3(){
	Person p = {name: "Stanley", age: 20};
	cout << p.name << endl << p.age;
}

void test4(){
	Person p{name: "Stanley", age: 20};
	cout << p.name << endl << p.age;
}

int main(){
	test4();
	return 0;
}