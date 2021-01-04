#include <iostream>

using namespace std;

int a=10;
int add(int a){
	static int sum = 0;
	sum += a;
	return sum;
}
