#include "Service.h"
#include <ctime>
#include <locale>
#include <iomanip>

Service::Service()
{
	this->repository = nullptr;
	this->undoRedoObject = nullptr;
}
Service::Service(InMemoryRepository* repository)
{
	this->repository = repository;
	this->undoRedoObject = new UndoRedo();
}
Service::Service(const Service& service)
{
	this->repository = service.repository;
}

int	Service::check_if_valid_date(std::string timeOfCreation)
{
	int position, month, day, year;
	int months_array[] = { 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 };

	position = timeOfCreation.find("-");
	if (position == std::string::npos)
		return -1;
	try
	{
		month = std::stoi(timeOfCreation.substr(0, position));
		if (month < 1 || month > 12)
			return -1;
	}
	catch (const std::exception& e)
	{
		return -1;
	}
	timeOfCreation.erase(0, position + 1);

	position = timeOfCreation.find("-");
	if (position == std::string::npos)
		return -1;
	try
	{
		day = std::stoi(timeOfCreation.substr(0, position));
		if ((day < 1 || day > months_array[month - 1]) && (month != 2))
			return -1;
	}
	catch (const std::exception& e)
	{
		return -1;
	}
	timeOfCreation.erase(0, position + 1);

	position = timeOfCreation.find("-");
	if (timeOfCreation.length() < 3)
		return -1;
	try
	{
		year = std::stoi(timeOfCreation.substr(0, position));
	}
	catch (const std::exception& e)
	{
		return -1;
	}
	timeOfCreation.erase(0, position);

	int first_number_to_check_if_is_a_leap_year = 400;
	int second_number_to_check_if_is_a_leap_year = 4;
	int number_that_shows_if_is_a_leap_year = 100;


	/// check if it's a leap year
	if (month == 2)
	{
		if (((year % first_number_to_check_if_is_a_leap_year == 0)
			|| (year % second_number_to_check_if_is_a_leap_year == 0 && year % number_that_shows_if_is_a_leap_year != 0)))
		{
			if (day < 0 || day > 29)
				return -1;
		}
		else
			if (day < 0 || day > 28)
				return -1;
	}

	return 0;
}

int Service::add_recording(std::string _title, std::string _location, std::string _timeOfCreation, int _timesAccessed,
	std::string _footagePreview)
{
	int valid_date;
	tm timeOfCreation_date;
	vector<Recording*> recordings = this->get_all_recordings();
	
	RecordingValidator recording_validator;

	valid_date = check_if_valid_date(_timeOfCreation);
	if (valid_date == -1)
	{
		if (this->repository->get_filepath() != "") {
			for (auto recording_element : recordings)
				delete recording_element;
		}
		throw MyException("Invalid date.\n");
	}

	sscanf(_timeOfCreation.c_str(), "%d-%d-%d", &timeOfCreation_date.tm_mon, &timeOfCreation_date.tm_mday, &timeOfCreation_date.tm_year);
	Recording* recording = new Recording{ _title, _location, timeOfCreation_date, _timesAccessed, _footagePreview };

	try {
		recording_validator.validate(recordings, *recording);
	}
	catch (MyException& exception)
	{
		if (this->repository->get_filepath() != "") {
			for (auto recording_element : recordings)
				delete recording_element;
			delete recording;
		}
		throw exception;
	}
	if (this->repository->get_filepath() != "") {
		for (auto recording_element : recordings)
			delete recording_element;
	}

	shared_ptr<Command> undoCommand = make_shared<UndoAddCommand>(*recording, this->repository->get_repository_length());
	this->undoRedoObject->addUndoCommand(undoCommand);

	this->repository->add_recording(*recording);

	if (this->repository->get_filepath() != "") {
		delete recording;
	}
	return 0;
}

