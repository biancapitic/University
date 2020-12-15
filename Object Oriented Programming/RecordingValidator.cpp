#include "RecordingValidator.h"


void	RecordingValidator::validate(vector<Recording*>& recordings, Recording& recording)
{
	auto condition = [&](Recording* r) {return r->get_title() == recording.get_title(); };
	if (std::find_if(recordings.begin(), recordings.end(), condition) != recordings.end())
	{
		throw MyException("A recording with that name already exists.\n");
	}
}