
#include <iostream>
#include "Matrix.h"
#include "ExtendedTest.h"
#include "ShortTest.h"
#include "NumberOfNonZeroElements.h"

using namespace std;


int main() {


	testAll();
	testAllExtended();
	testNumberOfNonZeroElements();
	cout << "Test End" << endl;
	system("pause");
}