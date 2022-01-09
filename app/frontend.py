from typing import List
from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastapi.exceptions import HTTPException
from starlette.responses import StreamingResponse
from app import main

def get_prefix_to_app() -> List[str]:
    paths = [route.__getattribute__('path').replace("/","") for route in main.app.routes]
    # print("="*30)
    # print(paths)
    # print("="*30)
    return paths

def is_path_from_prefix(path:str) -> bool:
    path = path.replace("/","")
    #print(f'path to check: {path}')
    for prefix in get_prefix_to_app():
        #print(f'prefix to check: {prefix}')
        if path.startswith(prefix):
            return True
    return False

router = APIRouter()

@router.get("/{path:path}")
async def get_frontend(path: str):
    # print("-"*40)
    valid = not(is_path_from_prefix(path))
    print(f'Frontend required: {path} - valid: {str(valid)}')
    if valid:
        if path == "":
            path = "index.html"
        # check if path exists, if not, return index.html
        if path.endswith(".js"):
            content_type = "application/javascript"
        elif path.endswith(".css"):
            content_type = "text/css"
        elif path.endswith(".mp3"):
            content_type = "audio/mpeg"
            path = "./app/core/assets/audios/" + path.split("/")[-1]
            return StreamingResponse(
                content=open(path, "rb")
            )
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