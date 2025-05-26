from fastapi import HTTPException
from sqlalchemy import select

from .database import create_session
from .models import (
    DrivingSchool_User,
    DrivingSchool_GroupLearns,
    DrivingSchool_Groups)

from . import models

from .schames import (
    DS_UserSchames,
    DS_GroupLearnsSchames,
    DS_GroupsSchames,
    DS_TG_ID_Schames)

from . import schames


async def commit_to_db(session, db):
    session.add(db)
    await session.flush()
    await session.commit()
    return db


async def get_data_by_query(session, query):
    result = await session.execute(query)
    return result.scalar()

async def get_all_data_by_query(session, query):
    result = await session.execute(query)
    return result.scalars().all()


async def create_user_db(
    schemas_user: DS_UserSchames
) -> DrivingSchool_User:
    
    async with create_session() as session:
        db = DrivingSchool_User(
            telegram_id = schemas_user.telegram_id,
            name = schemas_user.name,
            surname = schemas_user.surname,
            contact_phone = schemas_user.contact_phone,
            user_type = schemas_user.user_type
        )

        return await commit_to_db(session, db)


async def get_user_by_tg_id(
        tg_id: int
) -> DrivingSchool_User:
    
    async with create_session() as session:
        query = select(
            DrivingSchool_User
        ).where(
            DrivingSchool_User.telegram_id==tg_id
        )
        return await get_data_by_query(session, query)
    

async def get_all_users() -> DrivingSchool_User:
    async with create_session() as session:
        query = select(DrivingSchool_User)
        result = await session.execute(query)
        return result.scalars().all()


async def create_groupslearns_db(
        schames_grouplearn: DS_GroupLearnsSchames,
) -> DrivingSchool_GroupLearns:
    
    async with create_session() as session:
        db = DrivingSchool_GroupLearns(
            tg_id_user = schames_grouplearn.tg_id_user,
            title = schames_grouplearn.title
        )
    
        return await commit_to_db(session, db)


async def get_groupslearns_by_tgiduser(
        tg_id: int
) -> DrivingSchool_GroupLearns:
    async with create_session() as session:
        query = select(
            DrivingSchool_GroupLearns
        ).where(
            DrivingSchool_GroupLearns.tg_id_user == tg_id
        )
        return await get_data_by_query(session, query)


async def create_groups_db(
        groups_schames: DS_GroupsSchames
) -> DrivingSchool_Groups:
    async with create_session() as session:
        db = DrivingSchool_Groups(
            tg_id_student = groups_schames.tg_id_student,
            id_grouplearn = groups_schames.id_grouplearn
        )
        return await commit_to_db(session, db)


async def get_groups_by_tg_id(tg_id: int) -> DrivingSchool_Groups:
    async with create_session() as session:
        query = select(
            DrivingSchool_Groups
        ).where(
            DrivingSchool_Groups.tg_id_student==tg_id
        )
        return await get_data_by_query(session, query)


async def get_groups_by_idgrouplearn(id_grouplearn: int):
    async with create_session() as session:
        query = select(
            DrivingSchool_Groups
        ).where(
            DrivingSchool_Groups.id_grouplearn==id_grouplearn
        )
        return await get_data_by_query(session, query)


### ===================================== 
# ACADEMY

async def academy_create_student_db(
        schames: schames.Academy_StudentSchames
) -> models.Academy_Student:
    async with create_session() as session:
        db = models.Academy_Student(
            telegram_id = schames.telegram_id,
            name = schames.name,
            surname = schames.surname,
            email = schames.email
        )
        return await commit_to_db(session, db)


async def academy_get_student_by_tg_id(
        tg_id: int
) -> models.Academy_Student:
    async with create_session() as session:
        query = select(
            models.Academy_Student
        ).where(
            models
            .Academy_Student
            .telegram_id == tg_id
        )
        return await get_data_by_query(
            session, 
            query
        )


async def academy_create_courses(
        schames: schames.Academy_CoursesSchames
) -> models.Academy_Courses:
    async with create_session() as session:

        db = models.Academy_Courses(
            name = schames.name
        )
        return await commit_to_db(session, db)


async def academy_get_all_courses(
        
) -> models.Academy_Courses:
    async with create_session() as session:
        query = select(
            models.Academy_Courses
        )
        return await get_all_data_by_query(
            session, query
        )
    

async def academy_get_courses_by_id(
        id_courses: int
) -> models.Academy_Courses:
    async with create_session() as session:
        query = select(
            models.Academy_Courses
        ).where(
            models
            .Academy_Courses
            .id_courses == id_courses
        )
        return await get_data_by_query(session, query)


async def academy_create_ed_materials(
        schames: schames.Academy_EdMaterialsSchames
) -> models.Academy_EdMaterials:
    async with create_session() as session:
        db = models.Academy_EdMaterials(
            url = schames.url,
            id_courses = schames.id_courses
        )
        return await commit_to_db(session, db)
    

async def academy_get_ed_materials_by_id_courses(
    id_courses:int
) -> models.Academy_EdMaterials:
    async with create_session() as session:
        query = select(
            models.Academy_EdMaterials
        ).where(
            models
            .Academy_EdMaterials
            .id_courses == id_courses
        )
        return await get_data_by_query(session, query)


async def academy_create_certificate(
        schames: schames.Academy_CertificateSchames
) -> models.Academy_Certificate:
    async with create_session() as session:
        db = models.Academy_Certificate(
            tg_id_student = schames.tg_id_student,
            url_certificate = schames.url_certificate,
            id_courses = schames.id_courses
        )
        return await commit_to_db(session, db)


async def academy_get_cretificate_by_tg_id(
        tg_id: int
) -> models.Academy_Certificate:
    async with create_session() as session:
        query = select(
            models.Academy_Certificate
        ).where(
            models
            .Academy_Certificate
            .tg_id_student == tg_id
        )
        return await get_data_by_query(session, query)
