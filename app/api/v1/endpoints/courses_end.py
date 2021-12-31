#Endpoint to get list of course inside the website
from fastapi import APIRouter, Depends, HTTPException
from app.core.config import settings
from app.core.services.eslfast import parse_home

courses_router = APIRouter(
    prefix='/courses'
)

@courses_router.get('/')
def get_courses():
    courses = parse_home()
    return courses