#include <iostream>
#include <pthread.h>

using namespace std;

void* handler(void* args){
	cout << "threading";
	pthread_exit(NULL);
}

void test(){
	pthread_t t[5];
	for (int i = 0; i < 5; ++i)
	{
		int ret = pthread_create(&t[i], NULL, handler, NULL);
		if (ret != 0){
			cout << "error code: " << ret << endl; 
		}
	}
	pthread_exit(NULL);
}

int main(){
	test();
	return 0;
}