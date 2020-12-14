#include "SMIterator.h"
#include "SortedMap.h"
#include <exception>
using namespace std;

#include <iostream>

//Complexity: BC = WC = AC = Theta(1)
SortedMap::SortedMap(Relation r) {
	this->head = NULL;
	this->relation = r;
}

////Complexity: BC = WC = AC = Theta(1)
TValue SortedMap::add(TKey k, TValue v) {
	Node *current_node = this->head;
	Node *new_node;
	Node *prev_node = NULL;
	TValue old_value;

	if (current_node != NULL)
	{
		while (current_node != NULL && this->relation(current_node->info.first, k))
		{
			if (current_node->info.first == k)
			{
				old_value = current_node->info.second;
				current_node->info.second = v;
				return old_value;
			}
			prev_node = current_node;
			current_node = current_node->next;
		}
	}

	new_node = new Node;
	new_node->info.first = k;
	new_node->info.second = v;
	new_node->next = NULL;

	if (this->head == NULL)
		this->head = new_node;
	else if (prev_node == NULL)
	{
		new_node->next = current_node;
		this->head = new_node;
	}
	else
	{
		if (prev_node->next != NULL)
		{
			new_node->next = prev_node->next;
		}
		prev_node->next = new_node;
	}

	return NULL_TVALUE;
}

///Complexity: BC = Theta(1), WC = Theta(n), AC = O(n), n=number of elements in the map
TValue SortedMap::search(TKey k) const {
	Node *current_node = this->head;

	while (current_node != NULL && this->relation(current_node->info.first, k))
	{
		if (current_node->info.first == k)
			return current_node->info.second;

		current_node = current_node->next;
	}

	return NULL_TVALUE;
}


///Complexity: BC = Theta(1), WC = Theta(n), AC = O(n) , n=number of elements in the map
TValue SortedMap::remove(TKey k) {
	TValue value;
	Node *current_node = this->head;
	Node *prev = NULL;

	while (current_node != NULL && this->relation(current_node->info.first, k))
	{
		if (current_node->info.first == k)
		{
			value =  current_node->info.second;

			if (prev != NULL)
				prev->next = current_node->next;
			else
			{
				this->head = current_node->next;
			}

			delete current_node;

			return value;
		}
		prev = current_node;
		current_node = current_node->next;
	}

	return NULL_TVALUE;
}

///Complexity: BC = WC = AC = Theta(n), n=number of elements in the map
int SortedMap::size() const {
	if (this->head == NULL)
		return 0;

	int size = 0;
	Node *current_node = this->head;
	while (current_node != NULL)
	{
		size++;
		current_node = current_node->next;
	}
	return size;
}

//Complexity: BC = WC = AC = Theta(1)
bool SortedMap::isEmpty() const {
	if (this->head == NULL)
		return true;
	return false;
}

///Complexity: BC = WC = AC = Theta(1)
SMIterator SortedMap::iterator() const {
	return SMIterator(*this);
}


///Complexity: BC = Theta(1), WC = Theta(n), AC = O(n) , n=number of elements in the map
SortedMap::~SortedMap() {
	//TODO - Implementation

	Node *current_node = this->head;
	Node *next_node;

	while (current_node != NULL)
	{
		next_node = current_node->next;
		delete current_node;
		current_node = next_node;
	}
	this->head = NULL;
	this->relation = NULL;
}

///Complexity: BC = WC = AC = Theta(n), n=number of keys in the map
vector<TKey> SortedMap::keySet() const
{
	Node* current_node = this->head;
	vector<TKey> keyset;

	while (current_node != NULL)
	{
		keyset.push_back(current_node->info.first);
		current_node = current_node->next;
	}
	return keyset;
}
