import sys
import os
import pickle
import tempfile
import time
from typing import List
from functools import wraps
from contextlib import contextmanager

from cairosvg import svg2png

from rich import box
from rich.align import Align
from rich.console import Console
from rich.live import Live
from rich.table import Table
from rich.text import Text

from javascript import require
sys.path.insert(0,r'./') #Add root directory here
img_display = require("../utils/img_display.mjs")
console = Console()


BEAT_TIME = 0.04
GOOGLE_MARKDOWN = "[bold blue] G[/bold blue][bold red]o[/bold red]" \
                  "[bold yellow]o[/bold yellow][bold blue]g[/bold blue]" \
                  "[bold green]l[/bold green][bold red]e[/bold red]"


@contextmanager
def beat(length: int = 1) -> None:
    yield
    time.sleep(length * BEAT_TIME)


def generate_table(table_data: List[List]):
    table = Table(show_footer=False, box=box.HEAVY_EDGE)
    table_centered = Align.center(table)
    with Live(table_centered, console=console, screen=False, refresh_per_second=20):
        with beat(10):
            table.title = f"{GOOGLE_MARKDOWN}\nRetrieved links to crawl"

        with beat(10):
            table.title = (
                f"{GOOGLE_MARKDOWN}\n[bold green] Retrieved links to crawl [/bold green]"
            )

        with beat(2):
            table.add_column("Num", no_wrap=True)

        with beat(2):
            table.add_column("[bold blue] Links [/bold blue]", no_wrap=True)

        for row in table_data:
            with beat(5):
                table.add_row(*row)


def display_img(img_url=None, svg_code=None, size: float = None):

    size = '100%' if size is None else size
    if isinstance(size, float):
        size *= 100
        size = str(size) + '%'

    if img_url is not None:
        img_display.display_img(img_url, size, {'method': 'open image from web'})
        return
    if svg_code is not None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = os.path.join(temp_dir ,'temp_svg.png')
            svg2png(bytestring=svg_code, write_to=temp_path)
            img_display.display_img(temp_path, size, {'method': 'load saved svg image'})
            return


def markdown_print(msg: str, mark_downs: List[str]):

    from rich.console import Console
    console = Console()

    style = {
        "underline": f"[u] {temp_msg} [/u]",
        "italic": f"[i] {temp_msg} [/i]",
        "bold red": f"[{mark_down}] {temp_msg} [/{mark_down}]"
    }


    console.print()
    console.print(f'\n [u]No result found![/u]\n', style="bold red")


def parse_print(func):
    @wraps(func)
    def parse_print_wrapper(*args, **kwargs):
        result_dict = func(*args, **kwargs)
        if result_dict is None:
            console.print(f'\n [u]No result found![/u]\n', style="bold red")

            return None

        if result_dict['type'] == 'solution':
            title = result_dict['title']
            num_ans = result_dict['num_ans']
            parse_page = result_dict['solution']
            img_obj = result_dict['profile_url']
            print(f'\n Problem title: {title}')
            print(f' Number of answer in the discuss: {num_ans}')
            print(f'\n Correct answer: ')
            print('-' * 17)
            display_img(img_url=img_obj, size=0.42)
            print(f'{parse_page.strip()}')
            print('-' * 17)

            return result_dict

        if result_dict['type'] == 'definition':
            title = result_dict['title']
            parse_page = result_dict['def']
            print(f'\n  Definition title: {title}')
            print(f'\n Definition: ')
            print('-' * 17)
            print(f'{parse_page.strip()}')
            print('-' * 17)

            return result_dict

        if result_dict['type'] == 'weather':
            weather_info = result_dict['weather_info']
            svg = result_dict['svg']

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
            display_img(svg_code=svg, size=0.55)
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
            return result_dict

    return parse_print_wrapper

