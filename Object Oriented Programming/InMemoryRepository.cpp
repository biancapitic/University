#include "InMemoryRepository.h"

InMemoryRepository::InMemoryRepository()
{
	vector<Recording*> elements;
	this->elements = elements;
}
InMemoryRepository::InMemoryRepository(vector<Recording*> elements)
{
	this->elements = elements;
}
InMemoryRepository::InMemoryRepository(const InMemoryRepository& other_repository)
{
	this->elements = other_repository.elements;
	this->watch_list = other_repository.watch_list;
}

void	InMemoryRepository::add_recording(Recording& recording)
{
	Recording* recording_pointer = &recording;
	this->elements.push_back(recording_pointer);
}

void	InMemoryRepository::update_recording(Recording& recording)
{
	Recording* old_recording;
	int recording_index;

	recording_index = 0;
	while (recording_index < this->elements.size() && this->elements[recording_index]->get_title() != recording.get_title())
	{
		recording_index++;
	}
	old_recording = this->elements[recording_index];
	delete old_recording;
	this->elements[recording_index] = new Recording{ recording };
}
void	InMemoryRepository::delete_recording(int position)
{
	this->elements.erase(this->elements.begin() + position);
}

vector<Recording*> InMemoryRepository::get_elements_array()const
{
	return this->elements;
}

Recording* InMemoryRepository::get_element_from_position(int position)
{
	Recording* copy_recording = new Recording{ *this->elements[position] };
	return copy_recording;
}

int InMemoryRepository::repository_get_position_of_element(string recording_title)
{
	int recording_index;

	recording_index = 0;
	while (recording_index < this->elements.size() && this->elements[recording_index]->get_title() != recording_title)
		recording_index++;
	return recording_index;
}

void InMemoryRepository::add_recording_to_watch_list(Recording* recording)
{
	Recording* copy_recording = new Recording{ *recording };
	this->watch_list.push_back(copy_recording);
}

vector<Recording*> InMemoryRepository::get_watch_list() const
{
	return this->watch_list;
}

InMemoryRepository::~InMemoryRepository()
{
	for (auto recording : this->elements)
		delete recording;
	for (auto recording : this->watch_list)
		delete recording;
}

int InMemoryRepository::get_repository_length()
{
	return this->elements.size();
}

int InMemoryRepository::get_watch_list_length()
{
	return this->watch_list.size();
}

bool InMemoryRepository::check_if_element_in_watch_list(string recording_title)
{
	for (auto recording : this->watch_list)
		if (recording->get_title() == recording_title)
			return true;
	return false;
}