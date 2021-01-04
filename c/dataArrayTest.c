#include <stdio.h>

void test(){
	int a[] = {10, 20};
	printf("%d %d", a[0], a[1]);
}

void test2(){
	int a[10] = {10, 20, 30};
	for(int i=0; i<10; i++){
		printf("%d\n", a[i]);
	}
}

void main(){
	test();
}