#Main project file

#Import packages
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.api.v1.api import api_router
from app.frontend import router as front_route



app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f'{settings.API_V1_STR}/openapi.json'
)

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials = True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

routers = {
    settings.API_V1_STR:api_router,
    '':front_route,
}

for route, router in routers.items():
    app.include_router(router,prefix=route)