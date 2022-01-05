# APIRouter for api version 1

from fastapi import APIRouter
from .endpoints import *

api_router = APIRouter()

api_router.include_router(course, prefix="/courses", tags=["courses"])