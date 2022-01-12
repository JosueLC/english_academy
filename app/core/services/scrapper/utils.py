# Scrapper to www.eslfast.com
# Links to courses with xPath: //section[@class='beginners']//a/@href

#Dependencies
import json
import os
import string
import sys
import requests
import lxml.html as html
from urllib.parse import urljoin
import nltk
from string import punctuation
import xpaths
nltk.download('punkt')


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
    print('Starting scrapper...')
    courses = get_parsed_html(URL_HOME,xpaths.XPATH_LINK_TO_COURSES)
    for course in courses:
        #get link_url from link
        link_url = course.attrib['href']
        if link_url not in visited_links:
            if len(course) == 2:
                course_name = course[1][0].text_content()
            else:
                course_name = course[0][1].text_content()
            sys.stdout.write('\n>> Parsing course: {}\n'.format(course_name))
            visited_links.append(link_url)
            parse_course(link_url,course_name)
            update_stats()

def parse_course(url:str,course_name:str):
    classes = get_parsed_html(url,xpaths.XPATH_LINK_TO_CLASSES)
    classes = sorted(classes,key=lambda x: x.attrib['href'])
    progress = 1
    for link in classes:
        #Check if the link finishes with index(number).htm using regex.
        #if regex is ok, call again parse_course with the joined url to the link
        #else print the link joined with the url
        try:
            full_url = urljoin(url, link.attrib['href'])
            if full_url not in visited_links:
                visited_links.append(full_url)
                if not parse_class(full_url):
                    #print('recursive: {}'.format(full_url))
                    parse_course(full_url,course_name)
                sys.stdout.write('\rScrapped {} links of {}.'.format(progress,len(classes)))
                progress +=1
        except Exception as e:
            print(e.with_traceback(sys.exc_info()[2]))
            print('link: {}'.format(link))
            print(type(link))

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
    class_content = list()
    for xpath in xpaths:
        content = get_parsed_html(url,xpath)
        if len(content) > 0:
            class_content = [s for s in content if s.split()]
            class_content = [' '.join(s.split()) for s in class_content]
            class_content = [x for t in [nltk.sent_tokenize(s) for s in class_content] for x in t]
            if any(s[-1] not in punctuation for s in class_content):
                joined_content = ' '.join(class_content)
                class_content = nltk.sent_tokenize(joined_content)
            if len(class_content) > 0:
                #Save statistics
                tokens = [w for w in nltk.word_tokenize(' '.join(class_content)) if w not in string.punctuation]
                set_words = set(tokens)
                text_class_compose[filename] = {
                    'words': len(tokens),
                    'unique_words': len(set_words),
                    'sentences': len(class_content),
                    'richness': len(set_words)/len(tokens)
                }
                break
            else:
                print('No content found for {} in {}'.format(xpath,url))
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
        json.dump(data, f, indent=4, sort_keys=True)

def run():
    parse_home()

def rename_files():
    print('Renaming texts files...')
    #Set the work directory to the texts folder
    os.chdir(os.path.join(ASSETS_PATH,'texts'))
    #Get current and new filenames from json file
    data = json.load(open(build_path(['texts'],'text_class_analysis','json'),encoding='utf-8'))
    #from data.items() get the current filename (key) and change it to the new filename (value['new_name'])
    for key, value in data.items():
        cn = key + '.txt'
        nn = value['new_name'] + '.txt'
        os.rename(cn,nn)

    print('Renaming audios files...')
    #Repeat the process for audios
    os.chdir(os.path.join(ASSETS_PATH,'audios'))
    data = json.load(open(build_path(['texts'],'text_class_analysis','json'),encoding='utf-8'))
    for key, value in data.items():
        cn = key + '.mp3'
        nn = value['new_name'] + '.mp3'
        os.rename(cn,nn)

if __name__ == '__main__':
    #run()
    rename_files()
    #pass