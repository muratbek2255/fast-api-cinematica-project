from fastapi import APIRouter

from apps.cinema.api import cinema_router
from apps.movie.api import movie_router
from apps.payment.api import payment_router
from apps.rent.api import rent_router

api_router = APIRouter()

api_router.include_router(cinema_router, prefix='/cinema', tags=["cinema"])
api_router.include_router(movie_router, prefix='/movie', tags=["movie"])
api_router.include_router(rent_router, prefix='/rent', tags=["rent"])
api_router.include_router(payment_router, prefix='/payment', tags=["payment"])
