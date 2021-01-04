#include <stdio.h>

void test(){
	void f(){
		printf("%s", "apple");
	}
	f();
}

void test2(){
	int f(void (*p)(char* words)){
		p("banana");
	}
	void f2(char* words){
		printf("%s", words);
	}
	f(f2);
}

void main(){
	test2();
}