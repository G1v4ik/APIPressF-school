from contextlib import asynccontextmanager
from fastapi import FastAPI
# from api.database import 
import uvicorn
from dotenv import load_dotenv
from os import getenv

from api import routers
from api.config import get_settings
from api.database import create_tables

load_dotenv()

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    yield


api = FastAPI(lifespan=lifespan)

api.include_router(
    routers.router_driving_school
)

api.include_router(
    routers.router_academy
)


if __name__ == '__main__':
    settings = get_settings()
    uvicorn.run(
        "main:api", 
        host=settings.HOST, 
        port=settings.PORT,
        reload=settings.RELOAD,
    )