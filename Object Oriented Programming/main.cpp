#include "Lab14.h"
#include <QtWidgets/QApplication>
#include "Tests.h"

int main(int argc, char *argv[])
{
	QApplication app(argc, argv);
	ifstream configurationFile{ "ConfigurationFile.txt" };
	string line, repository_path, watch_list_path, line_copy;
	std::shared_ptr<InMemoryRepository> repository;
	int position;

	std::getline(configurationFile, line);
	if (line.find("file") != std::string::npos)
	{
		std::getline(configurationFile, line);
		position = line.find("=");
		line.erase(0, position + 1);
		repository_path = line;

		std::getline(configurationFile, line);
		line_copy = line;
		position = line_copy.find_last_of(".");
		line_copy.erase(0, position);

		watch_list_path = line.erase(0, line.find("=") + 1);

		if (line_copy == ".csv")
		{
			repository = std::make_shared<RepositoryWithCSV>(repository_path, watch_list_path);
		}
		else if (line_copy == ".html")
		{
			repository = std::make_shared<HtmlRepository>(repository_path, watch_list_path);
		}
	}
	else // it will be an inmemory repository
	{
		repository = std::make_shared<InMemoryRepository>();
	}

	Service service{ repository.get() };

	Lab14 gui{ service };
	gui.show();

	return app.exec();
}
