from Exceptions.exceptions import HamurabiException

class UI:
    def __init__(self, service):
        self._service = service

    def __print_current_situation(self):
        game = self._service.get_game_information()
        print(game)

    def __ui_year_decisions(self, year):
        try:
            acres_business = int(input("Acres to buy/sell(+/-)-> "))
            units_for_population = int(input("Units to feed the population-> "))
            acres_plant = int(input("Acres to plant->"))
            message = self._service.one_year(year, acres_business, units_for_population, acres_plant)
            return message
        except HamurabiException as he:
            print(he + "Try again!")
        except ValueError as ve:
            print("It must be an integer.")

    def play_game(self):
        year = 1
        while year <= 4:
            self.__print_current_situation()
            print()
            message = self.__ui_year_decisions(year + 1)
            if message:
                print(message)
                break
            year += 1
        if year == 5:
            self.__print_current_situation()
            message = self._service.end_game()
            print(message)