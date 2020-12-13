class MyAppError(Exception):
    pass


class RepositoryError(MyAppError):
    pass


class ValidatorError(MyAppError):
    pass


class RentalError(MyAppError):
    pass


class EmptyError(MyAppError):
    pass


class EOFBinaryError(MyAppError):
    pass