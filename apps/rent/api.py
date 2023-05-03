from fastapi import APIRouter

from apps.rent.repository import RentRepository


rent_router = APIRouter()


@rent_router.put("/add-rent")
async def insert_rent(id: int):
    """ Insert rent """
    repo = RentRepository()
    result = await repo.insert_rent(id)
    return result


@rent_router.put("/rollback-rent")
async def rollback_rent(id: int):
    """ Rollback rent """
    repo = RentRepository()
    result = await repo.rollback_rent(id)
    return result
