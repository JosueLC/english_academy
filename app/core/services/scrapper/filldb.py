import json
import os
import sys
import requests

ASSETS_PATH = os.path.join(os.path.dirname(__file__),'../../assets/')

urlbase = 'http://localhost:8000/api/v1'

def post_data(url,data):
    headers = {
        "Content-Type": "application/json; charset=utf-8"
    }
    d = json.dumps(data)
    r = requests.post(url=url,data=d,headers=headers)
    if r.status_code != 200:
        print(r)
    return r

def post_course(name:str, level: str) -> str:
    course = {
        'name':name,
        'description':name.replace('_',' '),
        'level':level
    }
    req = post_data(
        url=urlbase+'/course/',
        data=course
    )
    if req.status_code == 200:
        obj = req.json()
        return obj['id']
    return ''



def post_class(name: str, course_id:str) -> str:
    classs = {
        'name':name,
        'description':name.replace('_',' '),
        'course_id':course_id,
        'audio':''.join(['/audio/',name,'.mp3'])
    }
    req = post_data(urlbase+'/class/',classs)
    if req.status_code == 200:
        obj = req.json()
        return obj['id']
    return ''

def post_text(corpus: list[str], class_id: str) -> int:
    db_corpus = [
        {'line_number':i,
         'text': corpus[i],
         'class_id': class_id}
            for i in range(len(corpus))
    ]
    req = post_data(urlbase+'/texts/corpus',db_corpus)
    if req.status_code == 200:
        obj = json.loads(req.text)['count']
        return obj
    print(req.text)
    return 0

def run():
    data = json.load(open(ASSETS_PATH+'texts/text_class_analysis.json','r'))
    course_id_dict = {}
    size_data = len(data)
    progress=0
    texts_count = 0
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
                r = post_text(lines,class_id)
                texts_count += r
            except Exception as e:
                print('Text post error: {}'.format(e))
        progress += 1
        if progress %50 == 0:
            sys.stdout.write(f'\rPublished {progress} class of {size_data} with {texts_count} texts.')

if __name__ == '__main__':
    print('Filling database...')
    run()
    print('Finished.')