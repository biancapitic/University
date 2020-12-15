#pragma once
#include "InMemoryRepository.h"
#include <vector>

using std::vector;

class RecordingValidator {
public:
	void validate(vector<Recording*>&, Recording&);
};