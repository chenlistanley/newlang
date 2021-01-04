#include <stdio.h>
#include <string.h>

void test(){
	char a[20]={};
	strcpy(a, "apple");
	printf("%s", a);
	
}

void test2(){
	char a[20]="apple";
	strcat(a, " banana");
	printf("%s", a);
}

void test3(){
	int a= strcmp("apple", "banana");
	printf("%d", a);
}

void main(){
	test3();
}