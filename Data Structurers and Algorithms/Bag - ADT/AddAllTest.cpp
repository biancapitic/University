#include "AddAllTest.h"
#include <assert.h>
#include <iostream>

using namespace std;

void testAddAll()
{
	std::cout << "Test Add All" << std::endl;
	Bag b;
	Bag b2;

	b.add(5);
	b.add(1);
	b.add(10);
	b.add(7);
	b.add(1);
	b.add(11);
	b.add(-3);

	b2.add(5);
	b2.add(1);
	b2.add(10);
	b2.add(7);
	b2.add(1);
	b2.add(11);
	b2.add(11);
	b2.add(-3);
	b2.add(-9);
	b2.add(33);
	b2.add(55);

	b.addAll(b2);
	
	assert(b.size() == 18);
	assert(b.nrOccurrences(5) == 2);
	assert(b.nrOccurrences(-3) == 2);
	assert(b.nrOccurrences(11) == 3);
	assert(b.nrOccurrences(55) == 1);
	assert(b.nrOccurrences(33) == 1);
}