from apps.rent.models import Rent, StatusOfRent


class RentRepository:
    """ Rent Service """

    async def get_all_movie(self):
        return await Rent.objects.all()

    async def get_movie(self, id: int):
        return await Rent.objects.get(pk=id)

    async def insert_rent(self, id: int):

        rent = await self.get_movie(id)

        if rent.status == StatusOfRent.IN_PROGRESS:
            return "Rent is in progress"
        if rent.status == StatusOfRent.BOOKED:
            return "Rent is in been not free"
        else:
            await rent.update(status="IN_PROGRESS")
            return "Status in Progress"

    async def rollback_rent(self, id: int):

        rent = await self.get_movie(id)

        if rent.status == "IN_PROGRESS":
            await rent.update(is_rent=False)
            await rent.update(status="FREE")
            return "Rent rollback"
