from typing import Optional

from pydantic import BaseModel

from apps.rent.models import StatusOfRent


class RentSchema(BaseModel):
    row: str
    place: str
    is_rent: bool
    status: Optional[StatusOfRent]
