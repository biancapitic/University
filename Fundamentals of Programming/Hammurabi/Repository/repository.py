from Entities.entities import GameInformation


class GameRepository():
    def __init__(self):
        self._game = GameInformation(1, 0, 0, 100, 1000, 3, 200, 20, 2800)

    def get_game_information(self):
        return self._game

    def update_land_price(self, new_price):
        self._game.land_price = new_price

    def update_city_acres(self, new_acres_number):
        self._game.city_acres = new_acres_number

    def update_grain_stocks(self, new_grain_stocks):
        self._game.grain_stocks = new_grain_stocks

    def update_new_people_number(self, new_new_people_number):
        self._game.new_people_number = new_new_people_number

    def update_city_population(self, new_city_population):
        self._game.city_population = new_city_population

    def update_harvest_price(self, new_harvest_price):
        self._game._harvest_price = new_harvest_price

    def update_year(self, year):
        self._game._year = year

    def update_starved_people(self, nb_starved_people):
        self._game._starved_people_number = nb_starved_people
