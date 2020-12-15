#include "Exception.h"

MyException::MyException(string _message)
{
	this->message = _message;
}

string MyException::get_message() const
{
	return this->message;
}

MyException::~MyException()
{
}