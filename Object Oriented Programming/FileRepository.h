#pragma once
#include "InMemoryRepository.h"

class FilesRepository : public InMemoryRepository 
{
protected:
	string filepath;
	std::vector<Recording*> watch_list;
public:
	FilesRepository();
	FilesRepository(string filepath);
	FilesRepository(const FilesRepository&);
	virtual string					get_filepath() override;
	virtual void					add_recording(Recording&) override;
	virtual void					update_recording(Recording&) override;
	virtual void					delete_recording(int) override;
	virtual vector<Recording*>		get_elements_array()const override;
	virtual Recording* get_element_from_position(int) override;
	virtual int						repository_get_position_of_element(string) override;
	virtual void					write_elements_to_file(vector<Recording*>);
	virtual void					set_filepath(string)override;
	virtual int						get_repository_length() override;
	virtual bool					check_if_element_in_watch_list(string title);
	~FilesRepository();
};

class RepositoryWithCSV : public FilesRepository {
private:
	string watch_list_filepath;
public:
	RepositoryWithCSV();
	RepositoryWithCSV(string, string);
	RepositoryWithCSV(const RepositoryWithCSV&);
	string			get_watch_list_filepath() override;
	void			set_watch_list_filepath(string) override;
	void			add_recording_to_watch_list(Recording*) override;
	vector<Recording*>		get_watch_list()const override;
	int						get_watch_list_length() override;
	bool			check_if_element_in_watch_list(string title) override;

	~RepositoryWithCSV();
};

class HtmlRepository : public FilesRepository {
private:
	string watch_list_filepath;
public:
	HtmlRepository();
	HtmlRepository(string, string);
	HtmlRepository(const HtmlRepository&);

	string					get_watch_list_filepath() override;
	void					set_watch_list_filepath(string) override;
	void					add_recording_to_watch_list(Recording*) override;
	vector<Recording*>		get_watch_list() const override;
	int						get_watch_list_length() override;
	void					write_watch_list_to_html_file(vector<Recording*>&);
	void					get_watch_list_from_html(vector<Recording*>&);
	bool			check_if_element_in_watch_list(string title) override;

	~HtmlRepository();
};