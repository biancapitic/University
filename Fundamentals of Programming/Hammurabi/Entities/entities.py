class GameInformation():
    def __init__(self, year, starved_people_number, new_people_number, city_population,
                 city_acres, harvest_price, rats_units, land_price, grain_stocks):
        self._year = year
        self._starved_people_number = starved_people_number
        self._new_people_number = new_people_number
        self._city_population = city_population
        self._city_acres = city_acres
        self._harvest_price = harvest_price
        self._rats_units = rats_units
        self._land_price = land_price
        self._grain_stocks = grain_stocks

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, new_value):
        self._year = new_value

    @property
    def starved_people_number(self):
        return self._starved_people_number

    @starved_people_number.setter
    def starved_people_number(self, new_value):
        self._starved_people_number = new_value

    @property
    def new_people_number(self):
        return self._new_people_number

    @new_people_number.setter
    def new_people_number(self, new_value):
        self._new_people_number = new_value

    @property
    def city_population(self):
        return self._city_population

    @city_population.setter
    def city_population(self, new_value):
        self._city_population = new_value

    @property
    def city_acres(self):
        return self._city_acres

    @city_acres.setter
    def city_acres(self, new_value):
        self._city_acres = new_value

    @property
    def harvest_price(self):
        return self._harvest_price

    @harvest_price.setter
    def harvest_price(self, new_value):
        self._harvest_price = new_value

    @property
    def rats_units(self):
        return self._rats_units

    @rats_units.setter
    def rats_units(self, new_value):
        self._rats_units = new_value

    @property
    def land_price(self):
        return self._land_price

    @land_price.setter
    def land_price(self, new_value):
        self._land_price = new_value

    @property
    def grain_stocks(self):
        return self._grain_stocks

    @grain_stocks.setter
    def grain_stocks(self, new_value):
        self._grain_stocks = new_value

    def __str__(self):
        string = ''
        string += 'In year ' + str(self._year) + ','
        string += str(self._starved_people_number) + ' people starved.\n'
        string += str(self._new_people_number) + ' people came to city.\n'
        string += 'City population is ' + str(self._city_population) + '.\n'
        string += 'City owns ' + str(self._city_acres) + ' acres of land.\n'
        string += 'Harvest was ' + str(self._harvest_price) + ' units per acre.\n'
        string += 'Rats ate ' + str(self._rats_units) + ' units.\n'
        string += 'Land price is ' + str(self._land_price) + ' units per acre.\n'
        string += 'Grain stocks are ' + str(self._grain_stocks) + ' units.'
        return string