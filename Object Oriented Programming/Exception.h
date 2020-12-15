#pragma once
#include <string>
#include <exception>

using std::string;

class MyException {
	private:
		string message;
	public:
		MyException(string);
		string get_message() const;
		~MyException();
};