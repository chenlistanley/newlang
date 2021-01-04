#include <iostream>
#include <exception>

using namespace std;

void test(){
	try{
		throw "test exception";
	}catch(const char* e){
		clog << e;
	}
}

void test2(){
	try{
		throw exception();
	}catch(exception e){
		clog << e.what();
	}
}

int main(){
	test2();
	return 0;
}