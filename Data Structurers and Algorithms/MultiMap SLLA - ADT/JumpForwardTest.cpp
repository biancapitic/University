#include "JumpForwardTest.h"
#include "MultiMap.h"
#include "MultiMapIterator.h"
#include <assert.h>
#include <iostream>
using namespace std;

void testJumpForward()
{
	cout << "Test Jump Forward" << endl;

	MultiMap m;

	m.add(1, 100);
	m.add(2, 200);
	m.add(3, 300);
	m.add(1, 500);
	m.add(2, 600);
	m.add(4, 800);
	m.add(4, 900);
	m.add(4, 700);

	MultiMapIterator it = m.iterator();

	it.jumpForward(3);
	assert(it.getCurrent().first == 2 && it.getCurrent().second == 600);
	it.jumpForward(4);
	assert(it.getCurrent().first == 4 && it.getCurrent().second == 700);

	it.jumpForward(3);
	assert(it.valid() == false);
	try {
		it.first();
		it.jumpForward(-3);
		assert(it.valid() == false);
	}
	catch (exception&) {
	}
	it.first();
	it.jumpForward(5);
	assert(it.getCurrent().first == 4 && it.getCurrent().second == 800);

	it.jumpForward(10);
	try {
		it.getCurrent();
	}
	catch (exception&) {
	}
}
