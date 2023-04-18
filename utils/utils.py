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
            pass

        try:
            title, parse_page = func(*args, **kwargs)
            print(f'\n  Definition title: {title}')
            print(f'\n Definition: ')
            print('-' * 17)
            print(f'{parse_page.strip()}')
            print('-' * 17)

            return title, parse_page
        except ValueError:
            pass

        try:
            weather_info = func(*args, **kwargs)

            # Remove unwanted spaces in string
            re_weather_info = []
            for info_category in weather_info:
                re_info_category = []
                for info in info_category:
                    re_info = " ".join(info.split())
                    re_info_category.append(re_info)
                re_weather_info.append(re_info_category)
            weather_info = re_weather_info

            print(f'\n Weather information: ')
            print(f'\n Current weather info on date {weather_info[1][0]}: ')

            print('-' * 17)
            cur_weather_info = weather_info[0]
            print(f'Last update: {cur_weather_info[0]}')
            print(f'Current temperature: {cur_weather_info[1]}')
            print(f'Current real feel temperature: {cur_weather_info[2]}'+'C')
            print(f'Current weather description: {cur_weather_info[3]}')
            print('-' * 17)

            print(f'\n Current air quality: ')
            print('-' * 17)
            cur_air_quality = weather_info[1]
            print(f'Air quality AQI: {cur_air_quality[1]}')
            print(f'Air quality description: {cur_air_quality[2]}')
            print(f'Air quality statement: {cur_air_quality[3]}')
            print('-' * 17)

            print(f'\n Tomorrow weather info on date {weather_info[2][0]}: ')
            print('-' * 17)
            tomorrow_weather_info = weather_info[2]
            print(f'Tomorrow temperature: {tomorrow_weather_info[1]}')
            print(f'Tomorrow real feel temperature: {tomorrow_weather_info[2]}')
            print(f'Tomorrow weather description: {tomorrow_weather_info[3]}')
            print('-' * 17)
            return weather_info

        except ValueError:
            pass

    return parse_print_wrapper

