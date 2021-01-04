#include <iostream>
#include <csignal>
#include <unistd.h>

using namespace std;

void signalHandler(int sigNum){
	cout << "received signal number: " << signal << endl;
	exit(sigNum);
}

void test(){
	signal(SIGINT, signalHandler);
	while(true){
		sleep(1);
	}
}

void test2(){
	signal(SIGINT, signalHandler);
	for (int i = 0; i < 100; ++i)
	{
		if (i == 20){
			raise(SIGINT);
		}
		sleep(1);
	}
}

int main(){
	test2();
	return 0;
}