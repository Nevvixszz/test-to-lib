import time
import inspect
from functools import wraps
import random
import string
from error_handlers.errors import Error
class testing:
    def doctype():
        # Auto Documentation for users
        # In 1.1v ctl_CLI
        pass
    @staticmethod
    def check_types(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"Анализ функции: {func.__name__}")
            if func.__doc__:
                print(f"Описание: {func.__doc__.strip()}")
            try:
                sig = inspect.signature(func)
                annotations = func.__annotations__
                bound_args = sig.bind(*args, **kwargs)
                errors = 0
                print("Аргументы:")
                for name, value in bound_args.arguments.items():
                    expected_type = annotations.get(name)
                    actual_type = type(value)
                    if expected_type:
                        if isinstance(value, expected_type):
                            print(f"{name}: {value} ({actual_type.__name__})")
                        else:
                            errors += 1
                            print(f"\u001b[48;5;124m Ошибка \u001b[0m: {name}: {value} ({actual_type.__name__})\n - Ожидалось: {expected_type.__name__}")
                return f"Анализ функции {func.__name__} завершен\n - {f'Найдено \u001b[48;5;124m ошибок \u001b[0m: {errors}' if errors else '\u001b[48;5;34m Анализ успешный \u001b[0m'}"
            except Exception as error:
                print(f"При проверке произошла \u001b[48;5;124m ошибка \u001b[0m:\n {type(error).__name__}: {error}")
        return wrapper
    @staticmethod
    def check_errors(Comment=False):
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                print(f"Выполняется функция {func.__name__}")
                try:
                    start = time.time()
                    result = func(*args, **kwargs)
                    end = time.time()
                    res = end - start
                    if Comment == True:
                        print(f"Документация: {func.__doc__}")
                    return f"Результат выполнения \u001b[48;5;34m успешный \u001b[0m.\nВывод: {result}\n Время выполнения: {res*1000:.5f} ms."
                except Exception as error:
                    end = time.time()
                    res = end - start
                    import sys
                    exc_type, exc_obj, exc_tb = sys.exc_info()
                    print(f"При выполнении произошла \u001b[48;5;124m ошибка \u001b[0m:\n {exc_type.__name__} - {str(error)}\n Прошло времени перед ошибкой: {res*1000:.5f} ms.")
                    return False
            return wrapper
        return decorator
    @staticmethod
    def test_types(tests=3):
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                try:
                    print(f"Тест аргументов в функции {func.__name__}")
                    sig = inspect.signature(func)
                    type_name = None
                    for test_num in range(tests):
                        print(f"\n Тест {test_num + 1}")
                        test_args = []
                        for param_name, param in sig.parameters.items():
                            param_type = param.annotation
                            if param_type == int:
                                value = random.randint(1, 100)
                            elif param_type == float:
                                value = round(random.uniform(1.0, 100.0), 2)
                            elif param_type == str:
                                value = ''.join(random.choices(string.ascii_letters, k=5))
                            elif param_type == bool:
                                value = random.choice([True, False])
                            elif param_type == list:
                                import numpy
                                value = numpy.random.randint(0, 10, 2)
                            else:
                                value = random.randint(1, 10)
                                type_name = 1
                            test_args.append(value)
                            print(f" {param_name}: {value} ({'int' if type_name else param_type.__name__ })")
                        try:
                            result = func(*test_args)
                            print(f"Результат: {result}")
                            if type_name:
                                print(" \u001b[48;5;172m Примечание \u001b[0m: у вас не указаны аргументы, по умолчанию используется int. Чтобы не возникали ошибки, укажите явно типы аргументов!")
                        except Exception as error:
                            print(f"\u001b[48;5;124m Ошибка \u001b[0m: {error}")
                except Exception as error:
                    print(f"\u001b[48;5;124m Ошибка \u001b[0m: {error}")
                return "Анализ аргументов завершился"
            return wrapper
        return decorator
    @staticmethod
    def timer_ms(timer=1):
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                start = time.time()
                result = func(*args, **kwargs)
                end = time.time()
                res = end-start
                if res > timer:
                    return f"Анализ функции завершен\n Функция выполнялась {res * 1000} ms.\n \u001b[48;5;172m Примечание \u001b[0m: был превышен лимит {timer} sec! Ваша функция работает дольше чем указано в параметре."
                else:
                    return f"Анализ функции завершен\n Функция выполнялась {res * 1000} ms."
                return result
            return wrapper
        return decorator
