from datetime import datetime

from pydantic import BaseModel


class CinemaSchema(BaseModel):
    """Cinema Schema"""
    name: str
    session_report: datetime = datetime.now()
    likes: int

    class Config:
        orm_mode = True
