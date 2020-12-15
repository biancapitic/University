#include "Lab14.h"
#include <QModelIndexList>

Lab14::Lab14(Service& _service, QWidget* parent)
	: QMainWindow(parent), service{ _service }
{
    ui.setupUi(this);
	this->populateRecordingsList();
	this->populateWatchList(this->service.get_watch_list());
	this->initShortcuts();
	this->connectSignalsAndSlots();
	this->setUpButtons();
	
	this->watchListWidget = make_shared<WatchList>(make_shared<Service>(this->service));
}


void Lab14::setUpButtons()
{
	this->ui.addButton->setEnabled(false);
	this->ui.deleteButton->setEnabled(false);
	this->ui.updateButton->setEnabled(false);
	this->ui.undoButton->setEnabled(false);
	this->ui.redoButton->setEnabled(false);
	this->ui.nextWatchListButton->setEnabled(false);
	this->ui.filterButton->setEnabled(false);
	this->ui.removeFilterButton->setEnabled(false);
	this->ui.lookAtWatchListButton->setEnabled(false);
	this->ui.addToWatchListButton->setEnabled(false);
	this->ui.watchListTableViewButton->setEnabled(false);
}

void Lab14::populateRecordingsList()
{
	this->ui.recordingListWidget->clear();

	vector<Recording*> allRecordings = this->service.get_all_recordings();
	for (auto recording : allRecordings)
	{
		this->ui.recordingListWidget->addItem(QString::fromStdString(recording->get_title() + " - " + recording->get_location() + " - " +
			std::to_string(recording->get_time_of_creation().tm_mon) + "-" + std::to_string(recording->get_time_of_creation().tm_mday)
			+ "-" + std::to_string(recording->get_time_of_creation().tm_year) + " - " + std::to_string(recording->get_times_accessed()) +
			" - " + recording->get_footage_preview()));
	}

	if (this->service.get_file_path() != "") {
		for (auto recording : allRecordings)
			delete recording;
	}
}

int Lab14::getSelectedIndex() const
{
	QModelIndexList selectedIndexes = this->ui.recordingListWidget->selectionModel()->selectedIndexes();
	if (selectedIndexes.size() == 0)
	{
		this->ui.titleLineEdit->clear();
		this->ui.locationLineEdit->clear();
		this->ui.timeOfCreationLineEdit->clear();
		this->ui.timesAccessedLineEdit->clear();
		this->ui.footagePreviewLineEdit->clear();
		return -1;
	}

	// using single selection
	int selectedIndex = selectedIndexes.at(0).row();
	return selectedIndex;
}

void Lab14::connectSignalsAndSlots()
{
	QObject::connect(this->ui.recordingListWidget, &QListWidget::itemSelectionChanged, this, &Lab14::showRecordingDetails);
	QObject::connect(this->ui.addButton, &QPushButton::clicked, this, &Lab14::addRecording);
	QObject::connect(this->ui.deleteButton, &QPushButton::clicked, this, &Lab14::deleteRecording);
	QObject::connect(this->ui.updateButton, &QPushButton::clicked, this, &Lab14::updateRecording);
	QObject::connect(this->ui.modeAButton, &QPushButton::clicked, this, &Lab14::modeA);
	QObject::connect(this->ui.modeBButton, &QPushButton::clicked, this, &Lab14::changeToModeB);
	QObject::connect(this->ui.undoButton, &QPushButton::clicked, this, &Lab14::undo);
	QObject::connect(this->ui.redoButton, &QPushButton::clicked, this, &Lab14::redo);
	QObject::connect(this->ui.addToWatchListButton, &QPushButton::clicked, this, &Lab14::addToWatchList);
	QObject::connect(this->ui.nextWatchListButton, &QPushButton::clicked, this, &Lab14::nextRecording);
	QObject::connect(this->ui.filterButton, &QPushButton::clicked, this, &Lab14::filterWatchList);
	QObject::connect(this->ui.removeFilterButton, &QPushButton::clicked, this, &Lab14::removeFilter);
	QObject::connect(this->ui.lookAtWatchListButton, &QPushButton::clicked, this, &Lab14::lookAtWatchList);
	QObject::connect(this->ui.watchListTableViewButton, &QPushButton::clicked, this, &Lab14::openMylistTableView);
	QObject::connect(this->shortcutUndo, &QShortcut::activated, this, &Lab14::undo);
	QObject::connect(this->shortcutRedo, &QShortcut::activated, this, &Lab14::redo);
}

