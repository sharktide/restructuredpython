import time
import inspect
from functools import wraps
from typing import get_type_hints


class decorators:
    @staticmethod
    def access_control(allowed_roles):
        def decorator(func):
            def wrapper(user_role, *args, **kwargs):
                if user_role not in allowed_roles:
                    raise PermissionError("Access Denied")
                return func(*args, **kwargs)
            return wrapper
        return decorator

    @staticmethod
    def logging(func):
        def wrapper(*args, **kwargs):
            print(
                f"Calling {
                    func.__name__} with args: {args}, kwargs: {kwargs}")
            result = func(*args, **kwargs)
            print(f"{func.__name__} returned {result}")
            return result
        return wrapper

    @staticmethod
    def memoization(func):
        cache = {}

        def wrapper(*args):
            if args in cache:
                return cache[args]
            result = func(*args)
            cache[args] = result
            return result
        return wrapper

    @staticmethod
    def retry(retries=3, delay=1):
        def decorator(func):
            def wrapper(*args, **kwargs):
                for attempt in range(retries):
                    try:
                        return func(*args, **kwargs)
                    except Exception as e:
                        print(f"Attempt {attempt + 1} failed: {e}")
                        time.sleep(delay)
                raise Exception("All retries failed.")
            return wrapper
        return decorator

    @staticmethod
    def timer(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            print(f"{func.__name__} took {end_time - start_time:.2f} seconds.")
            return result
        return wrapper

    @staticmethod
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
