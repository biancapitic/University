#pragma once
#include <stdio.h>
#include <iostream>
#include <string>
#include <ctime>
#include <fstream>
#include "Exception.h"

using std::istream;
using std::ostream;
using std::cout;
using std::ifstream;
using std::ofstream;
using std::fstream;
using std::ios;
using std::remove;
using std::string;

class Recording {
private:
	std::string title;
	std::string location;
	tm timeOfCreation;
	int timesAccessed;
	std::string footagePreview;
public:
	Recording();
	Recording(std::string, std::string, tm, int, std::string);
	Recording(const Recording&);

	std::string get_title();
	std::string get_location();
	tm get_time_of_creation();
	int get_times_accessed();
	std::string get_footage_preview();
	void set_title(std::string);
	void set_location(std::string);
	void set_time_of_creation(tm);
	void set_times_accessed(int);
	void set_footage_preview(std::string);
	bool operator ==(const Recording&) const;
	void operator=(const Recording&);
	friend istream& operator>>(istream& buffer, Recording& recording);
	friend ostream& operator<<(ostream& buffer, const Recording& recording);
	string get_html_format();

	~Recording();

};


