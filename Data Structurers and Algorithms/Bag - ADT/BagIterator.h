#include "Bag.h"

class BagIterator
{
	friend class Bag;
	
private:
	const Bag& bag;
	int currentElement;

	BagIterator(const Bag& c);
public:
	void first();
	void next();
	TElem getCurrent() const;
	bool valid() const;
};