void Lab14::addRecording()
{
	string title = this->ui.titleLineEdit->text().toStdString();
	string location = this->ui.locationLineEdit->text().toStdString();
	string timeOfCreation = this->ui.timeOfCreationLineEdit->text().toStdString();
	string timesAccessed = this->ui.timesAccessedLineEdit->text().toStdString();
	string footagePreview = this->ui.footagePreviewLineEdit->text().toStdString();

	if (title.empty() || location.empty() || timeOfCreation.empty() || timesAccessed.empty() || footagePreview.empty())
		QMessageBox::critical(this, "Error", "You must give all the details for the new recording.");
	else {
		try {
			this->service.add_recording(title, location, timeOfCreation, stoi(timesAccessed), footagePreview);
			this->populateRecordingsList();
			int lastElementIndex = this->service.get_recording_list_length() - 1;
			this->ui.recordingListWidget->setCurrentRow(lastElementIndex);
		}
		catch (MyException& exception)
		{
			QMessageBox::critical(this, "Error", QString::fromStdString(exception.get_message()));
		}
	}
}

void Lab14::showRecordingDetails()
{
	string timeOfCration;
	vector<Recording*> recordings_list = this->service.get_all_recordings();
	int selectedIndex = this->getSelectedIndex();

	if (selectedIndex < 0)
		return;

	Recording recording = *recordings_list[selectedIndex];

	this->ui.titleLineEdit->setText(QString::fromStdString(recording.get_title()));
	this->ui.locationLineEdit->setText(QString::fromStdString(recording.get_location()));
	timeOfCration = std::to_string(recording.get_time_of_creation().tm_mon) + "-"
		+ std::to_string(recording.get_time_of_creation().tm_mday)
		+ "-" + std::to_string(recording.get_time_of_creation().tm_year);
	this->ui.timeOfCreationLineEdit->setText(QString::fromStdString(timeOfCration));
	this->ui.timesAccessedLineEdit->setText(QString::fromStdString(std::to_string(recording.get_times_accessed())));
	this->ui.footagePreviewLineEdit->setText(QString::fromStdString(recording.get_footage_preview()));

	if (this->service.get_file_path() != "") {
		for (auto recording_from_list : recordings_list)
			delete recording_from_list;
	}
}

void Lab14::deleteRecording()
{
	int selectedIndex = this->getSelectedIndex();
	vector<Recording*> recordings_list = this->service.get_all_recordings();
	if (selectedIndex < 0)
	{
		QMessageBox::critical(this, "Error", "No recording was selected!");
		return;
	}

	Recording recording = *recordings_list[selectedIndex];

	if (this->service.get_file_path() != "") {
		for (auto recording_from_list : recordings_list)
			delete recording_from_list;
	}

	this->service.delete_recording(recording.get_title());
	this->populateRecordingsList();
}

void Lab14::updateRecording()
{
	int selectedIndex = this->getSelectedIndex();
	vector<Recording*> recordings_list = this->service.get_all_recordings();
	if (selectedIndex < 0)
	{
		QMessageBox::critical(this, "Error", "No recording was selected!");
		return;
	}

	Recording recording = *recordings_list[selectedIndex];

	if (this->service.get_file_path() != "") {
		for (auto recording_from_list : recordings_list)
			delete recording_from_list;
	}

	string title = this->ui.titleLineEdit->text().toStdString();
	string location = this->ui.locationLineEdit->text().toStdString();
	string timeOfCreation = this->ui.timeOfCreationLineEdit->text().toStdString();
	string timesAccessed = this->ui.timesAccessedLineEdit->text().toStdString();
	string footagePreview = this->ui.footagePreviewLineEdit->text().toStdString();

	if (title.empty() || location.empty() || timeOfCreation.empty() || timesAccessed.empty() || footagePreview.empty())
	{
		QMessageBox::critical(this, "Error", "You must give all the details of the recording!");
		return;
	}
	else {
		this->service.update_recording(title, location, timeOfCreation, stoi(timesAccessed), footagePreview);
		this->populateRecordingsList();
		int lastElementIndex = this->service.get_recording_list_length() - 1;
		this->ui.recordingListWidget->setCurrentRow(lastElementIndex);
	}
}

void Lab14::filterWatchList()
{
	vector<Recording*> filtered_recording;
	string location = this->ui.watchListLocationLineEdit->text().toStdString();
	string stringTimesAccessed = this->ui.watchListTimesAccessedLineEdit->text().toStdString();

	if (location.empty() || stringTimesAccessed.empty())
		QMessageBox::critical(this, "Error", "You must give all the details for the new recording.");
	else {
		try {
			int timesAccessed = stoi(stringTimesAccessed);
			filtered_recording = this->service.get_certain_location_recordings_list(location, timesAccessed);
			if (filtered_recording.empty())
			{
				QMessageBox::critical(this, "Error", "There is no recording that meets the required conditions.\n");
			}
			else {
				this->ui.watchListWidget->clear();
				this->populateWatchList(filtered_recording);
			}
		}
		catch (MyException& exception)
		{
			QMessageBox::critical(this, "Error", QString::fromStdString(exception.get_message()));
		}
	}
}

