from typing import Dict, Any

from apps.payment.models import Payment


class PaymentRepository:
    """Payment Repository"""
    async def get_payment(self, id: int):
        return await Payment.objects.get(pk=id)

    async def create_check_payment(self, details: Dict[str, Any]):
        """Check Payment"""
        try:
            await Payment.objects.create(**details)
        except Exception as e:
            return "Something wrong with validation"

    async def update_payment_for_success(self, id: int, details: Dict[str, Any]):
        """Update Payment For Success"""
        try:
            payment = await self.get_payment(id)
            if payment.is_checked is True and payment.payment_status == "IN_PROGRESS":
                await payment.update(**details)
                await payment.rent.update(status='BOOKED')

            else:
                return "You have some problem with requisites"

        except Exception as e:
            return False
        return True

    async def rollback_payment(self, id: int, details: Dict[str, Any]):
        """Rollback payment """
