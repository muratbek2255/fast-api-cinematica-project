from apps.payment.schema import (
    PaymentSchema, PaymentCheckSchema
)


class PaymentRepository:
    """Payment Repository"""

    async def check_payment(self, req: PaymentCheckSchema):
        """"""

    async def add_payment(self, req: PaymentSchema):
        """"""
