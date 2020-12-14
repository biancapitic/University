#include "Bag.h"
#include "BagIterator.h"
#include <exception>
#include <iostream>
using namespace std;

//Complexity: BC = WC = AC = Theta(1)
int Bag::hash_prime_function(TElem elem) const
{
	return elem % this->m;
}

//Complexity: BC = WC = AC = Theta(1)
int Bag::hash_second_function(TElem elem) const
{
	if (elem % 2 == 1)
	{
		return 1 + (elem + 1) % this->m;
	}
	return 1 + elem % this->m;
}

//Complexity: BC = WC = AC = Theta(1)
int Bag::hash_function(TElem elem, int i) const
{
	if (elem < 0)
	{
		elem = abs(elem);
	}
	return (this->hash_prime_function(elem) + i * this->hash_second_function(elem)) % this->m;
}

///Complexity: BC = Theta(m), WC = Theta(m*old_capacity), AC = O(m * old_capacity), m = new_capacity
void Bag::resize()
{
	int old_capacity = this->m;
	this->m = this->m * 2;
	
	TElem *new_hash_table = new TElem[this->m];
	int j, position;
	TElem nullElem = NULL_TELEM;
	TElem deletedTElem = DeletedTElem;

	for (int i = 0; i < this->m; i++)
		new_hash_table[i] = nullElem;
	this->length = 0;
	for (int i = 0; i < old_capacity; i++)
	{
		if (this->hashTable[i] != nullElem && this->hashTable[i] != deletedTElem)
		{
			j = 0;
			position = this->hash_function(this->hashTable[i], j);
			while (j < this->m && new_hash_table[position] != nullElem)
			{
				j++;
				position = this->hash_function(this->hashTable[i], j);
				}
			new_hash_table[position] = this->hashTable[i];
			this->length += 1;
		}
	}
	delete []this->hashTable;
	this->hashTable = new_hash_table;
}

//Complexity: BC = WC = AC = Theta(m), m = capacity
Bag::Bag() {
	this->m = 8;
	this->length = 0;
	this->hashTable = new TElem[this->m];
	for (int i = 0; i < this->m; i++)
		this->hashTable[i] = NULL_TELEM;
}

///Complexity: BC = Theta(m), WC = Theta(m^2), AC = O(m^2), m = capacity
void Bag::add(TElem elem) {
	int i, position;
	TElem nullElem = NULL_TELEM;
	TElem deletedTElem = DeletedTElem;
	i = 0;
	position = this->hash_function(elem, i);
	while (i < this->m && this->hashTable[position] != nullElem && this->hashTable[position] != deletedTElem)
	{
		i++;
		position = this->hash_function(elem, i);
	}
	if (i == this->m)
	{
		this->resize();
		this->add(elem);
	}
	else
	{
		this->hashTable[position] = elem;
		this->length += 1;
	}
}

///Complexity: BC = Theta(1), WC = Theta(m), AC = O(m), m = capacity
bool Bag::remove(TElem elem) {
	int position, i;
	TElem nullElem = NULL_TELEM;
	TElem deletedTElem = DeletedTElem;

	if (this->length == 0)
		return false;
	i = 0;
	position = this->hash_function(elem, i);
	while (i < this->m && this->hashTable[position] != nullElem && this->hashTable[position] != elem)
	{
		i++;
		position = this->hash_function(elem, i);
	}
	if (this->hashTable[position] == elem)
	{
		this->hashTable[position] = deletedTElem;
		this->length--;
		return true;
	}
	return false; 
}

///Complexity: BC = Theta(1), WC = Theta(m), AC = O(m), m = capacity
bool Bag::search(TElem elem) const {
	int position, i;
	TElem nullElem = NULL_TELEM;
	TElem deletedTElem = DeletedTElem;

	if (this->length == 0)
		return false;
	i = 0;
	position = this->hash_function(elem, i);
	while (i < this->m && this->hashTable[position] != nullElem && this->hashTable[position] != elem)
	{
		i++;
		position = this->hash_function(elem, i);
	}
	if (i < this->m && this->hashTable[position] == elem)
		return true;
	return false;
}

///Complexity: BC = Theta(1), WC = Theta(m), AC = O(m), m = capacity
int Bag::nrOccurrences(TElem elem) const {
	int position, i, count;
	TElem nullElem = NULL_TELEM;
	TElem deletedTElem = DeletedTElem;

	if (this->length == 0)
		return false;

	count = 0;
	i = 0;
	position = this->hash_function(elem, i);
	while (i < this->m && this->hashTable[position] != nullElem )
	{
		if (this->hashTable[position] == elem)
			count++;
		i++;
		position = this->hash_function(elem, i);
	}
	return count;
}

//Complexity: BC = WC = AC = Theta(1)
int Bag::size() const {
	return this->length;
}

//Complexity: BC = WC = AC = Theta(1)
bool Bag::isEmpty() const {
	if (this->length == 0)
		return true;
	return false;
}

///Complexity: BC = Theta(1), WC = Theta(m), AC = O(m), m = capacity
BagIterator Bag::iterator() const {
	return BagIterator(*this);
}

//Complexity: BC = WC = AC = Theta(1)
Bag::~Bag() {
	delete []this->hashTable;
}

///Complexity: BC = Theta(1), WC = Theta((m^2) * n), AC = O(m*n), n = capacity of Bag b
void Bag::addAll(const Bag& b)
{
	TElem nullElem = NULL_TELEM;
	TElem deletedTElem = DeletedTElem;
	int index;

	if (b.length != 0)
	{
		for (index = 0; index < b.m; index++)
		{
			if (b.hashTable[index] != nullElem && b.hashTable[index] != deletedTElem)
				this->add(b.hashTable[index]);
		}
	}
}