void Lab14::removeFilter()
{
	populateWatchList(this->service.get_watch_list());
}

void Lab14::lookAtWatchList()
{
	try {

		string watch_list_filepath = this->service.get_watch_list_file_path();
		string open_app_name;
		if (watch_list_filepath != "")
		{
			if (watch_list_filepath.find(".html") != -1)
			{
				system(watch_list_filepath.c_str());
			}
			else {
				open_app_name = "notepad.exe " + watch_list_filepath;
				system(open_app_name.c_str());
			}
		}
	}
	catch (MyException exception_returned) {
		cout << exception_returned.get_message();
	}
	catch (exception& exception) {
		cout << exception.what();
	}
}

void Lab14::modeA()
{
	this->ui.addButton->setEnabled(true);
	this->ui.deleteButton->setEnabled(true);
	this->ui.updateButton->setEnabled(true);
	this->ui.undoButton->setEnabled(true);
	this->ui.redoButton->setEnabled(true);
	this->ui.nextWatchListButton->setEnabled(false);
	this->ui.filterButton->setEnabled(false);
	this->ui.removeFilterButton->setEnabled(false);
	this->ui.lookAtWatchListButton->setEnabled(false);
	this->ui.addToWatchListButton->setEnabled(false);
	this->ui.watchListTableViewButton->setEnabled(false);
}

void Lab14::changeToModeB()
{
	this->ui.addButton->setEnabled(false);
	this->ui.deleteButton->setEnabled(false);
	this->ui.updateButton->setEnabled(false);
	this->ui.undoButton->setEnabled(false);
	this->ui.redoButton->setEnabled(false);
	this->ui.nextWatchListButton->setEnabled(true);
	this->ui.filterButton->setEnabled(true);
	this->ui.removeFilterButton->setEnabled(true);
	this->ui.addToWatchListButton->setEnabled(true);
	this->ui.watchListTableViewButton->setEnabled(true);
	if (this->service.get_file_path() != "")
		this->ui.lookAtWatchListButton->setEnabled(true);
}

void Lab14::undo()
{
	try {
		this->service.undoCommand();
		this->populateRecordingsList();
	}
	catch(MyException& exception)
	{
		QMessageBox::critical(this, "Error", QString::fromStdString(exception.get_message()));
	}
}

void Lab14::redo()
{
	try {
		this->service.redoCommand();
		this->populateRecordingsList();
	}
	catch (MyException& exception)
	{
		QMessageBox::critical(this, "Error", QString::fromStdString(exception.get_message()));
	}
}

void Lab14::populateWatchList(vector<Recording*> recordings)
{
	this->ui.watchListWidget->clear();
	
	for (auto recording : recordings)
	{
		this->ui.watchListWidget->addItem(QString::fromStdString(recording->get_title() + " - " + recording->get_location() + " - " +
			std::to_string(recording->get_time_of_creation().tm_mon) + "-" + std::to_string(recording->get_time_of_creation().tm_mday)
			+ "-" + std::to_string(recording->get_time_of_creation().tm_year) + " - " + std::to_string(recording->get_times_accessed()) +
			" - " + recording->get_footage_preview()));
	}

	if (this->service.get_file_path() != "") {
		for (auto recording : recordings)
			delete recording;
	}
}

void Lab14::addToWatchList()
{
	int selectedIndex = this->getSelectedIndex();
	vector<Recording*> recordings_list = this->service.get_all_recordings();
	if (selectedIndex < 0)
	{
		QMessageBox::critical(this, "Error", "No recording was selected!");
		return;
	}

	Recording recording = *recordings_list[selectedIndex];

	try {
		this->service.save_to_watch_list(recording.get_title());
		this->populateWatchList(this->service.get_watch_list());
		int lastElementIndex = this->service.get_watch_list_length() - 1;
		this->ui.watchListWidget->setCurrentRow(lastElementIndex);
		this->watchListWidget->updateTableView();
	}
	catch (MyException& exception)
	{
		QMessageBox::critical(this, "Error", QString::fromStdString(exception.get_message()));
	}
}

void Lab14::nextRecording()
{
	int selectedIndex = this->getSelectedIndex();
	vector<Recording*> recordings_list = this->service.get_all_recordings();
	if (selectedIndex < 0 || selectedIndex == this->service.get_recording_list_length() - 1)
	{
		selectedIndex = 0;
	}
	else
	{
		selectedIndex += 1;
	}
	this->ui.recordingListWidget->setCurrentRow(selectedIndex);
}

void Lab14::openMylistTableView()
{
	this->watchListWidget->show();
}

void Lab14::initShortcuts()
{
	this->shortcutUndo = new QShortcut(QKeySequence(Qt::CTRL + Qt::Key_U), this);
	this->shortcutRedo = new QShortcut(QKeySequence(Qt::CTRL + Qt::Key_R), this);
}