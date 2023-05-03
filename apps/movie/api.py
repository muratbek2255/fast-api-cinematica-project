from fastapi import APIRouter
from starlette.responses import JSONResponse

from apps.movie.repository import MovieRepository
from apps.movie.schema import MovieSchema

movie_router = APIRouter()


@movie_router.post("/add")
async def insert_movie(req: MovieSchema):
    movie_dict = req.dict(exclude_unset=True)
    repo = MovieRepository()
    result = await repo.insert_movie(movie_dict)

    if result is True:
        return req
    else:
        return JSONResponse(content={'message': 'update trainer profile problem encountered'}, status_code=500)


@movie_router.put("/update/{id}")
async def update_movie(id: int, req: MovieSchema):
    movie_dict = req.dict(exclude_unset=True)
    repo = MovieRepository()
    result = await repo.update_movie(id, movie_dict)

    if result is True:
        return req
    else:
        return JSONResponse(content={'message': 'update trainer profile problem encountered'}, status_code=500)


@movie_router.delete("/delete/{id}")
async def delete_movie(id: int):
    repo = MovieRepository()
    result = await repo.delete_movie(id)

    if result is True:
        return result
    else:
        return JSONResponse(content={'message': 'update trainer profile problem encountered'}, status_code=500)
