#include "ExtendedTest.h"
#include "ShortTest.h"
#include "SortedMap.h"
#include "KeySetTest.h"


#include <iostream>
using namespace std;

#include <crtdbg.h>

int main() {
	testAll();
	testAllExtended();
	testKeySet();

	cout << "That's all!" << endl;
	_CrtDumpMemoryLeaks();
	system("pause");
	return 0;
}


