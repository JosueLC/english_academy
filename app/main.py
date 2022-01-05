#Main project file

#Import packages
# from fastapi import FastAPI
# from starlette.middleware.cors import CORSMiddleware

# from app.core.config import settings
# from app.core.data.database import Base, engine
# from app.api.v1.api import api_router
# from app.frontend import router as front_route

import os
from core.services import eslfast
import requests

# Base.metadata.create_all(bind=engine)

# app = FastAPI(
#     title=settings.PROJECT_NAME, openapi_url=f'{settings.API_V1_STR}/openapi.json'
# )

# # Set all CORS enabled origins
# if settings.BACKEND_CORS_ORIGINS:
#     app.add_middleware(
#         CORSMiddleware,
#         allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
#         allow_credentials = True,
#         allow_methods=["*"],
#         allow_headers=["*"],
#     )

# routers = {
#     settings.API_V1_STR:api_router,
#     '':front_route,
# }

# for route, router in routers.items():
#     app.include_router(router,prefix=route)

def download_file(url,path):
    filename = url.split('/')[-1]
    r = requests.get(url, allow_redirects=True)
    open(path + filename, 'wb').write(r.content)

def save_string_as_file(string,path):
    with open(path, 'w') as f:
        f.write(string)

def get_data_from_eslfast():
    print("Getting data from ESLFast...")
    #get path to project directory with os
    path = os.path.dirname(os.path.abspath(__file__))
    path_files = path + '/core/assets/'
    for course in eslfast.parse_home():
        for class_ in eslfast.parse_course(course):
            data = eslfast.parse_class(class_)
            download_file(data[0],path_files.format('audios/'))
            text = '{text:' + ','.join(data[1]) + '}'
            save_string_as_file(text,path_files.format('texts'))
    print("Data saved!")

if __name__ == '__main__':
    get_data_from_eslfast()