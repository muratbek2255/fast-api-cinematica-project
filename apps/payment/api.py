from fastapi import APIRouter

from apps.payment.repository import PaymentRepository
from apps.payment.schema import (
    PaymentCheckRequisitesSchema, PaymentSchema
)

payment_router = APIRouter()


@payment_router.post("/check-and-add")
async def check_and_add_payment(req: PaymentCheckRequisitesSchema):
    """This api for validate sum and requisites"""
    payment_dict = req.dict(exclude_unset=True)
    repo = PaymentRepository()
    result = await repo.create_check_payment(payment_dict)
    return result


@payment_router.put("/update-to-success/{id}")
async def finalize_payment_and_set_status_to_success(id: int, req: PaymentSchema):
    """This api for finalize payment and set status in Payment model to 'STATUS_SUCCESS' """
    payment_dict = req.dict(exclude_unset=True)
    repo = PaymentRepository()
    result = await repo.update_payment_for_success(id, payment_dict)
    return result
