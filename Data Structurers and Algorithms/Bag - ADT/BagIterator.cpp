#include <exception>
#include "BagIterator.h"
#include "Bag.h"

using namespace std;

///Complexity: BC = Theta(1), WC = Theta(m), AC = O(m), m = capacity
BagIterator::BagIterator(const Bag& c): bag(c)
{
	TElem nullElem = NULL_TELEM;
	TElem deletedTElem = DeletedTElem;

	this->currentElement = 0;
	while (this->currentElement < this->bag.m && (this->bag.hashTable[this->currentElement] == nullElem
		|| this->bag.hashTable[this->currentElement] == deletedTElem))
	{
		this->currentElement++;
	}
}

///Complexity: BC = Theta(1), WC = Theta(m), AC = O(m), m = capacity
void BagIterator::first() {
	TElem nullElem = NULL_TELEM;
	TElem deletedTElem = DeletedTElem;

	this->currentElement = 0;
	while (this->currentElement < this->bag.m && (this->bag.hashTable[this->currentElement] == nullElem
		|| this->bag.hashTable[this->currentElement] == deletedTElem))
	{
		this->currentElement++;
	}
}

///Complexity: BC = Theta(1), WC = Theta(m), AC = O(m), m = capacity
void BagIterator::next() {
	if (this->currentElement == this->bag.m)
		throw exception("Not valid.");

	TElem nullElem = NULL_TELEM;
	TElem deletedTElem = DeletedTElem;

	this->currentElement++;
	while (this->currentElement < this->bag.m && (this->bag.hashTable[this->currentElement] == nullElem
		|| this->bag.hashTable[this->currentElement] == deletedTElem))
	{
		this->currentElement++;
	}
}

//Complexity: BC = WC = AC = Theta(1)
bool BagIterator::valid() const {
	if (this->currentElement == this->bag.m)
		return false;
	return true;
}

//Complexity: BC = WC = AC = Theta(1)
TElem BagIterator::getCurrent() const
{
	if (this->currentElement == this->bag.m)
		throw exception("Not valid.");
	return  this->bag.hashTable[this->currentElement];
}
