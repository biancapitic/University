#include "WatchList.h"

WatchList::WatchList(shared_ptr<Service> service, QWidget *parent)
	: QWidget(parent)
{
	guiTableView.setupUi(this);
	this->service = service;
	this->recordingTableModel = new RecordingTableModel{ this->service };
	this->setupTableView();
}

WatchList::~WatchList()
{
}

void WatchList::setupTableView()
{
	this->guiTableView.watchListTableView->setModel(this->recordingTableModel);
}

void WatchList::updateTableView()
{
	this->recordingTableModel->updateTable();
}