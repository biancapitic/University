#pragma once

typedef int TElem;
#define NULL_TELEM 0

class Matrix {

private:
	TElem linesNumber;
	TElem columnsNumber;

	struct DynamicArray {
		TElem capacity;
		TElem length;
		TElem *elements;
	};

	DynamicArray *values;
	DynamicArray *columnsArray;
	DynamicArray *linesIndexArray;

	//function will resize the dynamic array
	void resize_dynamic_array(Matrix::DynamicArray*);

public:
	//constructor
	Matrix();
	Matrix(int nrLines, int nrCols);
	Matrix(const Matrix&);

	//returns the number of lines
	int nrLines() const;

	//returns the number of columns
	int nrColumns() const;

	//returns the element from line i and column j (indexing starts from 0)
	//throws exception if (i,j) is not a valid position in the Matrix
	TElem element(int i, int j) const;

	//modifies the value from line i and column j
	//returns the previous value from the position
	//throws exception if (i,j) is not a valid position in the Matrix
	TElem modify(int i, int j, TElem e);

	//assignment operator
	void operator=(const Matrix&);

	//returns the number of elements from the Matrix which are not NULL_TELEM.
	int numberOfNonZeroElems() const;

	//destructor
	~Matrix();
};