#pragma once

#include <algorithm>
#include "RecordingValidator.h"
#include "FileRepository.h"
#include "UndoRedo.h"

class Service
{
private:
	InMemoryRepository* repository;
	UndoRedo *undoRedoObject;
public:
	Service();
	Service(InMemoryRepository*);
	Service(const Service&);

	int	add_recording(std::string, std::string, std::string, int, std::string);
	int update_recording(std::string, std::string, std::string, int, std::string);
	int delete_recording(std::string);
	int get_recording_list_length();
	int	check_if_valid_date(std::string);
	vector<Recording*> get_all_recordings();
	Recording* get_next_recording_from_repository(int&);
	int save_to_watch_list(std::string);
	vector<Recording*> get_watch_list();
	vector<Recording*> get_certain_location_recordings_list(std::string location, int);
	int	get_watch_list_length();
	void	change_file_path(string);
	string	get_file_path();
	void	change_watch_list_file_path(string);
	string	get_watch_list_file_path();
	void	operator=(const Service&);
	void	undoCommand();
	void	redoCommand();

	~Service();
};