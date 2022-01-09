# APIRouter for api version 1

from fastapi import APIRouter
from .endpoints import *

import os

api_router = APIRouter()