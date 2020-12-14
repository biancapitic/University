#pragma once

#define NULL_TELEM -111111;
typedef int TElem;
class BagIterator; 
class Bag {

private:
	#define DeletedTElem -111112;
	TElem* hashTable;
	int m; // capacity
	int length;
	int get_next_prime(int);
	bool isPrime(int);
	void resize();
	int hash_function(TElem, int) const;
	int hash_prime_function(TElem) const;
	int hash_second_function(TElem) const;

	friend class BagIterator;
public:
	
	//constructor
	Bag();

	//adds an element to the bag
	void add(TElem e);

	//removes one occurence of an element from a bag
	//returns true if an element was removed, false otherwise (if e was not part of the bag)
	bool remove(TElem e);

	//checks if an element appearch is the bag
	bool search(TElem e) const;

	//returns the number of occurrences for an element in the bag
	int nrOccurrences(TElem e) const;

	//returns the number of elements from the bag
	int size() const;

	//returns an iterator for this bag
	BagIterator iterator() const;

	//checks if the bag is empty
	bool isEmpty() const;

	//adds all elements of b in the bag
	void addAll(const Bag& b);

	//destructor
	~Bag();
};