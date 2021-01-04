#include <stdio.h>

enum SEX{
	F,
	M
};

void test(){
	enum SEX s = F;
	printf("%d", s);
}

void test2(){
	printf("%d %d", F, M);
}

void test3(){
	for (int s = F; s <= M; ++s)
	{
		printf("%d\n", s);
	}
}

void main(){
	test3();
}
