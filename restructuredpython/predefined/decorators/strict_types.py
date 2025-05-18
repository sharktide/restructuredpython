import inspect
from functools import wraps
from typing import get_type_hints


def strict_types(func):
    sig = inspect.signature(func)
    type_hints = get_type_hints(func)

    @wraps(func)
    def wrapper(*args, **kwargs):
        bound_args = sig.bind(*args, **kwargs)
        bound_args.apply_defaults()

        # Check argument types
        for name, value in bound_args.arguments.items():
            expected_type = type_hints.get(name)
            if expected_type and not isinstance(value, expected_type):
                raise TypeError(
                    f"Argument '{name}' expected {
                        expected_type.__name__}, got {
                        type(value).__name__}")

        # Call the function
        result = func(*args, **kwargs)

        # Check return type
        expected_return = type_hints.get('return')
        if expected_return and not isinstance(result, expected_return):
            raise TypeError(
                f"Return value expected {
                    expected_return.__name__}, got {
                    type(result).__name__}")

        return result

    return wrapper
