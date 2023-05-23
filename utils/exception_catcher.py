from rich.console import Console
console = Console()


def exception_catch(debug=False):
    def wrap(func):
        def exception_catch_wrapper(*args, **kwargs):
            try:
                result_dict = func(*args, **kwargs)
                return result_dict
            except Exception:
                if debug:
                    console.print_exception(show_locals=True)
                return None
        return exception_catch_wrapper
    return wrap


