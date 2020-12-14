#include "SMIterator.h"
#include "SortedMap.h"
#include <exception>

using namespace std;


///Complexity: BC = WC = AC = Theta(1)
SMIterator::SMIterator(const SortedMap& m) : map(m) {
	this->current_element = map.head;
}

///Complexity: BC = WC = AC = Theta(1)
void SMIterator::first() {
	this->current_element = map.head;
}

///Complexity: BC = WC = AC = Theta(1)
void SMIterator::next() {
	if (this->current_element == NULL)
		throw exception("There is no next element!");

	this->current_element = this->current_element->next;
}

///Complexity: BC = WC = AC = Theta(1)
bool SMIterator::valid() const {
	if (this->current_element != NULL)
		return true;
	return false;
}

///Complexity: BC = WC = AC = Theta(1)
TElem SMIterator::getCurrent() const {
	if (this->current_element == NULL)
	{
		throw exception ("There is no element.");
	}
	return this->current_element->info;
}


