from typing import Dict, Any

from apps.cinema.models import Cinema


class CinemaRepository:
    """ Cinema Repository """

    async def get_all_movie(self):
        return await Cinema.objects.all()

    async def get_movie(self, id: int):
        return await Cinema.objects.get(pk=id)

    async def insert_cinema(self, details: Dict[str, Any]) -> bool:
        """Create Cinema function"""

        try:
            await Cinema.objects.create(**details)

        except Exception:
            return False
        return True

    async def update_cinema(self, id: int, details: Dict[str, Any]):
        """ Update Cinema Function"""

        try:
            cinema = await self.get_movie(id)
            await cinema.update(**details)

        except Exception:
            return False
        return True

    async def delete_cinema(self, id: int):
        """ Delete Cinema Function"""

        try:
            cinema = await self.get_movie(id)
            await cinema.delete()

        except Exception:
            return False
        return True
