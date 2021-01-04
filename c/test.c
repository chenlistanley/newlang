#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void test1(){
	int a0 = 10;
	float a1 = 10.99;
	double a2 = 10.9999;
	char a3 = 'D';
	printf("%d %f %f %c", a0, a1, a2, a3);
}

void test2(){
	int a[] = {10, 20, 30};
	for(int i=0; i<3; i++){
		printf("%d\n", a[i]);
	}
}

void test3(){
	char a[] = "apple";
	printf("%s", a);
}

void test4(){
	char a[] = {'a', 'p', 'p', 'l', 'e', '\0'};
	printf("%s\n", a);
}

void test5(){
	const int a = 10;
	printf("%d", a);
}

struct Person{
	char* name;
	int age;
};
void test6(){
	struct Person a = {name:"Stanley", age: 20};
	printf("%s %d", a.name, a.age);
}

enum Sex{
	F,
	M
};
void test7(){
	enum Sex a = F;
	printf("%d", a);
}

void test(){
	char* a = malloc(1);
	a = realloc(a, 10);
	strcpy(a, "apple");
	printf("%s", a);
	free(a);
}

void main(){
	test();
}