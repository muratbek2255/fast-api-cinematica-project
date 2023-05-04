from datetime import datetime

from pydantic import BaseModel


class RegistrationSchema(BaseModel):
    """User Registration Schema"""
    is_active: bool = True
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()
    role: str = "user"
    username: str
    password: str


class AuthenticationSchema(BaseModel):
    """User login Schema"""
    username: str
    password: str


class TokenSchema(BaseModel):
    access_token: str
    refresh_token: str


class TokenPayload(BaseModel):
    sub: str = None
    exp: int = None


class UserOut(BaseModel):
    id: int
    email: str


class SystemUser(UserOut):
    password: str
