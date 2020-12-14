#include "SortedBag.h"
#include "SortedBagIterator.h"
#include <iostream>
#include "ShortTest.h"
#include "ExtendedTest.h"
#include "ElementsWithMaximumFrequencyTest.h"

using namespace std;

int main() {
	testElementsWithMaximumFrequency();
	testAll();
	testAllExtended();
	
	cout << "Test over" << endl;
	system("pause");
}
