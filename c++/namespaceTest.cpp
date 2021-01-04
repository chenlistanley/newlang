#include <iostream>

using namespace std;

namespace n1{
	int add(int a, int b){
		return a+b;
	}
}

namespace n2{
	int add(int a, int b){
		return 100 + a + b;
	}
}

void test(){
	using namespace n1;
	int c = add(10, 20);
	cout << c;
}

void test1(){
	int c = n1::add(10, 20);
	cout << c;
}

void test2(){
	using namespace n2;
	int c = add(10, 20);
	cout << c;
}

void test3(){
	int c = n2::add(10, 20);
	cout << c;
}

int main(){
	test3();
	return 0;
}