#include "Matrix.h"
#include <exception>
#include <iostream>
using namespace std;


//Complexity: BC = WC = AC = Theta(1)
Matrix::Matrix()
{
	this->linesNumber = 0;
	this->columnsNumber = 0;
	this->linesIndexArray = new DynamicArray;
	this->columnsArray = new DynamicArray;
	this->values = new DynamicArray;

	this->linesIndexArray->capacity = 2;
	this->linesIndexArray->length = 0;
	this->linesIndexArray->elements = new TElem[2];

	this->columnsArray->capacity = 2;
	this->columnsArray->length = 0;
	this->columnsArray->elements = new TElem[2];

	this->values->capacity = 2;
	this->values->length = 0;
	this->values->elements = new TElem[2];
}

//Complexity: BC = WC = AC = Theta(n), n = nrLines
Matrix::Matrix(int nrLines, int nrCols) {

	this->linesNumber = nrLines;
	this->columnsNumber = nrCols;

	this->linesIndexArray = new DynamicArray;
	this->columnsArray = new DynamicArray;
	this->values = new DynamicArray;

	this->linesIndexArray->capacity = nrLines + 2;
	this->linesIndexArray->length = nrLines + 1;
	this->linesIndexArray->elements = new TElem[nrLines + 1];
	for (int i = 0; i <= nrLines; i++)
		this->linesIndexArray->elements[i] =0;

	this->columnsArray->capacity = 2;
	this->columnsArray->length = 0;
	this->columnsArray->elements = new TElem[2];

	this->values->capacity = 2;
	this->values->length = 0;
	this->values->elements = new TElem[2];
}

//Complexity: BC = WC = AC = Theta(n), n = max {nrLines, matrix.values->length}
Matrix::Matrix(const Matrix& matrix)
{
	this->linesNumber = matrix.linesNumber;
	this->columnsNumber = matrix.columnsNumber;

	this->linesIndexArray = new DynamicArray;
	this->columnsArray = new DynamicArray;
	this->values = new DynamicArray;

	this->linesIndexArray->capacity = matrix.linesIndexArray->capacity;
	this->linesIndexArray->length = matrix.linesIndexArray->length;
	this->linesIndexArray->elements = new TElem[this->linesIndexArray->capacity];
	for (int i = 0; i <= matrix.linesIndexArray->length; i++)
		this->linesIndexArray->elements[i] = matrix.linesIndexArray->elements[i];

	this->columnsArray->capacity = matrix.columnsArray->capacity;
	this->columnsArray->length = matrix.columnsArray->length;
	this->columnsArray->elements = new TElem[this->columnsArray->capacity];
	for (int i = 0; i <= matrix.columnsArray->length; i++)
		this->columnsArray->elements[i] = matrix.columnsArray->elements[i];

	this->values->capacity = matrix.values->capacity;
	this->values->length = matrix.values->length;
	this->values->elements = new TElem[this->values->capacity];
	for (int i = 0; i <= matrix.values->length; i++)
		this->values->elements[i] = matrix.values->elements[i];
}

//Complexity: BC = WC = AC = Theta(1)
int Matrix::nrLines() const {

	return this->linesNumber;
}

//Complexity: BC = WC = AC = Theta(1)
int Matrix::nrColumns() const {
	
	return this->columnsNumber;
}

//Complexity: BC = Theta(1), WC = Theta(n), AC = Theta(n), Total = O(n), n = nrColumns
TElem Matrix::element(int i, int j) const {

	int index_in_column_array;

	if (i < 0 || i >= this->linesNumber || j < 0 || j > this->columnsNumber)
		throw exception ("Invalid position");

	index_in_column_array = this->linesIndexArray->elements[i];
	while (index_in_column_array < this->linesIndexArray->elements[i + 1])
	{
		if (this->columnsArray->elements[index_in_column_array] == j)
			return this->values->elements[index_in_column_array];
		index_in_column_array++;
	}
	return NULL_TELEM;
}

//Complexity: BC = WC = AC = Theta(n), n = dynamic_array->length
void Matrix::resize_dynamic_array(Matrix::DynamicArray *dynamic_array)
{
	TElem *new_elements_array = new TElem[dynamic_array->capacity * 2];

	for (int i = 0; i < dynamic_array->length; i++)
		new_elements_array[i] = dynamic_array->elements[i];
	
	delete[] dynamic_array->elements;
	dynamic_array->elements = new_elements_array;
	dynamic_array->capacity *= 2;
}

