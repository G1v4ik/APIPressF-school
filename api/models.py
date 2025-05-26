from sqlalchemy import (
    String, 
    Integer, 
    ForeignKey, 
    MetaData, 
    VARCHAR,
    JSON,
    DATETIME)
from sqlalchemy.orm import (
    Mapped, 
    mapped_column, 
    DeclarativeBase)
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.dialects.postgresql import JSONB


import enum
import json


class BaseModel(AsyncAttrs, DeclarativeBase):
    metadata = MetaData(schema='apipressf')


class UserType(str, enum.Enum):
    STUDENT = "Student"
    TEACHER = "Teacher"


class DrivingSchool_User(BaseModel):
    __tablename__ = "DS_Users"
    telegram_id: Mapped[int] = mapped_column(primary_key=True, 
                                              autoincrement=False, 
                                              unique=True)
    name: Mapped[str | None]
    surname: Mapped[str | None] = mapped_column(
        nullable=True
    )
    contact_phone: Mapped[str | None] = mapped_column(
        nullable=True
    )
    user_type: Mapped[UserType] = mapped_column(
        default=UserType.STUDENT
    )



class DrivingSchool_GroupLearns(BaseModel):
    __tablename__ = "DS_GroupLearns"
    id_grouplearn: Mapped[int] = mapped_column(
        primary_key=True, autoincrement=True
    )
    tg_id_user: Mapped[int] = mapped_column(
        ForeignKey("DS_Users.telegram_id")
    )
    title: Mapped[str] = mapped_column(
        VARCHAR(length=100)
    )



class DrivingSchool_Groups(BaseModel):
    __tablename__ = "DS_Groups"
    id_group: Mapped[int] = mapped_column(
        primary_key=True, autoincrement=True
    )
    tg_id_student: Mapped[int] = mapped_column(
        ForeignKey("DS_Users.telegram_id")
    )
    id_grouplearn: Mapped[int] = mapped_column(
        ForeignKey("DS_GroupLearns.id_grouplearn")
    )



class Academy_Student(BaseModel):
    __tablename__ = "Academy_Student"
    telegram_id: Mapped[int] = mapped_column(
        primary_key=True, unique=True,
        autoincrement=False
    )
    name: Mapped[str]
    surname: Mapped[str]
    email: Mapped[str] = mapped_column(
        nullable=True
    )


class Academy_Courses(BaseModel):
    __tablename__ = "Academy_Courses"
    id_courses: Mapped[int] = mapped_column(
        primary_key=True, autoincrement=True
    )
    name: Mapped[str]


class Academy_EdMaterials(BaseModel):
    __tablename__ = "Academy_EdMaterials"
    id_ed_materials: Mapped[int] = mapped_column(
        primary_key=True, autoincrement=True
    )
    url: Mapped[str]
    id_courses: Mapped[str] = mapped_column(
        ForeignKey(
            "Academy_Courses.id_courses"
        )
    )


class Academy_Certificate(BaseModel):
    __tablename__ = "Academy_Certificate"
    id_certificate: Mapped[int] = mapped_column(
        primary_key=True, autoincrement=True,
        unique=True
    )
    tg_id_student: Mapped[int] = mapped_column(
        ForeignKey(
            "Academy_Student.telegram_id"
        )
    )
    url_certificate: Mapped[str]
    id_courses: Mapped[int] = mapped_column(
        ForeignKey(
            "Academy_Courses.id_courses"
        )
    )
