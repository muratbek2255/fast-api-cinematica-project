import ormar

from apps.base.utils.abstract_user_model import Login


class User(Login):
    username: str = ormar.String(max_length=100, unique=True)
    password: str = ormar.String(max_length=127, unique=False, index=False, nullable=False)
