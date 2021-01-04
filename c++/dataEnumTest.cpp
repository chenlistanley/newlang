#include <iostream>

using namespace std;


enum Gender {
	M=1,
	F
};

void test(){
	Gender g;
	g=F;
	cout << g;
}

int main(){
	test();
	return 0;
}