from sqlalchemy import (
    Text,
    String,  
    MetaData, 
    Boolean,
    DateTime,
    BigInteger)
from sqlalchemy.orm import (
    Mapped, 
    mapped_column, 
    DeclarativeBase)
from sqlalchemy.ext.asyncio import AsyncAttrs

from datetime import datetime


class BaseModel(AsyncAttrs, DeclarativeBase):
    metadata = MetaData(schema='api_support_pressf')


class SupportMessages(BaseModel):
    __tablename__ = 'supportmessages'
    id_message: Mapped[int] = mapped_column(
        primary_key=True, 
        autoincrement=True
    )
    telegram_id: Mapped[int] = mapped_column(BigInteger)
    username: Mapped[str] = mapped_column(String)
    message: Mapped[str] = mapped_column(Text)
    is_new: Mapped[bool] = mapped_column(Boolean, onupdate=True)
    create_at: Mapped[datetime] = mapped_column(DateTime)