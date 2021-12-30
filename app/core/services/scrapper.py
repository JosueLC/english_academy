# Scrapper to www.eslfast.com
# Links to courses with xPath: //section[@class='beginners']//a/@href

#Dependencies
import requests
import lxml.html as html
from urllib.parse import urljoin
import re

URL_HOME = 'https://www.eslfast.com/'

XPATH_LINK_TO_COURSE = '//section[@class="beginners"]//a/@href'
XPATH_LINK_TO_CLASSES = '//section[starts-with(@class,"beginners")]//a/@href'
XPATH_LINK_TO_AUDIOS = '//audio/@src'
XPATH_LINK_TO_TEXTS = '//p[@class="timed"]/text()'

INDEX_REGEX = re.compile(r'index\d+\.htm')
NEWLINE_CHARS = ["\n","\n\n"]

list_of_links = []
links_to_audios = []
texts_to_classes = {}

def parse_home():
    try:
        response = requests.get(URL_HOME)
        if response.status_code == 200:
            home = response.content.decode('utf-8')
            parsed = html.fromstring(home)
            links = parsed.xpath(XPATH_LINK_TO_COURSE)
            for link in links:
                if link not in list_of_links:
                    list_of_links.append(link)
                    parse_course(link)
        else:
            raise ValueError('Error: {}'.format(response.status_code))
    except ValueError as e:
        print(e)

def parse_course(url):
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
                if full_url not in list_of_links:
                    list_of_links.append(full_url)
                    if INDEX_REGEX.search(link):
                        parse_course(full_url)
                    else:
                        parse_class(full_url)
        else:
            raise ValueError('Error: {}'.format(response.status_code))
    except ValueError as e:
        print(e)

def parse_class(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            course = response.content
            parsed = html.fromstring(course)
            links = parsed.xpath(XPATH_LINK_TO_AUDIOS)
            for link in links:
                full_url = urljoin(url, link)
                if full_url not in list_of_links:
                    list_of_links.append(full_url)
                    links_to_audios.append(full_url)
                    texts_to_classes[full_url] = [p for p in parsed.xpath(XPATH_LINK_TO_TEXTS) if p not in NEWLINE_CHARS]
        else:
            raise ValueError('Error: {}'.format(response.status_code))
    except ValueError as e:
        print(e)