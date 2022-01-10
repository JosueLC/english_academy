# APIRouter for api version 1

from fastapi import APIRouter
from .endpoints import endpoints

import os

api_router = APIRouter()

for endpoint in endpoints:
    api_router.include_router(endpoint)