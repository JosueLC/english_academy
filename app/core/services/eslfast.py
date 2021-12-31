# Scrapper to www.eslfast.com
# Links to courses with xPath: //section[@class='beginners']//a/@href

#Dependencies
import re
import requests
import asyncio
import lxml.html as html
from urllib.parse import urljoin
from typing import List, Tuple
from pydantic import AnyHttpUrl

# Scrapping services to ESLFast website

#Constants
URL_HOME = 'https://www.eslfast.com/'
XPATH_LINK_TO_COURSE = '//section[@class="beginners"]//a/@href'
XPATH_LINK_TO_CLASSES = '//section[starts-with(@class,"beginners")]//a/@href'
XPATH_LINK_TO_AUDIOS = '//audio/@src'
XPATH_LINK_TO_TEXTS = '//p[@class="timed"]/text()'
INDEX_REGEX = re.compile(r'index\d+\.htm')
NEWLINE_CHARS = ["\n","\n\n"]

def parse_home() ->List[AnyHttpUrl]:
    courses_links = list();
    try:
        response = requests.get(URL_HOME)
        if response.status_code == 200:
            home = response.content.decode('utf-8')
            parsed = html.fromstring(home)
            links = parsed.xpath(XPATH_LINK_TO_COURSE)
            for link in links:
                if link not in courses_links:
                    courses_links.append(link)
        else:
            raise ValueError('Error: {}'.format(response.status_code))
    except ValueError as e:
        print(e)
    finally:
        return courses_links

def parse_course(url) -> List[AnyHttpUrl]:
    classes_links = list();
    try:
        response = requests.get(url)
        if response.status_code == 200:
            course = response.content
            parsed = html.fromstring(course)
            links = parsed.xpath(XPATH_LINK_TO_CLASSES)
            for link in links:
                #Check if the link finishes with index(number).htm using regex.
                #if regex is ok, call again parse_course with the joined url to the link
                #else print the link joined with the url
                full_url = urljoin(url, link)
                if INDEX_REGEX.search(link):
                    additional_class = asyncio.run(parse_course(full_url))
                    classes_links.append(*additional_class)
                elif full_url not in classes_links:
                    classes_links.append(full_url)
        else:
            raise ValueError('Error: {}'.format(response.status_code))
    except ValueError as e:
        print(e)
    finally:
        return classes_links

def parse_class(url) -> Tuple[AnyHttpUrl,List[str]]:
    try:
        response = requests.get(url)
        if response.status_code == 200:
            course = response.content
            parsed = html.fromstring(course)
            links = parsed.xpath(XPATH_LINK_TO_AUDIOS)
            full_url = urljoin(url, links[0])
            texts_class = [p for p in parsed.xpath(XPATH_LINK_TO_TEXTS) if p not in NEWLINE_CHARS]
            return full_url,texts_class
        else:
            raise ValueError('Error: {}'.format(response.status_code))
    except ValueError as e:
        print(e)
        return "",[]
