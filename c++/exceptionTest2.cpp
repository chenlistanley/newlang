#include <iostream>
#include <exception>

using namespace std;

struct myException :public exception
{
	const char* what() const throw(){
		return "my exception testing";
	} 
};

void test(){
	try{
		throw myException();
	}catch(myException e){
		clog << e.what();
	}
}

int main(){
	test();
	return 0;
}