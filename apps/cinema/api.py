from fastapi import APIRouter
from starlette.responses import JSONResponse

from apps.cinema.repository import CinemaRepository
from apps.cinema.schema import CinemaSchema

cinema_router = APIRouter()


@cinema_router.post("/add")
async def add_cinema(req: CinemaSchema):
    cinema_dict = req.dict(exclude_unset=True)
    repo = CinemaRepository()
    result = await repo.insert_cinema(cinema_dict)
    print(result)

    if result is True:
        return req
    else:
        return JSONResponse(content={'message': 'update cinema problem encountered'}, status_code=500)


@cinema_router.put("/update/{id}")
async def update_cinema(id: int, req: CinemaSchema):
    cinema_dict = req.dict(exclude_unset=True)
    repo = CinemaRepository()
    result = await repo.update_cinema(id, cinema_dict)

    if result is True:
        return req
    else:
        return JSONResponse(content={'message': 'update cinema problem encountered'}, status_code=500)


@cinema_router.delete("/delete/{id}")
async def delete_cinema(id: int):
    repo = CinemaRepository()
    result = await repo.delete_cinema(id)
    return result
