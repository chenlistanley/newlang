#include <stdio.h>

void test(){
	int a = 10;
	short a0 = 100;
	long a1 = 1000;
	float a2 = 10.99;
	double a3 = 10.99;
	char a4 = 'a';
	printf("%d %d %d %f %f %c", a, a0, a1, a2, a3, a4);
}

void main(){
	test();
}