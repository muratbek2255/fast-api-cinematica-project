from typing import Dict, Any

from apps.cinema.models import Cinema


class CinemaRepository:

    """ Cinema Repository """

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
            cinema = await Cinema.objects.get(pk=id)
            await cinema.update(**details)

        except Exception:
            return False
        return True

    async def delete_cinema(self, id: int):
        """ Delete Cinema Function"""

        try:
            cinema = await Cinema.objects.get(pk=id)
            await cinema.delete()

        except Exception:
            return False
        return True
