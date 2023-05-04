import sys
import requests
from javascript import require
sys.path.insert(0,r'./') #Add root directory here
from typing import List
from bs4 import BeautifulSoup
from utils.utils import parse_print
from utils.exception_catcher import exception_catch
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
img_display = require("../utils/img_display.mjs")


debug_mode_global = False


class Googler:
    def __init__(self, search_engine='google',debug_mode=False):
        global debug_mode_global
        debug_mode_global = debug_mode
        self.debug_mode = debug_mode
        # Query string parameters to crawl through results pages
        self.init_params = {
            'sxsrf': 'ACYBGNRmhZ3C1fo8pX_gW_d8i4gVeu41Bw:1575654668368',
            'ei': 'DJXqXcmDFumxrgSbnYeQBA',
            'start': '',
            'sa': 'N',
            'ved': '2ahUKEwjJua-Gy6HmAhXpmIsKHZvOAUI4FBDy0wN6BAgMEDI',
            'biw': '811',
            'bih': '628'
        }

        # Request headers
        self.init_headers = {
            'accept': '*/*',
            'accept-language': 'en,vi;q=0.9,en-CA;q=0.8,en-NZ;q=0.7,vi-VN;q=0.6,en-GB;q=0.5,en-US;q=0.4',
            'cache-control': 'no-cache',
            'pragma': 'no-cache',
            'referer': 'https://www.google.com/',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
        }

        # Init proxy
        self.proxy = {
            "http": 'https://159.223.41.3:5000'
        }

        self.search_engine = search_engine

    def fetch_html(self, page=None, url=None):

        proxy = self.proxy

        if page == 'stackoverflow':
            params = self.init_params
            headers = self.init_headers
            headers.update({'referer': 'https://stackoverflow.com/',
                            'origin': 'https://stackoverflow.com'})

        if page == 'stackexchange':
            params = self.init_params
            headers = self.init_headers
            headers.update({'referer': 'https://academia.stackexchange.com/',
                            'origin': 'https://academia.stackexchange.com'})

        if page == 'codegolf_stackexchange':
            params = self.init_params
            headers = self.init_headers
            headers.update({'referer': 'https://codegolf.stackexchange.com/',
                            'origin': 'https://codegolf.stackexchange.com'})

        if page == 'math_stackexchange':
            params = self.init_params
            headers = self.init_headers
            headers.update({'referer': 'https://math.stackexchange.com/',
                            'origin': 'https://math.stackexchange.com'})

        if page == 'wiki':
            params = self.init_params
            headers = self.init_headers
            headers.update({'referer': 'https://en.wikipedia.org/',
                            'origin': 'https://en.wikipedia.org'})

        if page == 'Accweather':
            params = self.init_params
            headers = self.init_headers
            headers.update({'referer': 'https://www.accuweather.com/',
                            'origin': 'https://www.accuweather.com'})

        if page == 'pytorch':
            options = Options()
            options.add_argument("--headless")
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
            browser = webdriver.Chrome(options=options)
            browser.get(url)

            return browser

        response = requests.get(url=url, params=params, headers=headers, proxies=proxy)

        return response

    def fetch_search_html(self, query):

        proxy = self.proxy

        if self.search_engine == 'google':
            params = self.init_params
            params.update({'q': query})
            headers = self.init_headers
            url = 'https://www.google.com/search'

        if self.search_engine == 'bing':
            params = self.init_params
            params.update({'q': query})
            headers = self.init_headers
            headers.update({'referer': 'https://www.bing.com/',
                            'origin': 'https://www.bing.com'})
            url = 'https://www.bing.com/search'

        response = requests.get(url=url, params=params, headers=headers, proxies=proxy)

        return response

    def parse_url(self, robj, class_name=None):

        soup = BeautifulSoup(robj.text, 'lxml')
        href_list = []
        featured_ans = None

        if self.search_engine == 'google':
            init_class_name = 'yuRUbf'
            class_name = init_class_name if class_name is None else class_name

            # Find featured answer
            try:
                featured_ans_tag = soup.find('div', {'class':'ifM9O'})
                featured_ans = featured_ans_tag.find('span', {'class': 'hgKElc'}).text
            except AttributeError:
                pass

            tags = soup.findAll('div', {'class': class_name})
            for tag in tags:
                for a_tag in tag.findAll('a'):
                    href_list.append(a_tag.__getitem__('href'))

        if self.search_engine == 'bing':
            init_class_name = 'b_algo'
            class_name = init_class_name if class_name is None else class_name
            tags = soup.findAll('li', {'class': class_name})
            for tag in tags:
                for a_tag in tag.findAll('a'):
                    href_list.append(a_tag.__getitem__('href'))

        return featured_ans, href_list

    @parse_print
    @exception_catch(debug=debug_mode_global)
    def parse_page(self, robj, parse_page):

        if parse_page == 'stackoverflow' or parse_page == 'stackexchange' \
                or parse_page == 'codegolf_stackexchange' or parse_page == 'math_stackexchange':
            soup = BeautifulSoup(robj.text, 'lxml')

            profile_url = None

            # Find problem title
            tag_title = soup.find('a', {'class': 'question-hyperlink'})
            title = tag_title.text

            # Get number of answers
            num_ans_header = soup.find('h2', {'class': 'mb0'})
            num_ans = int(num_ans_header.get('data-answercount'))
            if num_ans == 0:
                return {'title': title, 'num_ans': num_ans,
                        'solution': 'No answer found!',
                        'profile_url': profile_url, 'type': 'solution'}

            # Find correct ans
            tag_ans = soup.find('div', {'class': 'answer js-answer accepted-answer js-accepted-answer'})
            if tag_ans is None:
                # No correct ans found, find top answer instead
                tag_ans = soup.find('div', {'class': 'answer js-answer'})
            text = tag_ans.find('div', {'class': 's-prose js-post-body'})

            # Find ans avatar
            profile_avt_tag = tag_ans.find('div', {'class': 'gravatar-wrapper-32'})
            profile_url = profile_avt_tag.find('img').__getitem__('src')

            return {'title': title, 'num_ans': num_ans,
                    'solution': text.text, 'profile_url': profile_url,
                    'type': 'solution'}

        if parse_page == 'wiki':
            soup = BeautifulSoup(robj.text, 'lxml')

            # Find definition title
            try:
                title_tag = soup.find('span', {'class': 'mw-page-title-main'})
                title = title_tag.text
            except:
                title_tag = soup.find('h1', {'class': 'firstHeading mw-first-heading'})
                title = title_tag.text

            # Find definition
            full_content_tag = soup.find('div', {'class': 'mw-body-content mw-content-ltr'})
            texts = full_content_tag.findAll('p')
            for text in texts:
                if len(text.text) > 100:
                    return {'title': title, 'def': text.text, 'type': 'definition'}

        if parse_page == 'Accweather':
            soup = BeautifulSoup(robj.text, 'lxml')

            weather_info_tag = soup.find('div', {'class': 'page-content content-module'})
            # Current weather
            forecast_container_tag = weather_info_tag.find('div', {'class': 'forecast-container'})
            cur_weather_svg_url = str('https://www.accuweather.com'+forecast_container_tag.find('svg', {'class': 'weather-icon'}).__getitem__('data-src'))
            cur_weather_svg = self.fetch_html(page='Accweather',url=cur_weather_svg_url).text

            cur_weather_info_tag = weather_info_tag.find('a', {'class': 'cur-con-weather-card card-module content-module lbar-panel'})
            last_update = cur_weather_info_tag.find('p', {'class': 'cur-con-weather-card__subtitle'}).text
            temp = cur_weather_info_tag.find('div', {'class': 'temp'}).text
            real_feel_temp = cur_weather_info_tag.find('div', {'class': 'real-feel'}).text
            weather_description = cur_weather_info_tag.find('span', {'class': 'phrase'}).text

            # Current air quality
            air_quality_tag = weather_info_tag.find('div', {'class': 'air-quality-content'})
            date = air_quality_tag.find('p', {'class': 'date'}).text
            aqi_tag = air_quality_tag.find('div', {'class': 'aq-number-container'})
            aqi_num = aqi_tag.find('div', {'class': 'aq-number'}).text + \
                      aqi_tag.find('div', {'class': 'aq-unit'}).text.lstrip()
            air_quality_des = weather_info_tag.find('p', {'class': 'category-text'}).text
            air_quality_statement = weather_info_tag.find('p', {'class': 'statement'}).text

            # TOMORROW’S WEATHER FORECAST
            tomorrow_weather_tag = weather_info_tag.find('div', {'data-qa': 'tomorrowWeatherCard'})
            tomorrow_date = tomorrow_weather_tag.find('span', {'class': 'sub-title'}).text
            tomorrow_temp = tomorrow_weather_tag.find('div', {'class': 'temp'}).text + \
                   tomorrow_weather_tag.find('span', {'class': 'after-temp'}).text
            tomorrow_real_feel_temp = tomorrow_weather_tag.find('div', {'class': 'real-feel'}).text
            tomorrow_weather_description = tomorrow_weather_tag.find('div', {'class': 'phrase'}).text

            weather_info = [[last_update, temp, real_feel_temp, weather_description],
                            [date, aqi_num, air_quality_des, air_quality_statement],
                            [tomorrow_date, tomorrow_temp, tomorrow_real_feel_temp, tomorrow_weather_description]]

            return {'weather_info': weather_info, 'svg': cur_weather_svg, 'type': 'weather'}

        if parse_page == 'pytorch':

            profile_url = None

            soup = BeautifulSoup(robj.page_source, 'lxml')
            li_tag = soup.find('li',{'class': 'replies'})

            # Find problem title
            title_tag = soup.find('a', {'class':'fancy-title'})
            title = title_tag.text

            # Get number of answers
            try:
                num_ans = int(li_tag.find('span',{'class': 'number'}).text)
            except:
                return {'title': title, 'num_ans': num_ans,
                        'solution': 'No answer found!',
                        'profile_url': profile_url, 'type': 'solution'}

            articles = soup.findAll('article')
            for article in articles:
                if article.find('span', {'class': 'accepted-text'}) is not None:
                    profile_url = 'https://discuss.pytorch.org'+article.find('img', {'class': 'avatar'}).__getitem__('src')
                    text = article.find('div', {'class': 'cooked'})
                    return {'title': title, 'num_ans': num_ans,
                        'solution': text.text, 'profile_url': profile_url,
                        'type': 'solution'}
                else:
                    continue

            profile_url = 'https://discuss.pytorch.org'+articles[1].find('img', {'class': 'avatar'}).__getitem__('src')
            text = articles[1].find('div', {'class': 'cooked'})
            return {'title': title, 'num_ans': num_ans,
                    'solution': text.text, 'profile_url': profile_url,
                    'type': 'solution'}

    def search(self, query):
        repobj = self.fetch_search_html(query)
        featured_ans, links = self.parse_url(repobj)
        if self.debug_mode:
            print('--- Retrieved links to crawl ---')
            for link in links:
                print(link)
        if featured_ans is not None:
            print(f'\nFeatured answer: {featured_ans}')

        for idx, link in enumerate(links):
            if 'https://stackoverflow.com/' in link:
                print(f"\n\n----- |Result| {idx} -----")
                print(f"Solution in {link}")
                repobj = self.fetch_html(page='stackoverflow',url=link)
                self.parse_page(repobj, parse_page='stackoverflow')

            if 'https://academia.stackexchange.com/' in link:
                print(f"\n\n----- |Result| {idx} -----")
                print(f"Solution in {link}")
                repobj = self.fetch_html(page='stackexchange',url=link)
                self.parse_page(repobj, parse_page='stackexchange')

            if 'https://codegolf.stackexchange.com/' in link:
                print(f"\n\n----- |Result| {idx} -----")
                print(f"Solution in {link}")
                repobj = self.fetch_html(page='codegolf_stackexchange',url=link)
                self.parse_page(repobj, parse_page='codegolf_stackexchange')

            if 'https://math.stackexchange.com/' in link:
                print(f"\n\n----- |Result| {idx} -----")
                print(f"Solution in {link}")
                repobj = self.fetch_html(page='math_stackexchange',url=link)
                self.parse_page(repobj, parse_page='math_stackexchange')

            if 'https://discuss.pytorch.org/' in link:
                print(f"\n\n----- |Result| {idx} -----")
                print(f"Solution in {link}")
                repobj = self.fetch_html(page='pytorch',url=link)
                self.parse_page(repobj, parse_page='pytorch')

            if 'https://en.wikipedia.org/' in link:
                print(f"\n\n----- |Result| {idx} -----")
                print(f"Definition in {link}")
                repobj = self.fetch_html(page='wiki',url=link)
                self.parse_page(repobj, parse_page='wiki')

            if 'https://www.accuweather.com/' in link and 'hourly' \
                and 'daily' and 'translate' not in link:
                print(f"\n\n----- |Result| {idx} -----")
                print(f"Weather info {link}")
                repobj = self.fetch_html(page='Accweather',url=link)
                self.parse_page(repobj, parse_page='Accweather')




