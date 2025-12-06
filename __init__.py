from .core import testing
from .errors import Error
from .validation import Validate, EmailError, Oops, ToLarge, ToMin, StringType, IntType

__version__ = "0.1.0"
__all__ = [
    'testing',
    'Error',
    'Validate',
    'EmailError',
    'Oops',
    'ToLarge',
    'ToMin',
    'StringType',
    'IntType'
    ]

check_types = testing.check_types
check_errors = testing.check_errors
test_types = testing.test_types
timer_ms = testing.timer_ms
error_handler = Error.error_handler
