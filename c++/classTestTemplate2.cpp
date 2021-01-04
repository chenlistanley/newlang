#include <iostream>

using namespace std;

template <class T1, class T2>
class Person{
	T1 name;
	T2 age;

public:
	Person(T1 name, T2 age){
		this->name = name;
		this->age = age;
	}

	void say(){
		cout << this->name << endl << this->age << endl;
	}
};

template<class T1, class T2, class T3>
class Student: public Person<T1, T2>{
	T3 grade;

public:
	Student(T1 name, T2 age, T3 grade):Person<T1, T2>(name, age){
		this->grade=grade;
	}
	void say(){
		Person<T1,T2>::say();
		cout << this->grade << endl;
	}
};

void test(){
	Student<string, int, int> a("Stanley", 20, 8);
	a.say();
}

int main(){
	test();
	return 0;
}
