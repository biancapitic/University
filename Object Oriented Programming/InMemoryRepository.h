#pragma once
#include "Domain.h"
#include<string>
#include<vector>

using std::string;
using std::vector;
using std::shared_ptr;
using std::make_shared;

class InMemoryRepository
{
private:
	vector<Recording*> elements;
	vector<Recording*> watch_list;
public:
	InMemoryRepository();
	InMemoryRepository(vector<Recording*>);
	InMemoryRepository(const InMemoryRepository&);

	virtual void	add_recording(Recording&);
	virtual void	update_recording(Recording&);
	virtual void	delete_recording(int);
	virtual vector<Recording*> get_elements_array() const;
	virtual Recording* get_element_from_position(int);
	virtual int repository_get_position_of_element(std::string);
	virtual void add_recording_to_watch_list(Recording*);
	virtual vector<Recording*> get_watch_list() const;
	virtual int get_repository_length();
	virtual int get_watch_list_length();
	virtual bool check_if_element_in_watch_list(string);
	virtual string			get_watch_list_filepath() { return ""; };
	virtual void			set_watch_list_filepath(string) {};
	virtual void					set_filepath(string) {};
	virtual string					get_filepath() { return ""; };

	~InMemoryRepository();
};
