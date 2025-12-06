class EmailError(Exception):
    pass
class Oops(Exception):
    def __init__(self, message="Что-то пошло не так!"):
        self.message = message
        super().__init__(self.message)
class ToLarge(Exception):
    def __init__(self, message="Текст слишком длинный!"):
        self.message = message
        super().__init__(self.message)
class ToMin(Exception):
    def __init__(self, message="Текст слишком маленький!"):
        self.message = message
        super().__init__(self.message)
class StringType(Exception):
    def __init__(self, message="Строковая ошибка!"):
        self.message = message
        super().__init__(self.message)
class IntType(Exception):
    def __init__(self, message="Целочисленная ошибка!"):
        self.message = message
        super().__init__(self.message)
class Validate:
    @staticmethod
    def validate_email(email):
        if "@" not in email or '.' not in email.split("@")[-1]:
            raise EmailError(f"Некорректный email: {email}")
        return True
    @staticmethod
    def tolong(enter: str, long: int):
        if len(enter) > long:
            raise ToLarge()
        return True
    @staticmethod
    def tomin(enter: str, long: int):
        if len(enter) < long:
            raise ToMin()
        return True
