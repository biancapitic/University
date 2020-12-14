#include "Bag.h"
#include "ShortTest.h"
#include "ExtendedTest.h"
#include "AddAllTest.h"
#include <iostream>

using namespace std;

int main() {
	testAll();
	cout << "Short tests over" << endl;
	testAllExtended();
	testAddAll();
	cout << "All test over" << endl;
}