from datetime import datetime
import ormar

from db.session import metadata, database


class Cinema(ormar.Model):
    """
    Cinema model
    """
    class Meta(ormar.ModelMeta):
        tablename = 'cinema'
        metadata = metadata
        database = database

    id: int = ormar.Integer(primary_key=True)
    name: str = ormar.String(max_length=127)
    session_report: datetime = ormar.Date(datetime.now())
    likes: int = ormar.Integer(default=0)
