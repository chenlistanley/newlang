#include <stdio.h>

void test(){
	int f(){
		static int a=0;
		return a++;
	}
	for(int i=0; i<10; i++){
		printf("%d\n", f());
	}
}

void main(){
	test();
}
