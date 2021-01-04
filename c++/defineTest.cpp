#include <iostream>
#include <string>

using namespace std;

#define PI 3.1514926
#define add(x, y) (x+y)
#define A(x) #x
#define B(x, y) x ## y

void test(){
	double a = 5 * PI;
	cout << a;
}

void test2(){
	int a=add(1, 3);
	cout << a;
}

void test3(){
	cout << A(Hello C++);
}

void test4(){
	string xy="Hello C++";
	cout << B(x, y);
}

void test5(){
	cout << __DATE__ << endl << __TIME__;
}

int main(){
	test5();
	return 0;
}
