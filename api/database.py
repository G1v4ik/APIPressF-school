from sqlalchemy.ext.asyncio import (
    create_async_engine, async_sessionmaker
)

from .models import BaseModel

from .config import get_settings


settings = get_settings()


engine = create_async_engine(
    settings.DATABASE
)

create_session = async_sessionmaker(
    engine,
    expire_on_commit=False
)


async def create_tables():
    async with engine.begin() as conn:
       await conn.run_sync(BaseModel.metadata.create_all)


async def delete_tables():
    """DANGER"""
    async with engine.begin() as conn:
       await conn.run_sync(BaseModel.metadata.drop_all)