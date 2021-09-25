#include <iostream>

using namespace std;

namespace apple{
	void say(){
		cout << "apple";
	}
}

namespace banana{
	void say(){
		cout << "bananan";
	}
}

void test(){
	using namespace banana;
	say();
} 

int main(){
	test();
	return 0;
}