int Service::update_recording(std::string _title, std::string _location, std::string _timeOfCreation, int _timesAccessed,
	std::string _footagePreview)
{
	int valid_date, recording_position;
	tm timeOfCreation_date;
	
	valid_date = check_if_valid_date(_timeOfCreation);
	if (valid_date == -1)
		throw MyException("Invalid date.\n");

	recording_position = this->repository->repository_get_position_of_element(_title);
	if (recording_position == -1)
		throw MyException("There is no recording with that title in the repository.\n");
	
	sscanf(_timeOfCreation.c_str(), "%d-%d-%d", &timeOfCreation_date.tm_mon, &timeOfCreation_date.tm_mday, &timeOfCreation_date.tm_year);

	Recording recording{ _title, _location, timeOfCreation_date, _timesAccessed, _footagePreview };

	Recording *old_recording = this->repository->get_element_from_position(recording_position);
	shared_ptr<Command> undoCommand = make_shared <UndoUpdateCommand>(*old_recording, recording, recording_position);
	this->undoRedoObject->addUndoCommand(undoCommand);

	this->repository->update_recording(recording);

	return 0;
}

int Service::delete_recording(std::string title)
{
	int recording_position;
	recording_position = this->repository->repository_get_position_of_element(title);

	if (recording_position == -1)
		throw MyException("There is no recording with that title in the repository.\n");

	Recording *recording = this->repository->get_element_from_position(recording_position);
	shared_ptr<Command> undoCommand = make_shared <UndoDeleteCommand>(*recording, recording_position);
	this->undoRedoObject->addUndoCommand(undoCommand);

	this->repository->delete_recording(recording_position);
	return 0;
}

vector<Recording*> Service::get_all_recordings()
{
	return this->repository->get_elements_array();
}

int Service::get_recording_list_length()
{
	return this->repository->get_repository_length();
}

Recording* Service::get_next_recording_from_repository(int& position)
{
	position += 1;
	if (position == this->get_recording_list_length())
		position = 0;
	return this->repository->get_element_from_position(position);
}

int Service::save_to_watch_list(std::string title)
{
	int recording_position;
	Recording* recording_copy;
	Recording* recording;

	recording_position = this->repository->repository_get_position_of_element(title);
	if (recording_position == -1)
		throw MyException("There is no recording with that title in the repository.\n");
	
	if (this->repository->check_if_element_in_watch_list(title))
	{
		throw MyException("A recording with this title is already in the watch list.\n");
	}
	recording = this->repository->get_element_from_position(recording_position);

	recording_copy = new Recording{ *recording };
	this->repository->add_recording_to_watch_list(recording_copy);
	delete recording;
	delete recording_copy;
	return 0;
}

vector<Recording*> Service::get_watch_list()
{
	return this->repository->get_watch_list();
}

int		Service::get_watch_list_length()
{
	return this->repository->get_watch_list_length();
}

vector<Recording*> Service::get_certain_location_recordings_list(std::string location, int timesAccessed)
{
	vector<Recording*> recordings_list = this->repository->get_elements_array();
	vector<Recording*> recordings_list_from_location;

	for (auto recording : recordings_list)
		if (recording->get_location() == location && recording->get_times_accessed() < timesAccessed)
		{
			recordings_list_from_location.push_back(new Recording{ *recording });
		}

	if (this->repository->get_filepath() != "") {
		for (auto recording : recordings_list)
			delete recording;
	}
	return recordings_list_from_location;
}

void	Service::change_file_path(string filepath)
{
	this->repository->set_filepath(filepath);
}

string	Service::get_file_path()
{
	return this->repository->get_filepath();
}

void	Service::change_watch_list_file_path(string filepath)
{
	this->repository->set_watch_list_filepath(filepath);
}

string	Service::get_watch_list_file_path()
{
	return this->repository->get_watch_list_filepath();
}

void	Service::operator=(const Service& other_service)
{
	this->repository = other_service.repository;
}

void	Service::undoCommand()
{
	if (this->undoRedoObject->get_undo_list_size() == 0)
		throw MyException("Undo commands list is empty!");
	this->undoRedoObject->undo(this->repository);
}

void	Service::redoCommand()
{
	if (this->undoRedoObject->get_redo_list_size() == 0)
		throw MyException("Redo commands list is empty!");
	this->undoRedoObject->redo(this->repository);
}

Service::~Service()
{
	delete this->undoRedoObject;
}
