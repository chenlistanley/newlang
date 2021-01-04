#include <iostream>

using namespace std;

void test(){
	double* a;
	a = new double;
	*a = 10.9999;
	cout << *a;
	delete a;
}

void test2(){
	double* a;
	a = new double[2];
	a[0] = 10.9999;
	a[1] = 1.9999;
	cout << a[0] << endl << a[1];
	delete []a;
}

int main(){
	test2();
	return 0;
}