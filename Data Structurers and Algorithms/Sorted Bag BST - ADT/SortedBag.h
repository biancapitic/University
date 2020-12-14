#pragma once
typedef int TComp;
typedef TComp TElem;
typedef bool(*Relation)(TComp, TComp);
#define NULL_TCOMP -11111;

class SortedBagIterator;

#include <utility>
#include <string>
using std::pair;
using std::string;

class SortedBag {
	friend class SortedBagIterator;

private:
	pair<TElem, int> *info;
	int length;
	int capacity;
	int* left;
	int* right;
	int* parent;
	int root;
	Relation rel;

	struct EmptyPosition {
		int position;
		EmptyPosition* next;
	};
	EmptyPosition* firstEmpty;

public:
	//constructor
	SortedBag(Relation r);

	void parseBagForElementsWithMaxFrequency(int, int &, int&) const;
	void addRec(int,int, string, TComp);
	void resize();
	int findElement(int, TComp) const;
	int deleteElement(int,int,string, TComp);
	int getMaxElementLeftSubtree(int);

	//adds an element to the sorted bag
	void add(TComp e);

	//removes one occurence of an element from a sorted bag
	//returns true if an eleent was removed, false otherwise (if e was not part of the sorted bag)
	bool remove(TComp e);

	//checks if an element appearch is the sorted bag
	bool search(TComp e) const;

	//returns the number of occurrences for an element in the sorted bag
	int nrOccurrences(TComp e) const;

	//returns the number of elements from the sorted bag
	int size() const;

	//returns an iterator for this sorted bag
	SortedBagIterator iterator() const;

	//checks if the sorted bag is empty
	bool isEmpty() const;

	//returns the number of elements with the maximum frequency
	//if the SortedBag is empty, it returns 0
	int elementsWithMaximumFrequency() const;

	//destructor
	~SortedBag();
};