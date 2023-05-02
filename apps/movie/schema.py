from datetime import date

from pydantic import BaseModel


class MovieSchema(BaseModel):
    """Movie schema"""
    name: str
    year_of_creation: date
    director: str
    duration: str
    country: str
    description: str
    likes: int
    cinema: int
