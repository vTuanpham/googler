from functools import wraps


def exception_catch(func):
    @wraps(func)
    def exception_catch_wrapper(*args, **kwargs):
        try:
            result_dict = func(*args, **kwargs)
            return result_dict
        except:
            return None

    return exception_catch_wrapper
