import traceback


def exception_catch(debug=False):
    def wrap(func):
        def exception_catch_wrapper(*args, **kwargs):
            try:
                result_dict = func(*args, **kwargs)
                return result_dict
            except Exception as e:
                if debug:
                    traceback.print_tb(e.__traceback__)
                return None

        return exception_catch_wrapper
    return wrap


