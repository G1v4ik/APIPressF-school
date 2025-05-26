from fastapi import APIRouter

from api import crud, schames
from api.database import delete_tables


router_academy = APIRouter(
    prefix="/academy",
    tags=["academy"],
)


router_driving_school = APIRouter(
    prefix="/driving-school",
    tags=["driving-school"],
)

#DATABASE START

@router_driving_school.get('/drop/table')
async def view_drop_table():
    await delete_tables()
    return "OK"

# DATABASE END

# USER START

@router_driving_school.post('/users')
async def view_create_user(user: schames.DS_UserSchames):
    new_user = await crud.create_user_db(schemas_user=user)
    return new_user

# реализовать позже patch
# ==========================
# PATCH
# ==========================

@router_driving_school.get('/users')
async def view_get_all_users():
    return await crud.get_all_users()
    

@router_driving_school.get('/users/{telegram_id}')
async def view_get_user_by_tg_id(telegram_id: int):
    get_user = await crud.get_user_by_tg_id(tg_id=telegram_id)
    return get_user

# USER END


#GroupLearn START

@router_driving_school.post('/groups-learns')
async def view_create_groupslearns(
    group_learn: schames.DS_GroupLearnsSchames
):
    create_groupslearns = await crud.create_groupslearns_db(
        schames_grouplearn=group_learn
    )
    return create_groupslearns


@router_driving_school.get('/groups-learns/tg_id/{tg_id}')
async def view_get_grouplearn_by_tg_id(
        tg_id: int
):
    get_grouplearn = await crud.get_groupslearns_by_tgiduser(
        tg_id
    )
    return get_grouplearn


#GroupLearn END

#Groups START

@router_driving_school.post('/groups')
async def view_create_groups(
    groups: schames.DS_GroupsSchames
):
    create_groups = await crud.create_groups_db(
        groups_schames=groups
    )
    return create_groups


@router_driving_school.get('/groups/tg_id/{tg_id}')
async def view_get_groups_by_tg_id(tg_id: int):
    get_groups = await crud.get_groups_by_tg_id(
        tg_id
    )
    return get_groups

@router_driving_school.get('/groups/id_groupslearns/{id_groupslearns}')
async def view_get_group_by_id_groupslearns(
    id_groupslearns: int
):
    get_groups = await crud.get_groups_by_idgrouplearn(
        id_groupslearns
    )
    return get_groups

#Groups END


### ACADEMY
@router_academy.post('/students')
async def view_academy_create_student(
    data_student: schames.Academy_StudentSchames
):
    create_student = await crud.academy_create_student_db(
        data_student
    )
    return create_student


@router_academy.get('/students/tg_id/{tg_id}')
async def view_academy_get_student_tg_id(
    tg_id: int
):
    get_student = await crud.academy_get_student_by_tg_id(
        tg_id
    )
    return get_student


@router_academy.post('/courses')
async def view_academy_create_courses(
    data_courses: schames.Academy_CoursesSchames
):
    create_courses = await crud.academy_create_courses(
        data_courses
    )
    return create_courses


@router_academy.get('/courses')
async def view_academy_get_all_courses():
    get_courses = await crud.academy_get_all_courses()
    return get_courses


@router_academy.get('/corses/id_courses/{id_courses}')
async def view_academy_get_courses_by_id(
    id_courses: int
): 
    get_courses = await crud.academy_get_courses_by_id(
        id_courses
    )
    return get_courses


@router_academy.post('/ed_materials')
async def view_academy_create_ed_materials(
    data_ed_materials: schames.Academy_EdMaterialsSchames
):
    create_ed_materials = await crud.academy_create_ed_materials(
        data_ed_materials
    )
    return create_ed_materials


@router_academy.get('/ed_materials/id_courses/{id_courses}')
async def view_academy_get_ed_materials_by_id_courses(
    id_courses: int
):
    get_ed_materials = await crud.academy_get_ed_materials_by_id_courses(id_courses)
    return get_ed_materials


@router_academy.post('/certificates')
async def view_academy_create_certificate(
    data_certificate: schames.Academy_CertificateSchames
):
    create_certificate = await crud.academy_create_certificate(
        data_certificate
    )
    return create_certificate


@router_academy.get('/certificates/tg_id/{tg_id}')
async def view_academy_get_certificate_by_tg_id(
    tg_id: int
):
    get_certificates = await crud.academy_get_cretificate_by_tg_id(tg_id)
    return get_certificates