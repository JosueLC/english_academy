from typing import List
from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastapi.exceptions import HTTPException
from app import main

def get_prefix_to_app() -> List[str]:
    paths = [route.__getattribute__('path').replace("/","") for route in main.app.routes]
    # print("="*30)
    # print(paths)
    # print("="*30)
    return paths

def is_path_from_prefix(path:str) -> bool:
    # print(f'path to check: {path}')
    path = path.replace("/","")
    for prefix in get_prefix_to_app():
        if path.startswith(prefix):
            return True
    return False

router = APIRouter()

@router.get("/{path:path}")
async def get_frontend(path: str):
    # print("-"*40)
    valid = not(is_path_from_prefix(path))
    # print(f'Frontend required: {path} - valid: {str(valid)}')
    if valid:
        if path == "":
            path = "index.html"
        # check if path exists, if not, return index.html
        if path.endswith(".js"):
            content_type = "application/javascript"
        elif path.endswith(".css"):
            content_type = "text/css"
        else:
            content_type = "text/html"
            path = "index.html"
        # print(f'Frontend: {path}')
        return HTMLResponse(
            status_code=200,
            content=open(f"./app/view/{path}", "rb").read(),
            media_type=content_type
        )
    raise HTTPException(status_code=404, detail=f'Path {path} not found.')