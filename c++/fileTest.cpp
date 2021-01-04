#include <iostream>
#include <string>
#include <fstream>

using namespace std;

const string filename="fileData.txt";

void test(){
	ifstream ifs;
	ifs.open(filename, ios::in);
	char data[200];
	ifs >> data;
	cout << data;

	ifs.close();
}

void test2(){
	ofstream ofs;
	ofs.open(filename, ios::out);
	char data[] = "Welcome to C++";
	ofs << data;
	ofs.close();
}

void test3(){
	fstream fs;
	fs.open(filename, ios::in | ios::out);
	char data[100];
	fs >> data;
	cout << data;
	fs << data;

	fs.close();
}

int main(){
	test3();
}