//Complexity: BC = Theta(1), WC = Theta(n^2), AC = Theta(n^2), Total = O(n^2), n = columnsArray->length
TElem Matrix::modify(int i, int j, TElem e) {
	
	int index, old_value, line;

	if (i < 0 || i >= this->linesNumber || j < 0 || j > this->columnsNumber)
		throw exception ("Invalid position");

	index = this->linesIndexArray->elements[i];
	
	/// if the element of the matrix is not 0
	while (index < this->linesIndexArray->elements[i + 1])
	{
		if (this->columnsArray->elements[index] == j)
		{
			old_value = this->values->elements[index];

			/// if e is not 0 we will simply change the value from values array
			if (e != 0)
			{
				this->values->elements[index] = e;
			}
			else
			{
				///otherwise we will make the element 0, we will remove it from values and columns arrays

				for (int i = index; i < this->columnsArray->length - 1; i++)
				{
					this->columnsArray->elements[i] = this->columnsArray->elements[i + 1];
					this->values->elements[i] = this->values->elements[i + 1];
				}
				this->columnsArray->length -= 1;
				this->values->length -= 1;

				/// we decrease every position index value from the linesIndexArray
				for (line = i+1; line < this->linesIndexArray->length; line++)
					this->linesIndexArray->elements[line] -= 1;
			}
			return old_value;
		}
		index++;
	}
	/// this means that the element of the matrix is 0 so 
	/// we will add it to our values list and to columns and lines lists
	if (e != 0)
	{
		index = this->linesIndexArray->elements[i+1];
		
		/// if the columnsArray and values array are full we will resize them
		if (this->columnsArray->length == this->columnsArray->capacity)
		{
			this->resize_dynamic_array(this->columnsArray);
			this->resize_dynamic_array(this->values);
		}

		/// we make space for the new element in columnsArray and in values
		for (int i = this->columnsArray->length; i > index; i--)
		{
			this->columnsArray->elements[i] = this->columnsArray->elements[i - 1];
			this->values->elements[i] = this->values->elements[i-1];
		}

		/// we add the value and the column
		this->columnsArray->elements[index] = j;
		this->values->elements[index] = e;

		this->columnsArray->length += 1;
		this->values->length += 1;
		
		/// we increase every position index value from the linesIndexArray
		for (line = i + 1; line < this->linesIndexArray->length; line++)
			this->linesIndexArray->elements[line] += 1;
	}

	/// it means that e is 0 so we don't do anything
	return NULL_TELEM;
}

//Complexity: BC = WC = AC = Theta(1)
Matrix::~Matrix()
{
	delete[]this->linesIndexArray->elements;
	delete this->linesIndexArray;
	delete[]this->columnsArray->elements;
	delete this->columnsArray;
	delete[]this->values->elements;
	delete this->values;
}

//Complexity BC = WC = AC = Theta(n), n = max {other_matrix.linesIndexArray, other_matrix.values->length}
void Matrix::operator=(const Matrix& other_matrix)
{
	this->linesNumber = other_matrix.linesNumber;
	this->columnsNumber = other_matrix.columnsNumber;

	this->linesIndexArray = new DynamicArray;
	this->columnsArray = new DynamicArray;
	this->values = new DynamicArray;

	this->linesIndexArray->capacity = other_matrix.linesIndexArray->capacity;
	this->linesIndexArray->length = other_matrix.linesIndexArray->length;
	this->linesIndexArray->elements = new TElem[this->linesIndexArray->capacity];
	for (int i = 0; i <= other_matrix.linesIndexArray->length; i++)
		this->linesIndexArray->elements[i] = other_matrix.linesIndexArray->elements[i];

	this->columnsArray->capacity = other_matrix.columnsArray->capacity;
	this->columnsArray->length = other_matrix.columnsArray->length;
	this->columnsArray->elements = new TElem[this->columnsArray->capacity];
	for (int i = 0; i <= other_matrix.columnsArray->length; i++)
		this->columnsArray->elements[i] = other_matrix.columnsArray->elements[i];

	this->values->capacity = other_matrix.values->capacity;
	this->values->length = other_matrix.values->length;
	this->values->elements = new TElem[this->values->capacity];
	for (int i = 0; i <= other_matrix.values->length; i++)
		this->values->elements[i] = other_matrix.values->elements[i];
}

//Complexity: BC = WC = AC = Theta(1)
int Matrix::numberOfNonZeroElems() const
{
	return this->linesIndexArray->elements[this->linesIndexArray->length - 1];
}
