#pragma once

#include <QWidget>
#include "ui_WatchList.h"
#include "RecordingTableModel.h"
#include "Service.h"
#include "qdebug.h"

class WatchList : public QWidget
{
	Q_OBJECT

private:
	shared_ptr<Service> service;
	RecordingTableModel* recordingTableModel;
	Ui::WatchList guiTableView;

public:
	WatchList(shared_ptr<Service>,QWidget *parent = Q_NULLPTR);
	~WatchList();
	void setupTableView();
	void updateTableView();
};
