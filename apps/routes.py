from fastapi import APIRouter

from apps.cinema.api import cinema_router
from apps.movie.api import movie_router

api_router = APIRouter()

api_router.include_router(cinema_router, prefix='/cinema', tags=["cinema"])
api_router.include_router(movie_router, prefix='/movie', tags=["movie"])
