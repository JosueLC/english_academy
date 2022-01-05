# Scrapper to www.eslfast.com
# Links to courses with xPath: //section[@class='beginners']//a/@href

#Dependencies
import json
import os
import requests
import lxml.html as html
from urllib.parse import urljoin
import nltk
nltk.download('punkt')

import xpaths

URL_HOME = 'https://www.eslfast.com/'
ASSETS_PATH = os.path.join(os.path.dirname(__file__),'../../assets/')

visited_links = list()
text_class_compose = dict()

def get_parsed_html(url:str,xpath:str) -> list:
    try:
        response = requests.get(url)
        if response.status_code == 200:
            parsed = html.fromstring(response.content)
            return parsed.xpath(xpath)
        else:
            raise ValueError('Error: {}'.format(response.status_code))
    except Exception as e:
        print(e)
        return list()

def parse_home():
    courses = get_parsed_html(URL_HOME,xpaths.XPATH_LINK_TO_COURSES)
    for course in [courses[0]]:
        #get link_url from link
        link_url = course.attrib['href']
        if link_url not in visited_links:
            if len(course) == 2:
                course_name = course[1][0].text_content()
            else:
                course_name = course[0][1].text_content()
            visited_links.append(link_url)
            parse_course(link_url,course_name)
            update_stats()

def parse_course(url:str,course_name:str):
    classes = get_parsed_html(url,xpaths.XPATH_LINK_TO_CLASSES)
    for link in classes:
        #Check if the link finishes with index(number).htm using regex.
        #if regex is ok, call again parse_course with the joined url to the link
        #else print the link joined with the url
        full_url = urljoin(url, link.attrib['href'])
        if full_url not in visited_links:
            classes.append(full_url)
            visited_links.append(full_url)
            if not parse_class(full_url):
                parse_course(full_url,course_name)
    #classes[course_name] = classes

def parse_class(url) -> bool:
    filename = '-'.join(url.split('/')[-2:]).split('.')[0]
    audios = get_parsed_html(url,xpaths.XPATH_LINK_TO_AUDIOS)
    if len(audios) > 0:
        if len(audios) == 1:
            text_filepath = build_path(['texts'],filename,'txt')
            if not os.path.isfile(text_filepath):
                download_audio(urljoin(url,audios[0]),filename)
                save_to_file(format_texts(url,xpaths.XPATH_LINK_TO_TEXTS,filename),text_filepath)
        else:
            for audio in enumerate(audios):
                text_filename = filename + '-' + audio
                text_filepath = build_path(['texts'],text_filename,'txt')
                if not os.path.isfile(text_filepath):
                    download_audio(urljoin(url,audios[audio]),text_filename)
                    save_to_file(format_texts(url,xpaths.XPATH_LINK_TO_TEXTS,text_filename),text_filepath)
        return True
    else:
        return False

def download_audio(url,text_filename):
    filepath = build_path(['audios'],text_filename,'mp3')
    if not os.path.isfile(filepath):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                with open(filepath, 'wb') as f:
                    f.write(response.content)
            else:
                raise ValueError('Error download {}: {}'.format(url,response.status_code))
        except Exception as e:
            print(e)

def format_texts(url:str,xpaths:list, filename) -> list:
    content = list()
    for xpath in xpaths:
        content = get_parsed_html(url,xpath)
        if len(content) > 0:
            class_content = [s for s in content if s.split()]
            class_content = [' '.join(s.split()) for s in class_content]
            class_content = [x for t in [nltk.sent_tokenize(s) for s in class_content] for x in t]
            #Save statistics
            flatten = ' '.join(class_content).split()
            set_words = set(flatten)
            text_class_compose[filename] = {
                'words': len(flatten),
                'unique_words': len(set_words),
                'sentences': len(class_content),
                'density': len(flatten)/len(set_words)
            }
            break
    return class_content

def save_to_file(l:list, filepath:str):
    with open(filepath, 'w',encoding='utf-8') as f:
        for item in l:
            f.write(item + '\n')

def build_path(partials:list, filename:str, extension:str) -> str:
    return os.path.join(ASSETS_PATH,*partials,filename + '.' + extension)

def update_stats():
    #Update text_class_compose.json if not exists or if the file is empty
    #Read text_class_compose.json and update it with the new data
    #Save the new data to text_class_compose.json
    file = build_path(['texts'],'text_class_compose','json')
    if os.path.isfile(file) and os.stat(file).st_size > 0:
        with open(file, 'r') as f:
            data = json.load(f)
    else:
        data = dict()
    for key, value in text_class_compose.items():
        data[key] = value
    with open(file, 'w') as f:
        json.dump(data, f)

def run():
    parse_home()

if __name__ == '__main__':
    print('Starting scrapper...')
    # print(os.path.dirname(__file__))
    # print(os.path.join(os.path.dirname(__file__),'../../assets/texts'))
    run()