#include <stdio.h>

union Person{
	char* name;
	int age;
};

void test(){
	union Person a = {age: 30};
	printf("%d", a.age);
}

void test2(){
	union Person a = {name: "Stanley"};
	printf("%s", a.name);
}

void main(){
	test2();
}