#pragma once
#include "InMemoryRepository.h"

using std::shared_ptr;

class Command {
protected:
	Recording* recording;
	int element_id;
public:
	virtual void handler(InMemoryRepository*) = 0;
	virtual shared_ptr<Command> getOppositeCommand() = 0;
	Command();
	~Command();
};

class UndoAddCommand : public Command
{
public:
	shared_ptr<Command> getOppositeCommand() override;
	void handler(InMemoryRepository*) override;
	UndoAddCommand(const Recording&, int);
	UndoAddCommand(const UndoAddCommand&);
	~UndoAddCommand();
};

class UndoDeleteCommand :public Command
{
public:
	shared_ptr<Command> getOppositeCommand() override;
	void handler(InMemoryRepository*) override;
	UndoDeleteCommand(const Recording&, int);
	UndoDeleteCommand(const UndoDeleteCommand&);
	~UndoDeleteCommand();
};

class UndoUpdateCommand : public Command
{
private:
	Recording* new_recording;
public:
	shared_ptr<Command> getOppositeCommand() override;
	void handler(InMemoryRepository*) override;
	UndoUpdateCommand(const Recording&, const Recording&, int);
	UndoUpdateCommand(const UndoUpdateCommand&);
	~UndoUpdateCommand();
};

class UndoRedo {
	protected:
		vector<std::shared_ptr<Command>> undoCommandsList;
		vector<std::shared_ptr<Command>> redoCommandsList;
	public:
		UndoRedo();
		int get_undo_list_size();
		int get_redo_list_size();
		void addUndoCommand(shared_ptr<Command>);
		void addRedoCommand(shared_ptr<Command>);
		void undo(InMemoryRepository*);
		void redo(InMemoryRepository*);
		~UndoRedo();
};