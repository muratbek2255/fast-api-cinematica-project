import enum

import ormar

from db.session import metadata, database


class StatusOfRent(enum.Enum):
    IN_PROGRESS = 'IN_PROGRESS'
    FREE = 'FREE'
    BOOKED = 'BOOKED'


class Rent(ormar.Model):
    """ Rent model """

    class Meta(ormar.ModelMeta):
        tablename = 'rents'
        metadata = metadata
        database = database

    id: int = ormar.Integer(primary_key=True)
    row: str = ormar.String(max_length=125)
    place: str = ormar.String(max_length=125)
    is_rent: bool = ormar.Boolean(default=False)
    status: str = ormar.String(max_length=100, choices=list(StatusOfRent))
