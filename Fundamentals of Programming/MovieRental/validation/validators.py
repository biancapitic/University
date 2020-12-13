from exception.errors import ValidatorError

class GeneralValidator:
    def __init__(self):
        pass

    def IdExists(self, id, elements_list):
        if id in elements_list:
            raise ValidatorError('Id already in the list')
    def IdFound(self, id, elements_list):
        if id in elements_list:
            return True
        raise ValidatorError('Id ' + str(id) + ' not found.')

class MovieValidator:
    def __init__(self):
        pass

    def ValidateId(self, id):
        if id < 0:
            raise ValidatorError('Id must be a positive integer.')

    def ValidateAttribute(self, attribute):
        if attribute not in ['id', 'title', 'description', 'genre']:
            raise ValidatorError('Field does not exist.')

class ClientValidator:
    def __init__(self):
        pass
    def ValidateId(self, id):
        if id < 0:
            raise ValidatorError('Id must be a positive integer.')
    def ValidateAttribute(self, attribute):
        if attribute not in ['id', 'name']:
            raise ValidatorError('Field does not exist.')

class RentalValidator:
    def __init__(self):
        pass

    def ValidateId(self, id):
        if id < 0:
            raise ValidatorError('Id must be a positive integer.')

    def ValidateDate(self, date):
        # check if string date has characters which represent digits at the right positions.
        if not (date[0] >= '0' and date[0] <= '9' and date[1] >= '0' and date[1] <= '9' and date[3] >= '0' and date[3] <= '9' \
                    and date[4] >= '0' and date[4] <= '9' and date[6] >= '0' and date[6] <= '9' and date[7] >= '0' and date[7] <= '9' \
                and date[8] >= '0' and date[8] <= '9' and date[9] >= '0' and date[9] <= '9' and date[2] == '.' and date[5] == '.'):
                raise ValidatorError('Format of the date is not ok.')

        # check if the year is ok
        year = int(date[6:])
        if year < 1000:
            raise ValidatorError('Year of date is not ok.')

        # check if the month is ok
        if date[3] == '0':
            month = int(date[4])
        else:
            month = int(date[3:5])
        if month < 1 or month > 12:
            raise ValidatorError('Month of date is not ok.')

        #check if the day is ok
        if date[0] == '0':
            day = int(date[1])
        else:
            day = int(date[0:2])

        if month in [4, 6, 9, 11] and (day > 30 or day < 1):
            raise ValidatorError('Day of date is not ok.')
        if month in [1, 3, 5, 7, 8, 12] and (day > 31 or day < 1):
            raise ValidatorError('Day of date is not ok.')
        if month == 2 and (day > 29 or day < 1):
            raise ValidatorError('Day of date is not ok.')
