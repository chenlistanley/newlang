#include <iostream>

using namespace std;

void test(){
	char name[100];
	cout << "Name:";
	cin >> name;
	cout << "Welcome " << name;
}

void test2(){
	cerr << "Error testing";
}

void test3(){
	clog << "Error testing 2";
}

int main(){
	test3();
	return 0;
}