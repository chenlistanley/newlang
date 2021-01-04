#include <stdio.h>

void test(){
	printf("%s", "apple");
}

void test2(){
	char a = getchar();
	printf("%c", a);
}

void test3(){
	putchar('a');
}

void test4(){
	char a[10];
	gets(a);
	printf("%s", a);
}

void test5(){
	char a[]="apple";
	puts(a);
}

void test6(){
	char a[10];
	scanf("%s", a);
	printf("%s", a);
}

void main(){
	test6();
}



