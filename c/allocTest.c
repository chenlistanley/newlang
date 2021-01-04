#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void test(){
	char* a = (char*)calloc(10, sizeof(char));
	strcpy(a , "apple");
	printf("%s", a);
	free(a);
}

void test2(){
	char* a = (char*)malloc(10 * sizeof(char));
	strcpy(a , "apple");
	printf("%s", a);
	free(a);
}

void test3(){
	char* a = (char*)malloc(10 * sizeof(char));
	a=(char*)realloc(a, 100 * sizeof(char));
	strcpy(a , "apple banana orange pear");
	printf("%s", a);
	free(a);
}

void main(){
	test3();
}