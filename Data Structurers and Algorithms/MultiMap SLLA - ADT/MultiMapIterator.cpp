#include "MultiMapIterator.h"
#include "MultiMap.h"
#include <iostream>

//Complexity: BC = WC = AC = Theta(1)
MultiMapIterator::MultiMapIterator(const MultiMap& c): col(c) {
	this->currentKey = this->col.head;
	this->currentElement = -1;
	if (this->currentKey != -1)
		this->currentElement = this->col.map[this->currentKey].head;
}

//Complexity: BC = WC = AC = Theta(1)
TElem MultiMapIterator::getCurrent() const{

	if (this->currentKey == this->col.firstEmpty || this->currentKey == -1)
		throw exception("Element doesn't exist.\n");
	
	TElem element;
	element.first = this->col.map[this->currentKey].key;
	element.second = this->col.map[this->currentKey].infoSLLA[this->currentElement];

	return element;
}

//Complexity: BC = WC = AC = Theta(1)
bool MultiMapIterator::valid() const {
	if (this->currentKey != this->col.firstEmpty && this->currentKey != -1)
		return true;

	return false;
}

//Complexity: BC = WC = AC = Theta(1)
void MultiMapIterator::next() {
	if (this->currentKey == this->col.firstEmpty || this->currentKey == -1)
		throw exception("Exception\n");

	if (this->col.map[this->currentKey].next[this->currentElement] != this->col.map[this->currentKey].firstEmpty)
		this->currentElement = this->col.map[this->currentKey].next[this->currentElement];
	else
	{
		this->currentKey = this->col.next[this->currentKey];
		if (this->currentKey != this->col.firstEmpty)
		{
			this->currentElement = this->col.map[this->currentKey].head;
		}
		else
			this->currentElement = -1;
	}
}

//Complexity: BC = WC = AC = Theta(1)
void MultiMapIterator::first() {
	this->currentKey = this->col.head;
	this->currentElement = -1;
	if (this->currentKey != -1)
		this->currentElement = this->col.map[this->currentKey].head;
}

//Complexity: BC = Theta(1), WC = Theta(n), AC = O(n), n=number of elements
void MultiMapIterator::jumpForward(int k)
{
	if (this->currentKey == this->col.firstEmpty || this->currentKey == -1 || k <= 0)
		throw exception("Exception\n");

	int count = 0;
	while (count < k)
	{
		if (this->currentKey == this->col.firstEmpty || this->currentKey == -1)
			break;
		if (this->col.map[this->currentKey].next[this->currentElement] != this->col.map[this->currentKey].firstEmpty)
			this->currentElement = this->col.map[this->currentKey].next[this->currentElement];
		else
		{
			this->currentKey = this->col.next[this->currentKey];
			if (this->currentKey != this->col.firstEmpty)
			{
				this->currentElement = this->col.map[this->currentKey].head;
			}
			else
				this->currentElement = -1;
		}
		count++;
	}
}

