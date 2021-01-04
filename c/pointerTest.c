#include <stdio.h>

void test(){
	int a=10;
	int *b;
	b=&a;
	printf("%d\n", a);
	printf("%d\n", *b);
}

void main(){
	test();
}