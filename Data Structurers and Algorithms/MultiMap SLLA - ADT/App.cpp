#include <iostream>
#include "MultiMap.h"
#include "ExtendedTest.h"
#include "ShortTest.h"
#include "JumpForwardTest.h"
#include "MultiMapIterator.h"
#include <crtdbg.h>

using namespace std;


int main() {


	testAll();
	testAllExtended();
	testJumpForward();
	cout << "End" << endl;
	system("pause");

}
