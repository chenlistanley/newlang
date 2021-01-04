#include <iostream>

using namespace std;

#define PREFER_LANGUAGE 10

void test(){
	cout << PREFER_LANGUAGE << endl;
}

void test1(){
	const int a=10;
	const int b=20;
	cout << a << endl << b;
}

int main(){
	test1();
	return 0;
}