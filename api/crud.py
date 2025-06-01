from fastapi import HTTPException
from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from .database import create_session

from . import models

from . import schames


async def commit_to_db(session: AsyncSession, db):
    session.add(db)
    await session.flush()
    await session.commit()
    return db


async def update_to_db(
        session: AsyncSession, 
        query, 
        new_data: schames.DS_response_message
    ):
    update_to = await session.execute(query)
    is_new = update_to.scalars().one()
    is_new.is_new = new_data.is_new
    await session.commit()
    return is_new



async def get_data_by_query(session: AsyncSession, query):
    result = await session.execute(query)
    return result.scalar()

async def get_all_data_by_query(session: AsyncSession, query):
    result = await session.execute(query)
    return result.scalars().all()


async def send_support_message(
        data: schames.DS_support_new_message
) -> schames.DS_support_new_message:
    
    async with create_session() as session:
        db = models.SupportMessages(
            telegram_id = data.telegram_id,
            username = data.username,
            message = data.message,
            is_new = data.is_new,
            create_at = data.create_at
        )

        return await commit_to_db(session, db)


async def list_support_message(
        
)-> list[models.SupportMessages]:
    async with create_session() as session:
        query = select(
            models.SupportMessages
        ).where(
            models.SupportMessages.is_new == True  # noqa: E712
        )
        return await get_all_data_by_query(session, query)


async def response_support_message(
        new_data: schames.DS_response_message
) -> models.SupportMessages:
    async with create_session() as session:
            
        query = select(
            models.SupportMessages
        ).filter(
            models.SupportMessages
            .id_message == new_data.id_message
        )
        
        return await update_to_db(session, query, new_data)
    
