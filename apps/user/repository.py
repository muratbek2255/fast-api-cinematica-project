from typing import Dict, Any

from apps.user.models import User


class UserRepository:
    """User Crud Repository"""

    async def get_user(self, id: int):
        return await User.objects.get(pk=id)

    async def create_user(self, details: Dict[str, Any]):
        """For creating user"""
        try:
            await User.objects.create(**details)
        except Exception as e:
            return False
        return True

    async def delete_user(self, id: int, details: Dict[str, Any]):
        """For deleting user"""
        try:
            user = await self.get_user(id)
            await user.delete()
        except Exception as e:
            return False
        return True
