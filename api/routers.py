from fastapi import APIRouter

from api import crud, schames


router_driving_support = APIRouter(
    prefix='/driving-school',
    tags=['driving-supp']
)


@router_driving_support.get('/support_messages')
async def list_new_support_message():
    list_new_message = await crud.list_support_message()
    return list_new_message


@router_driving_support.post('/support_messages')
async def send_new_support_message(data: schames.DS_support_new_message):
    new_message = await crud.send_support_message(data)
    return new_message


@router_driving_support.patch('/support_messages')
async def response_support_message(data: schames.DS_response_message):
    new_data = await crud.response_support_message(data)
    return new_data
    
