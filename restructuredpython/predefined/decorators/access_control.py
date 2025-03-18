def access_control(allowed_roles):
    def decorator(func):
        def wrapper(user_role, *args, **kwargs):
            if user_role not in allowed_roles:
                raise PermissionError("Access Denied")
            return func(*args, **kwargs)
        return wrapper
    return decorator
