import time
from functools import wraps
class Error:
    exception_errs = {
        'ZeroDivisionError': ZeroDivisionError,
        'TypeError': TypeError,
        'NameError': NameError,
        'ValueError': ValueError,
        'IndexError': IndexError,
        'KeyError': KeyError,
        'FileNotFoundError': FileNotFoundError,
        'AttributeError': AttributeError,
        'ImportError': ImportError,
        'RuntimeError': RuntimeError,
        'ArithmeticError': ArithmeticError,
        'AssertionError': AssertionError,
        'BufferError': BufferError,
        'LookupError': LookupError,
        'MemoryError': MemoryError,
        'OSError': OSError,
        'ReferenceError': ReferenceError,
        'StopAsyncIteration': StopAsyncIteration,
        'StopIteration': StopIteration,
        'SystemError': SystemError,
        'Warning': Warning,
        'SyntaxError': SyntaxError,
        'KeyboardInterrupt': KeyboardInterrupt,
        'OverflowError': OverflowError,
        'ModuleNotFoundError': ModuleNotFoundError,
        'IndentationError': IndentationError,
        'UnicodeError': UnicodeError,
        'TabError': TabError,
        'UnicodeDecodeError': UnicodeDecodeError,
        'UnicodeEncodeError': UnicodeEncodeError,
        'UnicodeTranslateError': UnicodeTranslateError,
        'EOFError': EOFError,
        'NotADirectoryError': NotADirectoryError,
        'ChildProcessError': ChildProcessError,
        'TimeoutError': TimeoutError,
        'BlockingIOError': BlockingIOError,
        'PermissionError': PermissionError,
        'IsADirectoryError': IsADirectoryError,
        'ConnectionError': ConnectionError,
        'UserWarning': UserWarning,
        'FutureWarning': FutureWarning
        }
    def error_handler(typeerr="all", simple=False):
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                if simple == False:
                    print(f"Анализ функции {func.__name__}")
                    if typeerr == "all" or typeerr == "All":
                        try:
                            start = time.time()
                            result = func(*args, **kwargs)
                            end = time.time()
                            res = end-start
                            return f"Анализ функции завершен. Результат \u001b[48;5;34m успешный \u001b[0m\nВывод:\n {result}\n Время выполнения: {res*1000:.5f} ms."
                        except Exception as error:
                            end = time.time()
                            res = end-start
                            return f"Анализ функции завершен. Получена \u001b[48;5;124m ошибка \u001b[0m:\n {type(error).__name__}: {error}\n Завершенное время: {res*1000:.5f} ms."
                    elif typeerr in Error.exception_errs:
                        error_class = Error.exception_errs[typeerr]
                        try:
                            try:
                                start = time.time()
                                result = func(*args, **kwargs)
                                end = time.time()
                                res = end-start
                                return f"Анализ функции завершен. Результат \u001b[48;5;34m успешный \u001b[0m\nВывод:\n {result}\n Время выполнения: {res*1000:.5f} ms."
                            except error_class as error:
                                end = time.time()
                                res = end-start
                                return f"Анализ функции завершен. Получена \u001b[48;5;124m ошибка \u001b[0m:\n {type(error).__name__}: {error}\n Завершенное время: {res*1000:.5f} ms."
                        except Exception as error:
                            return f"Анализ функции завершен. Получена \u001b[48;5;124m ошибка \u001b[0m:\n {type(error).__name__}: {error}\n \u001b[48;5;172m Примечание \u001b[0m: Эта функция проверяет выполнение функции {func.__name__}. Попробуйте исправить существующий код, чтобы не было ошибок."
                    else:
                        return f"Получена \u001b[48;5;124m ошибка \u001b[0m:\n Нет такой ошибки!"
                else:
                    if typeerr == "all" or typeerr == "All":
                        try:
                            return func(*args, **kwargs)
                        except Exception as error:
                            return f"{type(error).__name__}: {error}"
                    elif typeerr in Error.exception_errs:
                        error_class = Error.exception_errs[typeerr]
                        try:
                            return func(*args, **kwargs)
                        except error_class as error:
                            return f"{type(error).__name__}: {error}"
                    else:
                        return f"Получена \u001b[48;5;124m ошибка \u001b[0m:\n Нет такой ошибки!"
            return wrapper
        return decorator
