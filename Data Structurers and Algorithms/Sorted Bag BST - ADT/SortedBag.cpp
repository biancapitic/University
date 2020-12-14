#include "SortedBag.h"
#include "SortedBagIterator.h"
#include <iostream>


//Complexity: BC = WC = AC = Theta(m), m = capacity
SortedBag::SortedBag(Relation r) {
	this->length = 0;
	this->rel = r;
	this->capacity = 4;
	this->root = -1;
	
	this->left = new int[this->capacity];
	this->right = new int[this->capacity];
	this->parent = new int[this->capacity];
	this->info = new pair<TElem, int>[this->capacity];
	this->firstEmpty = new EmptyPosition;

	this->firstEmpty->position = 0;
	this->firstEmpty->next = NULL;
	EmptyPosition* prev_pos = this->firstEmpty;

	for (int i = 0; i < this->capacity; i++)
	{
		this->parent[i] = -1;
		this->left[i] = -1;
		this->right[i] = -1;
		this->info[i].first = -111111;
		this->info[i].second = 0;
		if (i > 0)
		{
			EmptyPosition* new_empty_position = new EmptyPosition;
			new_empty_position->position = i;
			new_empty_position->next = NULL;
			prev_pos->next = new_empty_position;
			prev_pos = new_empty_position;
		}
	}
}

//Complexity: BC = WC = AC = Theta(m), m = 2 * old_capacity
void SortedBag::resize()
{
	int *new_left = new int[this->capacity * 2];
	int *new_right = new int[this->capacity * 2];
	int *new_parent = new int[this->capacity * 2];
	pair<TElem, int> *new_info = new pair<TElem, int>[this->capacity * 2];
	this->firstEmpty = new EmptyPosition;
	for (int i = 0; i < this->capacity; i++)
	{
		new_parent[i] = this->parent[i];
		new_left[i] = this->left[i];
		new_right[i] = this->right[i];
		new_info[i].first = this->info[i].first;
		new_info[i].second = this->info[i].second;
	}
	this->firstEmpty->position = this->capacity;
	this->firstEmpty->next = NULL;
	EmptyPosition* prev_pos = this->firstEmpty;
	for (int i = this->capacity + 1; i < this->capacity * 2; i++)
	{
		EmptyPosition* new_empty_position = new EmptyPosition;
		new_empty_position->position = i;
		new_empty_position->next = NULL;
		prev_pos->next = new_empty_position;
		prev_pos = new_empty_position;
	}
	this->capacity *= 2;
	delete []this->left;
	delete[]this->right;
	delete[]this->parent;
	delete[]this->info;

	this->left = new_left;
	this->right = new_right;
	this->info = new_info;
	this->parent = new_parent;
}

///Complexity: BC = Theta(1), WC = Theta(log(n)), AC = O(log(n)), n = number of distinct elements
void SortedBag::addRec(int position, int prev_position, string direction, TComp e)
{
	if (position == -1)
	{
		if (this->firstEmpty == NULL)
		{
			this->resize();
		}
		this->info[this->firstEmpty->position].first = e;
		this->info[this->firstEmpty->position].second = 1;
		this->parent[this->firstEmpty->position] = prev_position;
		if (direction == "left")
			this->left[prev_position] = this->firstEmpty->position;
		else
			this->right[prev_position] = this->firstEmpty->position;
		this->left[this->firstEmpty->position] = -1;
		this->right[this->firstEmpty->position] = -1;
		
		EmptyPosition* old_firstEmpty = this->firstEmpty;
		this->firstEmpty = this->firstEmpty->next;
		delete old_firstEmpty;
	}
	else {
		if (this->rel(e, this->info[position].first))
		{
			if (this->info[position].first == e)
				this->info[position].second += 1;
			else
				this->addRec(this->left[position], position, "left", e);
		}
		else
		{
			this->addRec(this->right[position], position, "right", e);
		}
	}
}

///Complexity: BC = Theta(1), WC = Theta(log(n)), AC = O(log(n)), n = number of distinct elements
void SortedBag::add(TComp e) {
	
	if (this->length == 0)
	{
		this->root = this->firstEmpty->position;
		this->info[this->firstEmpty->position].first = e;
		this->info[this->firstEmpty->position].second = 1;
		this->left[this->firstEmpty->position] = -1;
		this->right[this->firstEmpty->position] = -1;
		EmptyPosition* emptypos = this->firstEmpty;
		this->firstEmpty = this->firstEmpty->next;
		delete emptypos;
	}
	else
	{
		this->addRec(this->root, -1, "none", e);
	}

	this->length++;
}

///Complexity: BC = WC = AC = O(log(n)), n = number of distinct elements
int SortedBag::getMaxElementLeftSubtree(int position)
{
	if (this->right[position] == -1)
		return position;

	return this->getMaxElementLeftSubtree(this->right[position]);
}

