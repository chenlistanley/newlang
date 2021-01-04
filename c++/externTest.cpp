#include <iostream>

using namespace std;

extern int a;
extern int add(int a);


int main(){
	int b = add(a);
	cout << b;
	return 0;
}