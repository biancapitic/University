#include "RecordingTableModel.h"

RecordingTableModel::RecordingTableModel(shared_ptr<Service> service, QObject* parent)
:QAbstractTableModel {parent}
{
	this->service = service;
}

int RecordingTableModel::rowCount(const QModelIndex& parent) const
{
	int recordings_number = this->service->get_watch_list_length();

	return recordings_number;
}

int RecordingTableModel::columnCount(const QModelIndex& parent) const
{
	// Number of attributes of a recording
	return 5;
}

QVariant RecordingTableModel::data(const QModelIndex& index, int role) const
{
	vector<Recording*> recordings;
	Recording recording;
	int row = index.row();
	int column = index.column();

	recordings = this->service->get_watch_list();
	if (row < recordings.size())
	{
		recording = *recordings[row];

		string timeOfCreationString = std::to_string(recording.get_time_of_creation().tm_mon) +
			"-" + std::to_string(recording.get_time_of_creation().tm_mday) + "-" +
			std::to_string(recording.get_time_of_creation().tm_year);

		if (role == Qt::DisplayRole || role == Qt::EditRole)
		{
			switch (column)
			{
			case 0:
				return QString::fromStdString(recording.get_title());
			case 1:
				return QString::fromStdString(recording.get_location());
			case 2:
				return QString::fromStdString(timeOfCreationString);
			case 3:
				return QString::fromStdString(std::to_string(recording.get_times_accessed()));
			case 4:
				return QString::fromStdString(recording.get_footage_preview());
			default:
				break;
			}
		}
	}
	
	if (role == Qt::BackgroundRole)
	{
		return QBrush{ QColor{103, 203, 133} };
	}
	return QVariant{};
}

QVariant RecordingTableModel::headerData(int section, Qt::Orientation orientation, int role) const
{
	if (role == Qt::DisplayRole)
	{
		if (orientation == Qt::Horizontal)
		{
			switch (section)
			{
			case 0:
				return QString{ "Title" };
			case 1:
				return QString{ "Location" };
			case 2:
				return QString{ "Time of Creation" };
			case 3:
				return QString{ "Times Accessed" };
			case 4:
				return QString{ "Footage preview" };
			default:
				break;
			}
		}
	}
	return QVariant{};
}

void RecordingTableModel::updateTable()
{
	QModelIndex topLeft = this->index(1, 1);
	QModelIndex bottomRight = createIndex(this->rowCount(), this->columnCount());
	emit layoutChanged();
	emit dataChanged(topLeft, bottomRight);
}

RecordingTableModel::~RecordingTableModel()
{

}