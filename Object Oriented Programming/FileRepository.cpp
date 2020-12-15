#include "FileRepository.h"

FilesRepository::FilesRepository()
{
	this->filepath = "";
}

FilesRepository::FilesRepository(string filepath)
{
	this->filepath = filepath;
	vector<Recording*> watch_list;
	this->watch_list = watch_list;
}

FilesRepository::FilesRepository(const FilesRepository& other_repository)
{
	this->filepath = other_repository.filepath;
	this->watch_list = other_repository.watch_list;
}

FilesRepository::~FilesRepository()
{
	for (auto recording : this->watch_list)
		delete recording;
}

string	FilesRepository::get_filepath()
{
	return this->filepath;
}

void	FilesRepository::set_filepath(string filepath)
{
	this->filepath = filepath;
}

vector<Recording*> FilesRepository::get_elements_array() const
{
	Recording recording;
	Recording* recording_pointer;
	fstream read_file;
	vector<Recording*> elements{};

	read_file.open(this->filepath, ios::in | ios::out | ios::app);
	if (read_file.is_open())
	{
		while (read_file >> recording)
		{
			recording_pointer = new Recording{ recording };
			elements.push_back(recording_pointer);
		}
		return elements;
	}
	else
		throw MyException("Can't open / create the file\n");
}

void FilesRepository::add_recording(Recording& recording)
{
	ofstream file;
	file.open(this->filepath, ios::out | ios::app);

	if (file.is_open())
	{
		file << recording;
	}
	else
		throw MyException("Can't open / create the file\n");
}

void FilesRepository::write_elements_to_file(vector<Recording*> elements)
{
	ofstream file;
	file.open(this->filepath, ios::out);
	if (file.is_open())
	{
		for (auto recording : elements)
			file << *recording;
	}
	else
		throw MyException("Can't open / create the file\n");
}

void FilesRepository::update_recording(Recording& recording)
{
	vector<Recording*> elements = this->get_elements_array();

	ofstream file;
	file.open(this->filepath, ios::out);
	if (file.is_open())
	{
		for (auto recording_from_list : elements)
		{
			if (recording_from_list->get_title() == recording.get_title())
			{
				file << recording;
			}
			else
				file << *recording_from_list;
		}
		for (auto recording_from_list : elements)
			delete recording_from_list;
	}
	else
		throw MyException("Can't open / create the file\n");
}

void FilesRepository::delete_recording(int position)
{
	vector<Recording*> elements = this->get_elements_array();

	delete elements[position];
	elements.erase(elements.begin() + position);

	this->write_elements_to_file(elements);

	for (auto recording_from_list : elements)
		delete recording_from_list;
}

Recording* FilesRepository::get_element_from_position(int position)
{
	vector <Recording*> elements = this->get_elements_array();
	Recording* recording = new Recording{ *(elements.at(position)) };

	for (auto recording_from_list : elements)
		delete recording_from_list;

	return recording;
}

int FilesRepository::repository_get_position_of_element(std::string recording_title)
{
	vector <Recording*> elements = this->get_elements_array();
	int position = -1;

	if (elements.size() == 0)
		return -1;

	for (auto recording : elements)
	{
		position += 1;
		if (recording->get_title() == recording_title)
		{
			for (auto recording_from_list : elements)
				delete recording_from_list;
			return position;
		}
	}

	for (auto recording_from_list : elements)
		delete recording_from_list;

	return -1;
}

int FilesRepository::get_repository_length()
{
	vector<Recording*> recording_list = this->get_elements_array();
	int length = recording_list.size();

	for (auto recording : recording_list)
		delete recording;

	return length;
}

bool FilesRepository::check_if_element_in_watch_list(string title) {
	for (auto recording : this->watch_list)
		if (recording->get_title() == title)
			return true;
	return false;
}
















RepositoryWithCSV::RepositoryWithCSV()
{
	this->set_filepath("");
	this->watch_list_filepath = "";
}

RepositoryWithCSV::RepositoryWithCSV(string repository_filepath, string watch_list_filepath)
{
	this->set_filepath(repository_filepath);
	this->watch_list_filepath = watch_list_filepath;
}

RepositoryWithCSV::RepositoryWithCSV(const RepositoryWithCSV& other_repository)
{
	this->set_filepath(other_repository.filepath);
	this->set_watch_list_filepath(other_repository.watch_list_filepath);
}

string			RepositoryWithCSV::get_watch_list_filepath()
{
	return this->watch_list_filepath;
}

void			RepositoryWithCSV::set_watch_list_filepath(string filepath)
{
	this->watch_list_filepath = filepath;
}

void			RepositoryWithCSV::add_recording_to_watch_list(Recording* recording)
{
	ofstream file;

	file.open(this->watch_list_filepath, ios::out | ios::app);
	if (file.is_open())
		file << *recording;
	else
		throw MyException("Can't open / create the file\n");
}

vector<Recording*>		RepositoryWithCSV::get_watch_list() const
{
	Recording recording;
	Recording* recording_pointer;
	fstream read_file;
	vector<Recording*> watch_list{};

	read_file.open(this->watch_list_filepath, ios::in | ios::out | ios::app);
	if (read_file.is_open())
	{
		while (read_file >> recording)
		{
			recording_pointer = new Recording{ recording };
			watch_list.push_back(recording_pointer);
		}
		return watch_list;
	}
	else
		throw MyException("Can't open / create the file\n");
}

