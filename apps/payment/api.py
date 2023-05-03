from fastapi import APIRouter

from apps.payment.schema import PaymentCheckSchema

payment_router = APIRouter()


@payment_router.post("/check")
async def check_payment(req: PaymentCheckSchema):
    """"""
