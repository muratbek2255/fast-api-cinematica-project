import databases
import ormar
import sqlalchemy

from core.settings import SQLALCHEMY_DATABASE_URI


metadata = sqlalchemy.MetaData()
database = databases.Database(SQLALCHEMY_DATABASE_URI)
engine = sqlalchemy.create_engine(SQLALCHEMY_DATABASE_URI)


class MainMata(ormar.ModelMeta):
    metadata = metadata
    database = database
