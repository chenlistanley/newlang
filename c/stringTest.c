#include <stdio.h>

void test(){
	char a[]="apple";
	printf("%s\n", a);
}

void test2(){
	char a[10]="apple";
	printf("%s\n", a);
}

void test3(){
	char a[10]={'a', 'p', 'p', 'l', 'e', '\0'};
	printf("%s\n", a);
}

void test4(){
	char *a="apple";
	printf("%s\n", a);
}

void main(){
	test();
}