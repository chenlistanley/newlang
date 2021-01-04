#include <iostream>

using namespace std;

template<typename T>
T add(T a, T b){
	return a + b;
}

void test(){
	cout << add(10, 20) << endl;
	cout << add(10.99, 20.99) << endl;
}

int main(){
	test();
	return 0;
}