#pragma once

#include <QtWidgets/QMainWindow>
#include "ui_Lab14.h"
#include "Service.h"
#include <vector>
#include <string>
#include <qmessagebox.h>
#include <exception>
#include <qshortcut.h>
#include "WatchList.h"
#include <ui_Lab14.h>

using std::exception;

class Lab14 : public QMainWindow
{
	Q_OBJECT
		friend class modeB;
public:
    Lab14(Service& service, QWidget* parent = Q_NULLPTR);

private:
    Ui::Lab14Class ui;
	shared_ptr<WatchList> watchListWidget;
	Service& service;
	QShortcut* shortcutUndo;
	QShortcut* shortcutRedo;

	void connectSignalsAndSlots();

	// mode A
	void populateRecordingsList();
	void addRecording();
	void updateRecording();
	void deleteRecording();
	void showRecordingDetails();
	int getSelectedIndex() const;
	void changeToModeB();
	void undo();
	void redo();
	void modeA();
	void setUpButtons();
	void openMylistTableView();
	void initShortcuts();

	//mode B
	void addToWatchList();
	void populateWatchList(vector<Recording*>);
	void nextRecording();
	void filterWatchList();
	void removeFilter();
	void lookAtWatchList();
};
