from fastapi import APIRouter

from api import crud, schames


router_driving_supp = APIRouter(
    prefix='/driving-school',
    tags=['driving-supp']
)


@router_driving_supp.get()
async def get_new_supp_mess():
    ...


@router_driving_supp.post()
async def send_new_supp_mess():
    ...