# APIRouter for api version 1

from fastapi import APIRouter
from fastapi.staticfiles import StaticFiles
from .endpoints import *

import os

api_router = APIRouter()

#Mount assets folder as static directory

path = os.path.join(os.path.dirname(__file__), '../../core/assets')

api_router.mount("/assets", StaticFiles(directory=path), name="assets")