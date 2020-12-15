#include "Domain.h"

Recording::Recording()
{
	tm timeOfCreation;
	timeOfCreation.tm_year = 0;
	timeOfCreation.tm_mday = 0;
	timeOfCreation.tm_mon = 0;

	this->title = "";
	this->footagePreview = "";
	this->location = "";
	this->timeOfCreation = timeOfCreation;
	this->timesAccessed = -1;
}

Recording::Recording(std::string _title, std::string _location, tm _timeOfCreation, int _timesAccessed,
	std::string _footagePreview)
{
	this->title = _title;
	this->location = _location;
	this->timeOfCreation = _timeOfCreation;
	this->timesAccessed = _timesAccessed;
	this->footagePreview = _footagePreview;
}

Recording::Recording(const Recording& other_recording)
{
	this->title = other_recording.title;
	this->location = other_recording.location;
	this->timeOfCreation = other_recording.timeOfCreation;
	this->timesAccessed = other_recording.timesAccessed;
	this->footagePreview = other_recording.footagePreview;
}

Recording::~Recording()
{
}

std::string Recording::get_title()
{
	return this->title;
}
std::string Recording::get_location()
{
	return this->location;
}

tm Recording::get_time_of_creation()
{
	return this->timeOfCreation;
}

int Recording::get_times_accessed()
{
	return this->timesAccessed;
}

std::string Recording::get_footage_preview()
{
	return this->footagePreview;
}

void Recording::set_title(std::string new_title)
{
	this->title = new_title;
}

void Recording::set_location(std::string new_location)
{
	this->location = new_location;
}

void Recording::set_time_of_creation(tm new_time_of_creation)
{
	this->timeOfCreation = new_time_of_creation;
}

void Recording::set_times_accessed(int new_times_accessed)
{
	this->timesAccessed = new_times_accessed;
}

void Recording::set_footage_preview(std::string new_footage_preview)
{
	this->footagePreview = new_footage_preview;
}

bool Recording::operator==(const Recording& other_recording) const
{
	return this->title == other_recording.title;
}

void Recording::operator=(const Recording& recording)
{
	this->title = recording.title;
	this->location = recording.location;
	this->timeOfCreation = recording.timeOfCreation;
	this->timesAccessed = recording.timesAccessed;
	this->footagePreview = recording.footagePreview;
}

istream& operator>>(istream& buffer, Recording& recording)
{
	std::string _timeOfCreation;
	std::string parameter_type;
	tm timeOfCreation_date;

	buffer >> parameter_type;
	buffer >> recording.title;
	recording.set_title(recording.title.substr(0, recording.title.length() - 1));

	buffer >> parameter_type;
	buffer >> recording.location;
	recording.set_location(recording.location.substr(0, recording.location.length() - 1));

	buffer >> parameter_type;
	buffer >> _timeOfCreation;
	sscanf(_timeOfCreation.c_str(), "%d-%d-%d", &recording.timeOfCreation.tm_mon, &recording.timeOfCreation.tm_mday,
		&recording.timeOfCreation.tm_year);

	buffer >> parameter_type;
	buffer >> recording.timesAccessed;

	buffer >> parameter_type;
	buffer >> parameter_type;
	buffer >> recording.footagePreview;

	return buffer;
}

ostream& operator<<(ostream& buffer, const Recording& recording)
{
	buffer << "TITLE: " << recording.title << ", LOCATION: " << recording.location
		<< ", TIME_OF_CREATION: " << recording.timeOfCreation.tm_mon << "-" << recording.timeOfCreation.tm_mday << "-"
		<< recording.timeOfCreation.tm_year << ", TIMES_ACCESSED: " << recording.timesAccessed
		<< ", FOOTAGE_PREVIEW: " << recording.footagePreview << "\n";
	return buffer;
}

string Recording::get_html_format()
{
	string html_recording_format = "";

	html_recording_format += "<tr>\n";
	html_recording_format += "<td>" + this->get_title() + "</td>\n";
	html_recording_format += "<td>" + this->get_location() + "</td>\n";
	html_recording_format += "<td>" + std::to_string(this->get_time_of_creation().tm_mon) +
		"-" + std::to_string(this->get_time_of_creation().tm_mday) + "-" + 
		std::to_string(this->get_time_of_creation().tm_year) + "</td>\n";
	html_recording_format += "<td>" + std::to_string(this->get_times_accessed()) + "</td>\n";
	html_recording_format += "<td>" + this->get_footage_preview() + "</td>";
	html_recording_format += "</tr>\n";

	return html_recording_format;
}