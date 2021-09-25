#include <stdio.h>
#include <stdlib.h>
#include <string.h>


void test(){
	char* a = malloc(1);
	a = realloc(a, 10);
	strcpy(a, "apple");
	printf("%s ", a);
	free(a);
} 

void main(){
	test();
}