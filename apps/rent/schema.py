from pydantic import BaseModel


class RentSchema(BaseModel):
    row: str
    place: str
    is_rent: bool
