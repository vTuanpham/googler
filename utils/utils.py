import time
from functools import wraps


def parse_print(func):
    @wraps(func)
    def parse_print_wrapper(*args, **kwargs):
        try:
            title, num_ans, parse_page = func(*args, **kwargs)
            print(f'Problem title: {title}')
            print(f'Number of answer in the discuss: {num_ans}')
            print(f'\nCorrect answer: ')
            print(parse_page.strip())

            return title, num_ans, parse_page
        except:
            title, parse_page = func(*args, **kwargs)
            print(f'Definition title: {title}')
            print(parse_page.strip())

            return title, parse_page

    return parse_print_wrapper

