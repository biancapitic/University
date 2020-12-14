#include "ElementsWithMaximumFrequencyTest.h"
#include "SortedBag.h"
#include "SortedBagIterator.h"
#include <assert.h>
#include <iostream>

bool relation(TComp e1, TComp e2) {
	return e1 <= e2;
}

void testElementsWithMaximumFrequency()
{
	SortedBag sb(relation);
	std::cout << "Test elements with maximum frequency...\n";
	assert(sb.elementsWithMaximumFrequency() == 0);

	sb.add(5);
	sb.add(6);
	sb.add(0);
	sb.add(6);
	sb.add(10);

	assert(sb.elementsWithMaximumFrequency() == 1);

	sb.add(8);
	sb.add(5);
	sb.add(0);

	assert(sb.elementsWithMaximumFrequency() == 3);
}