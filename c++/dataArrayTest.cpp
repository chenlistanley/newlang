#include <iostream>

using namespace std;

void test(){
	int a[10];
	a[0]=1;
	a[1]=3;
	a[2]=5;
	for(int i=0; i<10; i++){
		cout << a[i] << endl;
	}
}

void test2(){
	int a[10]={1, 3, 5};
	for(int i=0; i<10; i++){
		cout << a[i] << endl;
	}
}

void test3(){
	int a[]={1, 3, 5};
	for(int i=0; i<3; i++){
		cout << a[i] << endl;
	}
}

int main(){
	test3();
	return 0;
}