int		RepositoryWithCSV::get_watch_list_length()
{
	vector<Recording*> recording_list = this->get_watch_list();
	int length = recording_list.size();

	for (auto recording : recording_list)
		delete recording;

	return length;
}

bool RepositoryWithCSV::check_if_element_in_watch_list(string title) {
	vector<Recording*> watch_list= this->get_watch_list();

	for (auto recording : watch_list)
		if (recording->get_title() == title)
		{
			for (auto recording_from_list : watch_list)
				delete recording_from_list;
			return true;
		}

	for (auto recording_from_list : watch_list)
		delete recording_from_list;
	return false;
}

RepositoryWithCSV::~RepositoryWithCSV()
{}

HtmlRepository::HtmlRepository()
{
	this->set_filepath("");
	this->watch_list_filepath = "";
}

HtmlRepository::HtmlRepository(string repository_filepath, string watch_list_filepath)
{
	this->set_filepath(repository_filepath);
	this->watch_list_filepath = watch_list_filepath;
}

HtmlRepository::HtmlRepository(const HtmlRepository& other_repository)
{
	this->set_filepath(other_repository.filepath);
	this->set_watch_list_filepath(other_repository.watch_list_filepath);
}

string	HtmlRepository::get_watch_list_filepath()
{
	return this->watch_list_filepath;
}

void HtmlRepository::set_watch_list_filepath(string)
{
	this->watch_list_filepath = filepath;
}

void HtmlRepository::add_recording_to_watch_list(Recording* recording)
{
	ofstream file;
	vector<Recording*> watch_list = this->get_watch_list();
	watch_list.push_back(recording);
	this->write_watch_list_to_html_file(watch_list);

	auto recording_from_list = watch_list.begin();
	watch_list.pop_back();
	for (auto recording_from_list : watch_list)
		delete recording_from_list;
}
vector<Recording*>		HtmlRepository::get_watch_list() const
{
	vector<Recording*> watch_list{};
	fstream read_file;
	string line;
	Recording* recording_pointer;
	string title;
	string location;
	tm timeOfCreation;
	int timesAccessed;
	string footagePreview;

	timeOfCreation.tm_mon = 1;
	timeOfCreation.tm_mday = 1;
	timeOfCreation.tm_year = 2000;

	read_file.open(this->watch_list_filepath, ios::in | ios::out | ios::app);
	if (read_file.is_open())
	{
		if (getline(read_file, line))
		{
			getline(read_file, line);
			while (line != "</tr>")
			{
				getline(read_file, line);
			}
			getline(read_file, line);
			while (line != "</table>")
			{
				getline(read_file, line); // title
				title = line.substr(strlen("<tr>"), strlen(line.c_str()) - strlen("<tr></tr>"));

				getline(read_file, line); // location
				location = line.substr(strlen("<tr>"), strlen(line.c_str()) - strlen("<tr></tr>"));

				getline(read_file, line); // timeOfcreation
				line = line.substr(strlen("<tr>"), strlen(line.c_str()) - strlen("<tr></tr>"));
				sscanf(line.c_str(), "%d-%d-%d", &timeOfCreation.tm_mon, &timeOfCreation.tm_mday, &timeOfCreation.tm_year);

				getline(read_file, line); // timesAccessed
				timesAccessed = atoi((line.substr(strlen("<tr>"), strlen(line.c_str()) - strlen("<tr></tr>"))).c_str());

				getline(read_file, line); // location
				footagePreview = line.substr(strlen("<tr>"), strlen(line.c_str()) - strlen("<tr></tr></td>"));

				getline(read_file, line);
				recording_pointer = new Recording{ title, location, timeOfCreation, timesAccessed, footagePreview };
				watch_list.push_back(recording_pointer);
			}
		}
		return watch_list;
	}
	else
		throw MyException("Can't open / create the file\n");
}

int	HtmlRepository::get_watch_list_length()
{
	vector<Recording*> recording_list = this->get_watch_list();
	int length = recording_list.size();

	for (auto recording : recording_list)
		delete recording;

	return length;
}

void HtmlRepository::write_watch_list_to_html_file(vector<Recording*>& watch_list)
{
	ofstream file;
	file.open(this->watch_list_filepath, ios::out);
	if (file.is_open())
	{
		file << "<!DOCTYPE html>\n";
		file << "<html>\n";
		file << "<head>\n";
		file << "<title>Recordings</title>\n";
		file << "</head>\n";
		file << "<body>\n";
		file << "<table border=\"1\">\n";
		file << "<tr>";
		file << "<td>TITLE</td>";
		file << "<td>LOCATION</td>";
		file << "<td>TIME_OF_CREATION</td>";
		file << "<td>TIMES_ACCESSED</td>";
		file << "<td>FOOTAGE_PREVIEW</td>\n";
		file << "</tr>\n";
		for (auto recording : watch_list)
			file << recording->get_html_format();
		file << "</table>\n";
		file << "</body>\n";
		file << "</html>\n";
	}
	else
		throw MyException("Can't open / create the file\n");
}

bool HtmlRepository::check_if_element_in_watch_list(string title)
{
	vector<Recording*> watch_list = this->get_watch_list();

	for (auto recording : watch_list)
		if (recording->get_title() == title)
		{
			for (auto recording_from_list : watch_list)
				delete recording_from_list;
			return true;
		}

	for (auto recording_from_list : watch_list)
		delete recording_from_list;
	return false;
}

HtmlRepository::~HtmlRepository()
{
}