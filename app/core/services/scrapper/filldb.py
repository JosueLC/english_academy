import json
import os
import sys
from nltk.util import pr
import requests

ASSETS_PATH = os.path.join(os.path.dirname(__file__),'../../assets/')

urlbase = 'http://localhost:8000/api/v1'

def post_course(name:str, level: str) -> str:
    course = {
        'name':name,
        'description':'',
        'level':level
    }
    req = requests.post(
        url=urlbase+'/course',
        data=course,
        allow_redirects=True
    )
    if req.status_code == 200:
        obj = req.json()
        return obj['id']
    return ''



def post_class(name: str, course_id:str) -> str:
    classs = {
        'name':name,
        'description':'',
        'course_id':course_id,
        'audio':''.join('/audio/',name,'.mp3')
    }
    req = requests.post(urlbase+'/class',classs)
    if req.status_code == 200:
        obj = req.json()
        return obj['id']
    return ''

def post_text(number:int, text: str, class_id: str):
    text = {
        'number':number,
        'text': text,
        'class_id': class_id
    }
    req = requests.post(urlbase+'/texts',text)
    if req.status_code == 200:
        obj = req.json()
        return obj['id']
    return ''

def run():
    data = json.load(open(ASSETS_PATH+'texts/text_class_analysis.json','r'))
    course_id_dict = {}
    size_data = len(data)
    print(size_data)
    progress=0
    for clas in data.values():
        course_name = '_'.join([clas['course'],clas['level']])
        if not course_name in course_id_dict:
            level = int(clas['level'][-1])
            course_id = post_course(course_name, level)
            if len(course_id)> 0:
                course_id_dict[course_name] = course_id
            else:
                print(f'Error - {course_name}')
        class_id = post_class(
            name=clas['new_name'],
            course_id=course_id_dict[course_name]
        )
        if len(class_id)> 0:
            try:
                texts = open(''.join([ASSETS_PATH,'texts/',clas['new_name'],'.txt']),'r')
                lines = texts.readlines()
                for i in range(len(lines)):
                    post_text(i,lines[i],class_id)
            except Exception as e:
                print('Error: {}'.format(e))
        progress +=1
        if progress % 100 == 0:
            sys.stdout.write(f'\rPublished {progress} class of {size_data}')

if __name__ == '__main__':
    print('Filling database...')
    run()
    print('Finished.')