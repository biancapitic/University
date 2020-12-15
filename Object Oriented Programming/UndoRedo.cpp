#include "UndoRedo.h"

Command::Command()
{}

Command::~Command()
{}

UndoAddCommand::UndoAddCommand(const Recording& recording, int element_id)
{
	this->element_id = element_id;
	this->recording = new Recording{ recording };
}

UndoAddCommand::UndoAddCommand(const UndoAddCommand& other_addCommand)
{
	this->element_id = other_addCommand.element_id;
	this->recording = new Recording{ *other_addCommand.recording };
}

void UndoAddCommand::handler(InMemoryRepository* repository)
{
	int position = repository->repository_get_position_of_element(this->recording->get_title());
	repository->delete_recording(position);
}

shared_ptr<Command> UndoAddCommand::getOppositeCommand()
{
	shared_ptr<Command> opposite_command = make_shared<UndoDeleteCommand>(*this->recording, this->element_id);
	return opposite_command;
}

UndoAddCommand::~UndoAddCommand()
{
	delete this->recording;
}


UndoDeleteCommand::UndoDeleteCommand(const Recording& recording, int element_id)
{
	this->element_id = element_id;
	this->recording = new Recording{ recording };
}

UndoDeleteCommand::UndoDeleteCommand(const UndoDeleteCommand& other_delete_command)
{
	this->recording = new Recording{ *other_delete_command.recording };
	this->element_id = other_delete_command.element_id;
}

UndoDeleteCommand::~UndoDeleteCommand()
{
	delete this->recording;
}

void UndoDeleteCommand::handler(InMemoryRepository* repository)
{
	repository->add_recording(*(new Recording{ *this->recording }));
}

shared_ptr<Command> UndoDeleteCommand::getOppositeCommand()
{
	shared_ptr<Command> opposite_command = make_shared<UndoAddCommand>(*this->recording, this->element_id);
	return opposite_command;
}


UndoUpdateCommand::UndoUpdateCommand(const Recording& recording, const Recording& new_recording, int element_id)
{
	this->element_id = element_id;
	this->recording = new Recording{ recording };
	this->new_recording = new Recording{ new_recording };
}

UndoUpdateCommand::UndoUpdateCommand(const UndoUpdateCommand& other_update_command)
{
	this->new_recording = new Recording{ *other_update_command.new_recording };
	this->recording = new Recording{ *other_update_command.recording };
	this->element_id = other_update_command.element_id;
}

UndoUpdateCommand::~UndoUpdateCommand()
{
	delete this->new_recording;
	delete this->recording;
}


void UndoUpdateCommand::handler(InMemoryRepository* repository)
{
	repository->update_recording(*this->recording);
}

shared_ptr<Command> UndoUpdateCommand::getOppositeCommand()
{
	shared_ptr<Command> opposite_command = make_shared<UndoUpdateCommand>(*this->new_recording,*this->recording, this->element_id);
	return opposite_command;
}


UndoRedo::UndoRedo()
{
}

void UndoRedo::addUndoCommand(shared_ptr<Command> command)
{
	undoCommandsList.push_back(command);
}

void UndoRedo::addRedoCommand(shared_ptr<Command> command)
{
	redoCommandsList.push_back(command);
}

int UndoRedo::get_undo_list_size()
{
	return this->undoCommandsList.size();
}

int UndoRedo::get_redo_list_size()
{
	return this->redoCommandsList.size();
}

void UndoRedo::undo(InMemoryRepository* repository)
{
	shared_ptr<Command> oppositeCommand =  this->undoCommandsList[this->undoCommandsList.size() - 1]->getOppositeCommand();
	this->undoCommandsList[this->undoCommandsList.size() - 1]->handler(repository);
	this->addRedoCommand(oppositeCommand);
	this->undoCommandsList.pop_back();
}


void UndoRedo::redo(InMemoryRepository* repository)
{
	shared_ptr<Command> oppositeCommand = this->redoCommandsList[this->redoCommandsList.size() - 1]->getOppositeCommand();
	this->redoCommandsList[this->redoCommandsList.size() - 1]->handler(repository);
	this->addUndoCommand(oppositeCommand);
	this->redoCommandsList.pop_back();
}

UndoRedo::~UndoRedo()
{
}