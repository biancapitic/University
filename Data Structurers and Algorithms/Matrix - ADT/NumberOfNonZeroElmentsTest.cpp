#include <assert.h>
#include "Matrix.h"
#include <iostream>
#include "NumberOfNonZeroElements.h"

using namespace std;

void testNumberOfNonZeroElements()
{
	cout << "Test Number Of Non Zero Elements\n";
	Matrix m(9, 9);
	for (int j = 0; j < m.nrColumns() - 1; j++)
		m.modify(j, j+1, 3);
	assert(m.numberOfNonZeroElems() == m.nrColumns() - 1);
}