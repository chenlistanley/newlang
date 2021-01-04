#include <stdio.h>

#define FILE_PATH "data.txt"

void test(){
	FILE* f;
	char str[100];
	f = fopen(FILE_PATH, "r");
	fgets(str, 100, f);
	printf("%s\n", str);
	fclose(f);
}

void test2(){
	FILE* f;
	char str[100];
	f = fopen(FILE_PATH, "r");
	fscanf(f, "%s", str);
	printf("%s\n", str);
	fclose(f);
}

void test3(){
	FILE* f;
	char str[100];
	f = fopen(FILE_PATH, "w");
	// f = fopen(FILE_PATH, "a");
	fprintf(f, "%s\n", "apple banana");
	fprintf(f, "%s\n", "orange pear");
	fclose(f);
}

void test4(){
	FILE* f;
	char str[100];
	f = fopen(FILE_PATH, "w");
	fputs("apple", f);
	fputs(" banana", f);
	fclose(f);
}


void main(){
	test2();
}