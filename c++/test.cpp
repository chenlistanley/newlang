#include <iostream>
#include <exception>
#include <string.h>

using namespace std;

void test1(){
	int a0 = 10;
	float a1 = 10.99;
	double a2 = 10.9999;
	char a3 = 'D';
	string a4 = "apple";
	cout << a0 << " " << a1 << " " << a2 << " " << a3 << " " << a4;
}

void test2(){
	int a[] = {10, 20, 30};
	for(int i=0; i<3; i++){
		cout << a[i] << endl;
	}
}

void test3(){
	char a[] = "apple";
	cout << a;
}

void test4(){
	const string a = "apple";
	cout << a;
}


void test5(){
	enum Sex{
		F,
		M
	};
	Sex a = M;
	cout << a;
}


void test6(){
	struct Person{
		string name;
		int age;
	};
	Person a = {name:"Stanley", age:20};
	cout << a.name << " " << a.age;
}

void test7(){
	class Person{
		string name;
		int age;

	public:
		Person(string name, int age){
			this->name = name;
			this->age = age;
		}
		void say(){
			cout << this->name << " " << this->age;
		}
	};

	Person a = Person("Stanley", 20);
	a.say();
}

void test8(){
	class Sayer{
		virtual void say() = 0;
	};
	class Person : Sayer{
		string name;
		int age;

	public:
		Person(string name, int age){
			this->name = name;
			this->age = age;
		}
		void say(){
			cout << this->name << " " << this->age;
		}
	};

	Person a = Person("Stanley", 20);
	a.say();
}

void test9(){
	class Person{
		string name;
		int age;

	public:
		Person(string name, int age){
			this->name = name;
			this->age = age;
		}
		void say(){
			cout << this->name << " " << this->age;
		}
	};
	class Student:Person{
		int glade;
	public:
		Student(string name, int age, int glade):Person(name, age){
			this->glade = glade;
		}
		void say(){
			Person::say();
			cout << " " << this->glade;
		}
	};

	Student a = Student("Stanley", 20, 8);
	a.say();
}

template<class T, class S>
class Person{
	T name;
	S age;

public:
	Person(T name, S age){
		this->name = name;
		this->age = age;
	}
	void say(){
		cout << this->name << " " << this->age;
	}
};
void test10(){
	Person<string,int> a = Person<string,int>("Stanley", 20);
	a.say();
}

void test11(){
	try{
		throw "apple error";
	}catch(const char* e){
		clog << e;
	}
}

void test12(){
	try{
		throw exception();
	}catch(exception e){
		clog << e.what();
	}
}

void test13(){
	struct ne:exception{
		const char* what() const throw(){
			return "apple";
		}
	};
	try{
		throw ne();
	}catch(ne e){
		clog << e.what();
	}
}

void test14(){
	int* a;
	a = new int;
	*a = 10;
	cout << *a;
	delete a;
}

void test(){
	char* a;
	a = new char[10];
	strcpy(a, "apple");
	cout << a;
	delete []a;
}

int main(){
	test();
	return 0;
}
