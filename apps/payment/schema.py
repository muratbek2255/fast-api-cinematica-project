from datetime import datetime

from pydantic import BaseModel


class PaymentCheckSchema(BaseModel):
    """For validate schema"""
    sum_of_favour: int
    account_check: str


class PaymentSchema(BaseModel):
    """Payment schema"""
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()
    sum_of_favour: int
    account_check: str
    rent: int
