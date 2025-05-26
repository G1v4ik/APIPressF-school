from pydantic import (
    BaseModel, 
    Field, 
    field_validator,
    EmailStr)
from typing import Optional, Annotated
import re
from datetime import time

_surname = Annotated[str, Field(max_length=30)]
# _contact_phone = Annotated[str, Field(max_length=12)]

class DS_TG_ID_Schames(BaseModel):
    telegram_id: int

class DS_UserSchames(DS_TG_ID_Schames):
    name: str = Field(max_length=30)
    surname: Optional[_surname] = None
    contact_phone: Optional[str] = None
    user_type: Optional[str] = None


    @field_validator('contact_phone')
    def validator_phone_number(cls, value):
        if not re.match(r'^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$', value):
            raise ValueError('Номер телефона должен начинаться с "+" и содержать 11 цифр')
        return value


class DS_GroupLearnsSchames(BaseModel):
    tg_id_user: int
    title: str = Field(max_length=100)


class DS_GroupsSchames(BaseModel):
    tg_id_student: int
    id_grouplearn: int


class Academy_StudentSchames(BaseModel):
    telegram_id: int
    name: str = Field(max_length=30)
    surname: str = Field(max_length=30)
    email: Optional[EmailStr] = None


class Academy_CoursesSchames(BaseModel):
    name: str = Field(max_length=30)


class Academy_EdMaterialsSchames(BaseModel):
    url: str
    id_courses: int


class Academy_CertificateSchames(BaseModel):
    tg_id_student: int
    url_certificate: str
    id_courses: int
