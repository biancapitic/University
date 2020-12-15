#pragma once
#include <QAbstractTableModel>
#include "Service.h"
#include <qbrush.h>
#include <qfont.h>

class RecordingTableModel: public QAbstractTableModel
{
	private:
		shared_ptr<Service> service;
	public:
		RecordingTableModel(shared_ptr<Service>, QObject* parent = NULL);
		~RecordingTableModel();

		int rowCount(const QModelIndex& parent = QModelIndex{}) const override;
		int columnCount(const QModelIndex& parent = QModelIndex{}) const override;
		QVariant data(const QModelIndex&, int role = Qt::DisplayRole) const override;
		QVariant headerData(int, Qt::Orientation, int) const override;
		void updateTable();
};

