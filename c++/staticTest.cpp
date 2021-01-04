#include <iostream>

using namespace std;


int add(){
	static int a=0;
	a +=1;
	return a;
}

void test(){
	int a, b;
	a=add();
	b=add();
	cout << a << endl << b;
}

int main(){
	test();
	return 0;
}