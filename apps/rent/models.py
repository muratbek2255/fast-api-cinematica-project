import ormar

from db.session import metadata, database


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
    
