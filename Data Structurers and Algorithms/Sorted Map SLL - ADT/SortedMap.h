#pragma once
#include <utility>
#include <vector>

typedef int TKey;
typedef int TValue;
typedef std::pair<TKey, TValue> TElem;
typedef bool(*Relation)(TKey, TKey);

#define NULL_TVALUE -11111
#define NULL_TPAIR pair<TKey, TValue>(-11111, -11111);
class SMIterator;
using std::vector;

class SortedMap {
	friend class SMIterator;
private:
	struct Node {
		TElem info;
		Node *next;
	};

	Node *head;
	Relation relation;
	
public:

	// constructor
	SortedMap(Relation r);

	// adds a pair (key,value) to the map
	//if the key already exists in the map, then the value associated to the key is replaced by the new value and the old value is returned
	//if the key SMes not exist, a new pair is added and the value null is returned
	TValue add(TKey c, TValue v);

	//searches for the key and returns the value associated with the key if the map contains the key or null: NULL_TVALUE otherwise
	TValue search(TKey c) const;


	//removes a key from the map and returns the value associated with the key if the key existed ot null: NULL_TVALUE otherwise
	TValue remove(TKey c);

	//returns the number of pairs (key,value) from the map
	int size() const;

	//checks whether the map is empty or not
	bool isEmpty() const;

	// return the iterator for the map
	// the iterator will return the keys following the order given by the relation
	SMIterator iterator() const;

	//returns a vector with all the keys from the sortedmap
	vector<TKey> keySet() const;

	// destructor
	~SortedMap();
};
