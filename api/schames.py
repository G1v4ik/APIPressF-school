from pydantic import (
    BaseModel, 
    Field)

from datetime import datetime


class DS_support_new_message(BaseModel):
    username: str
    message: str
    is_new: bool = Field(default=True)
    create_at: datetime = Field(default=datetime.now())


class DS_response_message(BaseModel):
    username: str
    is_new: bool = False