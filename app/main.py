from services.scrapper import parse_home, parse_course, parse_class
from services.scrapper import list_of_links, links_to_audios, texts_to_classes

def run():
    parse_home()

if __name__ == '__main__':
    run()
    print('Finished.')