///Complexity: BC = Theta(1), WC = Theta(log(n)), AC = O(log(n)), n = number of distinct elements
int SortedBag::deleteElement(int position, int prev_position, string direction, TComp elem)
{
	if (position == -1)
		return -1;

	if (this->rel(elem, this->info[position].first))
	{
		if (this->info[position].first == elem)
		{
			if (this->info[position].second > 1)
			{
				this->info[position].second -= 1;
				return position;
			}
			else
			{
				int new_position;
				if (this->left[position] == -1 && this->right[position] == -1)
				{
					if (prev_position != -1)
					{
						if (direction == "left")
							this->left[prev_position] = -1;
						else
							this->right[prev_position] = -1;
					}
					else
						this->root = -1;
					this->info[position].first = -111111;
					this->info[position].second = 0;
					this->right[position] = -1;
					this->left[position] = -1;
					this->parent[position] = -1;
					EmptyPosition* new_empty_position = new EmptyPosition;
					new_empty_position->position = position;
					new_empty_position->next = this->firstEmpty;
					this->firstEmpty = new_empty_position;
					return -2;
				}
				else if (this->left[position] == -1)
				{
					new_position = this->right[position];
					if (prev_position != -1)
					{
						if (direction == "left")
							this->left[prev_position] = this->right[position];
						else
							this->right[prev_position] = this->right[position];
					}
					else
						this->root = this->right[position];
					this->parent[this->right[position]] = prev_position;

					this->info[position].first = -111111;
					this->info[position].second = 0;
					this->right[position] = -1;
					this->left[position] = -1;
					this->parent[position] = -1;
					EmptyPosition* new_empty_position = new EmptyPosition;
					new_empty_position->position = position;
					new_empty_position->next = this->firstEmpty;
					this->firstEmpty = new_empty_position;
					return -2;
				}
				else if (this->right[position] == -1)
				{
					new_position = this->left[position];
					if (prev_position != -1)
					{
						if (direction == "left")
							this->left[prev_position] = this->left[position];
						else
							this->right[prev_position] = this->left[position];
					}
					else
						this->root = this->left[position];
					this->parent[this->left[position]] = prev_position;

					this->info[position].first = -111111;
					this->info[position].second = 0;
					this->right[position] = -1;
					this->left[position] = -1;
					this->parent[position] = -1;
					EmptyPosition* new_empty_position = new EmptyPosition;
					new_empty_position->position = position;
					new_empty_position->next = this->firstEmpty;
					this->firstEmpty = new_empty_position;
					return -2;
				}

				int maxFromLeftSubtreePos = this->getMaxElementLeftSubtree(this->left[position]);
				this->info[position].first = this->info[maxFromLeftSubtreePos].first;
				this->info[position].second = this->info[maxFromLeftSubtreePos].second;
				this->info[maxFromLeftSubtreePos].second = 1;
				int result = this->deleteElement(this->left[position], position, "left", this->info[position].first);
				if (result != -1)
					return result;
				return position;
			}
		}
		else
			return this->deleteElement(this->left[position],position, "left", elem);
	}
	else
	{
		return this->deleteElement(this->right[position], position, "right", elem);
	}
}

///Complexity: BC = Theta(1), WC = Theta(log(n)), AC = O(log(n)), n = number of distinct elements
bool SortedBag::remove(TComp e) {
	if (this->length == 0)
		return false;

	int new_root = this->deleteElement(this->root, -1, "none", e);

	if (new_root != -1)
	{
		this->length -= 1;
		return true;
	}
	return false;
}

///Complexity: BC = Theta(1), WC = Theta(n), AC = O(log(n)),n = number of distinct elements
int SortedBag::findElement(int position, TComp e) const
{
	if (position == -1)
		return -1;
	if (this->info[position].first == e)
		return position;
	int left_result = this->findElement(this->left[position], e);
	int right_result = this->findElement(this->right[position], e);
	if (left_result != -1)
		return left_result;
	if (right_result != -1)
		return right_result;
	return -1;
}

///Complexity: BC = Theta(1), WC = Theta(n), AC = O(log(n)),n = number of distinct elements
bool SortedBag::search(TComp elem) const {
	int position;
	position = this->findElement(this->root, elem);
	if (position != -1)
		return true;
	return false;
}

///Complexity: BC = Theta(1), WC = Theta(n), AC = O(log(n)), n = number of distinct elements
int SortedBag::nrOccurrences(TComp elem) const {
	int position;

	position = this->findElement(this->root, elem);
	if (position != -1)
		return this->info[position].second;

	return 0;
}

//Complexity: BC = WC = AC = Theta(1)
int SortedBag::size() const {
	return this->length;
}

//Complexity: BC = WC = AC = Theta(1)
bool SortedBag::isEmpty() const {
	if (this->length == 0)
		return true;
	return false;
}

///Complexity: BC = Theta(1), WC = Theta(m), AC = O(m), m = capacity
SortedBagIterator SortedBag::iterator() const {
	return SortedBagIterator(*this);
}

//Complexity: BC = WC = AC = Theta(1)
SortedBag::~SortedBag() {
	delete[]this->left;
	delete[]this->right;
	delete[]this->parent;
}

//Complexity: BC = WC = AC = Theta(n), n = number of distinct elements
void SortedBag::parseBagForElementsWithMaxFrequency(int position, int &maxFrequency, int &numberOfElements) const
{
	if (position != -1)
	{
		if (this->info[position].second > maxFrequency)
		{
			maxFrequency = this->info[position].second;
			numberOfElements = 1;
		}
		else if (this->info[position].second == maxFrequency)
			numberOfElements += 1;
		
		this->parseBagForElementsWithMaxFrequency(this->left[position], maxFrequency, numberOfElements);
		this->parseBagForElementsWithMaxFrequency(this->right[position], maxFrequency, numberOfElements);
	}
}

///Complexity: BC = WC = AC = Theta(n), n = number of distinct elements
int SortedBag::elementsWithMaximumFrequency() const
{
	if (this->length == 0)
		return 0;

	int maxFrequency = 0;
	int numberOfElements = 0;
	this->parseBagForElementsWithMaxFrequency(this->root, maxFrequency, numberOfElements);
	return numberOfElements;
}