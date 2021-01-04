#include <stdio.h>

struct Person
{
	char* name;
	int age;
};

void test(){
	struct Person a;
	a.name="Stanley";
	a.age=20;
	
	printf("%s %d", a.name, a.age);
}

void test2(){
	struct Person a={name: "Stanley", age:20};
	printf("%s %d", a.name, a.age);
}

void test3(){
	struct Person a={"Stanley", 20};
	printf("%s %d", a.name, a.age);
}

void test4(){
	struct Person a={name: "Stanley", age:20};
	struct Person *p;
	p=&a;
	printf("%s %d", p->name, p->age);
}

void main(){
	test4();
}