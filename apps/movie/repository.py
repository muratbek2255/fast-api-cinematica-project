from typing import Dict, Any

from apps.movie.models import Movie


class MovieRepository:
    """Movie Repository"""
    async def get_all_movie(self):
        return await Movie.objects.all()

    async def get_movie(self, id: int):
        return await Movie.objects.get(pk=id)

    async def insert_movie(self, details: Dict[str, Any]) -> bool:
        """ Create Cinema function """
        try:
            await Movie.objects.create(**details)
        except Exception:
            return False
        return True

    async def update_movie(self, id: int, details: Dict[str, Any]):
        """ Update Cinema Function"""
        try:
            cinema = await self.get_movie(id)
            await cinema.update(**details)
        except Exception:
            return False
        return True

    async def delete_movie(self, id: int):
        """ Delete Cinema Function"""
        try:
            cinema = await self.get_movie(id)
            await cinema.delete()
        except Exception:
            return False
        return True
