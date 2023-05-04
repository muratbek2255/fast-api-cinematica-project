import enum
from datetime import datetime

import ormar

from apps.rent.models import Rent

from db.session import metadata, database


class StatusOfPayment(enum.Enum):
    IN_PROGRESS = 'IN_PROGRESS'
    SUCCESS = 'STATUS_SUCCESS'
    ROLLBACK = 'STATUS_ROLLBACK'


class Payment(ormar.Model):
    """Payment model"""
    class Meta(ormar.ModelMeta):
        tablename = 'payments'
        metadata = metadata
        database = database

    id: int = ormar.Integer(primary_key=True)
    created_at: datetime = ormar.DateTime(nullable=True)
    updated_at: datetime = ormar.DateTime(nullable=True)
    payment_status: str = ormar.String(max_length=125, choices=list(StatusOfPayment), nullable=True)
    sum_of_favour: int = ormar.Integer(nullable=True)
    account_check: str = ormar.String(max_length=50, nullable=True)
    is_checked: bool = ormar.Boolean(default=False, nullable=True)
    is_finished: bool = ormar.Boolean(default=False, nullable=True)
    rent: int = ormar.ForeignKey(to=Rent, unique=False, index=False, nullable=True)
