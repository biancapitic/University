from Exceptions.exceptions import HamurabiException

class Validator():
    @staticmethod
    def validate_business_acres(business_acres, game_information):
        if business_acres < 0 and game_information.city_acres + business_acres < 0:
            raise HamurabiException("You don\'t have that many acres to sell. Try again.")
        if business_acres > 0 and game_information.grain_stocks -  game_information.land_price * business_acres < 0:
            raise HamurabiException("You don\'t have enough units to buy so many acres.")

    @staticmethod
    def validate_units_for_population(units_for_population, game_information):
        total_grain = game_information.grain_stocks
        if total_grain - units_for_population < 0:
            raise HamurabiException("You can\'t feed the people with so many units, because you don\'t have them.")

    @staticmethod
    def validate_acres_to_plant(acres_to_plant, game_information):
        total_acres = game_information.city_acres
        if acres_to_plant > total_acres or acres_to_plant > game_information.grain_stocks:
            raise HamurabiException("You don'\t have that many acres to plant.")
