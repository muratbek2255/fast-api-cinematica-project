from datetime import datetime

from pydantic import BaseModel, validator


class PaymentCheckRequisitesSchema(BaseModel):
    """For validate schema"""
    is_checked: bool = True
    payment_status: str = 'IN_PROGRESS'


class PaymentSchema(BaseModel):
    """Payment schema"""
    sum_of_favour: int
    account_check: str
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()
    rent: int
    payment_status: str = 'STATUS_SUCCESS'
    is_finished: bool = True

    @validator("sum_of_favour")
    def validate_sum_of_favour(cls, values):
        if values > 500:
            return values
        else:
            raise ValueError("WTD")

    @validator("account_check")
    def validate_account_check(cls, values):
        if values is not None:
            return values
        else:
            raise ValueError("WTD")
