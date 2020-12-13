from random import randrange

from Validator.validator import Validator

class Service():
    def __init__(self, repository):
        self._repository = repository

    def get_game_information(self):
        return self._repository.get_game_information()

    def update_land_price(self):
        new_price = randrange(15, 26)
        self._repository.update_land_price(new_price)

    def buy_or_sell_land(self, business_acres):
        game_information = self._repository.get_game_information()
        new_number_city_acres = game_information.city_acres
        new_grain_stocks = game_information.grain_stocks
        if business_acres != 0:
            # sell
            if business_acres < 0:
                new_number_city_acres += business_acres
                new_grain_stocks += game_information.land_price * (-1) * business_acres
            # buy
            elif business_acres > 0:
                new_number_city_acres += business_acres
                new_grain_stocks -= game_information.land_price * business_acres
            self._repository.update_city_acres(new_number_city_acres)
            self._repository.update_grain_stocks(new_grain_stocks)

    def get_number_of_new_people_to_city(self):
        new_people_number = randrange(0,11)
        return new_people_number

    def feed_population(self, units_for_population):
        game_information = self._repository.get_game_information()
        people_number = game_information.city_population
        if 20 * people_number > units_for_population:
            fed_people = units_for_population // 20
            if people_number - fed_people > people_number // 2:
                return 'Game over!'
            else:
                self._repository.update_city_population(people_number - (people_number - fed_people))
                self._repository.update_starved_people(people_number - fed_people)
                self._repository.update_new_people_number(0)
        else:
            new_people_to_city_number = self.get_number_of_new_people_to_city()
            self._repository.update_new_people_number(new_people_to_city_number)
            self._repository.update_city_population(people_number + new_people_to_city_number)
            self._repository.update_starved_people(0)
        self._repository.update_grain_stocks(game_information.grain_stocks - units_for_population)

    def update_harvest_price(self):
        new_harvest_price = randrange(1, 7)
        self._repository.update_harvest_price(new_harvest_price)

    def harvest_grain(self):
        grain_harvested = 0
        game_information = self._repository.get_game_information()
        if game_information.city_population * 10 <= game_information.city_acres:
            grain_harvested = game_information.city_population * 10 * game_information.harvest_price
        else:
            grain_harvested = game_information.city_acres * game_information.harvest_price
        self._repository.update_grain_stocks(game_information.grain_stocks + grain_harvested)

    def rats_infestation(self):
        chance = randrange(1, 6)
        if chance == 1:
            game_information = self._repository.get_game_information()
            rat_grain = 0.1 * game_information.grain_stocks
            self._repository.update_grain_stocks(game_information.grain_stocks - rat_grain)

    def one_year(self, year, acres_business, units_for_population, acres_plant):
        game_information = self._repository.get_game_information()
        Validator.validate_business_acres(acres_business, game_information)
        Validator.validate_units_for_population(units_for_population, game_information)
        Validator.validate_acres_to_plant(acres_plant, game_information)
        self.update_land_price()
        self.buy_or_sell_land(acres_business)
        message = self.feed_population(units_for_population)
        self.update_harvest_price()
        self.harvest_grain()
        self.rats_infestation()
        self._repository.update_year(year)
        return message

    def end_game(self):
        game_information = self._repository.get_game_information()
        if game_information.city_population >= 100 and game_information.city_acres >= 1000:
            return "Congratulation! You won!"
        else:
            return 'Sorry, you lost!'
