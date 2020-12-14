#include "SortedBagIterator.h"
#include "SortedBag.h"
#include <exception>

using namespace std;

//Complexity: BC = WC = AC = Theta(n), n = number of distinct elements
SortedBagIterator::SortedBagIterator(const SortedBag& b) : bag(b) {
	this->iteratorStack = new int[this->bag.length];
	this->stackLength = 0;
	this->nrOccurences = 0;
	int position = this->bag.root;
	while (position != -1)
	{
		this->stackLength += 1;
		this->iteratorStack[this->stackLength -1] = position;
		position = this->bag.left[position];
	}
	if (this->stackLength != 0)
	{
		this->currentElemet = this->iteratorStack[this->stackLength - 1];
		this->nrOccurences = this->bag.info[this->currentElemet].second;
	}
	else
		this->currentElemet = -1;
}

//Complexity: BC = WC = AC = Theta(1)
TComp SortedBagIterator::getCurrent() {
	if (this->currentElemet == -1)
		throw exception();
	return this->bag.info[this->currentElemet].first;
}

//Complexity: BC = WC = AC = Theta(1)
bool SortedBagIterator::valid() {
	if (this->currentElemet != -1)
		return true;
	return false;
}

//Complexity: BC = WC = AC = Theta(1)
void SortedBagIterator::next() {
	if (this->currentElemet == -1)
		throw exception();
	this->nrOccurences -= 1;
	if (this->nrOccurences <= 0)
	{
		int elementPos = this->iteratorStack[this->stackLength - 1];
		this->stackLength--;
		if (this->bag.right[elementPos] != -1)
		{
			elementPos = this->bag.right[elementPos];
			while (elementPos != -1)
			{
				this->iteratorStack[this->stackLength] = elementPos;
				this->stackLength += 1;
				elementPos = this->bag.left[elementPos];
			}
		}
		if (this->stackLength != 0)
		{
			this->currentElemet = this->iteratorStack[this->stackLength - 1];
			this->nrOccurences = this->bag.info[this->currentElemet].second;
		}
		else
			this->currentElemet = -1;
	}
}

//Complexity: BC = WC = AC = Theta(n), n = number of distinct elements
void SortedBagIterator::first() {
	this->iteratorStack = new int[this->bag.length];
	this->stackLength = 0;
	int position = this->bag.root;
	while (position != -1)
	{
		this->stackLength += 1;
		this->iteratorStack[this->stackLength -1] = position;
		position = this->bag.left[position];
	}
	if (this->stackLength != 0)
	{
		this->currentElemet = this->iteratorStack[this->stackLength - 1];
		this->nrOccurences = this->bag.info[this->currentElemet].second;
	}
	else
		this->currentElemet = -1;
}

