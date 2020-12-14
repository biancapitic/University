#include "KeySetTest.h"
#include <cassert>

bool relation(TKey key1, TKey key2) {
	if (key1 <= key2) {
		return true;
	}
	else {
		return false;
	}
}

void testKeySet()
{
	SortedMap sm(relation);

	vector<TKey> keyset;
	keyset = sm.keySet();
	assert(keyset.size() == 0);

	for (int i = 1; i< 100; i++)
		sm.add(i, i+1);

	keyset = sm.keySet();
	for (int i = 0; i < keyset.size(); i++)
	{
		assert(keyset[i] == i + 1);
	}

	cout << "Test keyset done.\n";
}