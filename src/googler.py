import requests
import time
import sys
sys.path.insert(0,r'./') #Add root directory here
from typing import List
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from utils.utils import parse_print


class Googler:
    def __init__(self, search_engine='google'):
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
            'cookie': 'S=billing-ui-v3=pxApETqldBkuFJB5dvhfmnmEjQSygT1o:billing-ui-v3-efe=pxApETqldBkuFJB5dvhfmnmEjQSygT1o; SEARCH_SAMESITE=CgQIwJcB; OTZ=6981436_28_28__28_; SID=VgjOxeftABrio97kzbcnoouuctRKXm42s2WcxD0dgkg0gr2LJ7eXUaSmh8ZbkHMvX4s9Vg.; __Secure-1PSID=VgjOxeftABrio97kzbcnoouuctRKXm42s2WcxD0dgkg0gr2LUwqK3CHVL3egyZNnrP6TiQ.; __Secure-3PSID=VgjOxeftABrio97kzbcnoouuctRKXm42s2WcxD0dgkg0gr2LMHt5G0EZPx0c4QKSJqNlfQ.; HSID=APHGfeuKJp0vfdslA; SSID=A8x9T6Kvlh2Iwwvpg; APISID=q0WoEerdv-ERXRvX/ANixn7OUJ-2Net5JI; SAPISID=lH7Zm_E6465KE-Ax/Atj-pfzgzQOojPqYL; __Secure-1PAPISID=lH7Zm_E6465KE-Ax/Atj-pfzgzQOojPqYL; __Secure-3PAPISID=lH7Zm_E6465KE-Ax/Atj-pfzgzQOojPqYL; NID=511=T5To3UV10PHOOkhiboL4bZa5OE9UwtprBpjIU1xJYlltnBgpfXL1c39McOHpnjrnYk6dnkioYSzDpkClrkVl_I65ghE4RsqMPMrYB-DtKXdk-VQ0iKetRRrlbZHBjA_cbWyyTg0Lrz4edHExkpMtxpxTAYiafhU0qjJ_NVIEtbIMoj5QgI0ykLCKambSv7d7ToQZOHZikv3f0Uw7yDQnkD4kxeOHkZFmRvgH4ma6WOC5oGsJgQwYFa2rdMiPVtWP2lrBTGlEa2VuNhT9a3OTPc7OX432LFv97ZDU66ifNdFBxUjAHgG5ysPEi7UjbLtr2U2E-nKkatqEgjwfBz2B_a0BznRXZOSWMUM9MkUwHJ-ZrGjxJ68; AEC=AUEFqZf8BkHA7aR4qczY9LXa42w1lH01gXPAbzuh3R0tfxB8PEUFeJ3tIXg; DV=k4fzKS9NhUtRoL-BnfVaSItCx6s-eBgaJsH45ZPKQwEAAFBxZ8UCkzF_XwEAAASIm0L1K13fWQAAAGnw0XD9ZnENFwAAAA; 1P_JAR=2023-04-15-07; SIDCC=AP8dLtyAhlXcSw-RVD-zFNQJJ93z-UDKfnXiWVM19KyCzTAVZOpOKnaGftS7xO2hQln0TBFbhYQ; __Secure-1PSIDCC=AP8dLtyPp3rLaCwB6nkJgy0nd3b-5mM8TS41I2jJPC4_Jz8eXGujFH-H4J93k4JxxwI2_4OsrXc; __Secure-3PSIDCC=AP8dLtxksuaTIufONI1n4YIV-wm2YW6rSn3X0aJwbpPB6xC9ohQ_O8r79Oy9GsS07m_2QM485O5U',
            'pragma': 'no-cache',
            'referer': 'https://www.google.com/',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
        }

        self.search_engine = search_engine

    def fetch_html(self, page=None, url=None):

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

        if page == 'pytorch':
            options = Options()
            options.add_argument("--headless")
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
            browser = webdriver.Chrome(options=options)
            browser.get(url)

            return browser

        response = requests.get(url=url, params=params, headers=headers)

        return response

    def fetch_search_html(self, query):
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

        response = requests.get(url=url, params=params, headers=headers)

        return response

    def parse_url(self, robj, class_name=None) -> List[str]:

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
    def parse_page(self, robj, parse_page):

        if parse_page == 'stackoverflow' or parse_page == 'stackexchange' \
                or parse_page == 'codegolf_stackexchange' or parse_page == 'math_stackexchange':
            soup = BeautifulSoup(robj.text, 'lxml')

            # Find problem title
            tag_title = soup.find('a', {'class': 'question-hyperlink'})
            title = tag_title.text

            # Get number of answers
            num_ans_header = soup.find('h2', {'class': 'mb0'})
            num_ans = int(num_ans_header.get('data-answercount'))
            if num_ans == 0:
                return title, num_ans, 'No answer found!'

            # Find correct ans
            tag_ans = soup.find('div', {'class': 'answer js-answer accepted-answer js-accepted-answer'})
            if tag_ans is None:
                # No correct ans found, find top answer instead
                tag_ans = soup.find('div', {'class': 'answer js-answer'})
            text = tag_ans.find('div', {'class': 's-prose js-post-body'})

            return title, num_ans, text.text

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
                    return title, text.text

        if parse_page == 'pytorch':
            soup = BeautifulSoup(robj.page_source, 'lxml')
            li_tag = soup.find('li',{'class': 'replies'})

            # Find problem title
            title_tag = soup.find('a', {'class':'fancy-title'})
            title = title_tag.text

            # Get number of answers
            try:
                num_ans = int(li_tag.find('span',{'class': 'number'}).text)
            except:
                return title, num_ans, 'No answer found!'

            articles = soup.findAll('article')
            for article in articles:
                if article.find('span', {'class': 'accepted-text'}) is not None:
                    text = article.find('div', {'class': 'cooked'})
                    return title, num_ans, text.text
                else:
                    continue

            text = articles[1].find('div', {'class': 'cooked'})
            return title, num_ans, text.text

    def search(self, query):
        repobj = self.fetch_search_html(query)
        featured_ans, links = self.parse_url(repobj)
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



