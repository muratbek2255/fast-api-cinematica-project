from datetime import date

import ormar

from apps.cinema.models import Cinema
from db.session import metadata, database


class Movie(ormar.Model):
    """Movie model"""

    class Meta(ormar.ModelMeta):
        tablename = 'movies'
        metadata = metadata
        database = database

    id: int = ormar.Integer(primary_key=True)
    name: str = ormar.String(max_length=127)
    year_of_creation: date = ormar.Date()
    director: str = ormar.String(max_length=129)
    duration: str = ormar.String(max_length=129)
    country: str = ormar.String(max_length=129)
    description: str = ormar.String(max_length=500)
    likes: int = ormar.Integer(default=0)
    cinema: int = ormar.ForeignKey(to=Cinema,  unique=False, index=False, nullable=False)
