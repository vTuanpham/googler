import time
from functools import wraps


def parse_print(func):
    @wraps(func)
    def parse_print_wrapper(*args, **kwargs):
        try:
            title, num_ans, parse_page = func(*args, **kwargs)
            print(f'\n Problem title: {title}')
            print(f' Number of answer in the discuss: {num_ans}')
            print(f'\n Correct answer: ')
            print('-' * 17)
            print(f'{parse_page.strip()}')
            print('-' * 17)

            return title, num_ans, parse_page
        except ValueError:
            title, parse_page = func(*args, **kwargs)
            print(f'\n  Definition title: {title}')
            print(f'\n Definition: ')
            print('-' * 17)
            print(f'{parse_page.strip()}')
            print('-' * 17)

            return title, parse_page

    return parse_print_wrapper

