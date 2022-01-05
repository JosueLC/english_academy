import re

XPATH_LINK_TO_COURSES = '//section[@class="beginners"]//a'
XPATH_LINK_TO_CLASSES = '//section[starts-with(@class,"beginners")]//a'
XPATH_LINK_TO_AUDIOS = '//audio/@src'
XPATH_LINK_TO_TEXTS1 = '//p[@class="timed"]/text()'
XPATH_LINK_TO_TEXTS2 = '//p[@class="timed"]/span/text()'
XPATH_LINK_TO_TEXTS3 = '//p[@class="read_text"]/font/text()'
XPATH_LINK_TO_TEXTS = [
    XPATH_LINK_TO_TEXTS1,
    XPATH_LINK_TO_TEXTS2,
    XPATH_LINK_TO_TEXTS3,
    ]
INDEX_REGEX = re.compile(r'index\d+\.htm')