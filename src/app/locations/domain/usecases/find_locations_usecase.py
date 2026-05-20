from app.locations.domain.dtos.find_location import FindLocationDTO
from app.locations.domain.dtos.location import LocationDTO
from app.locations.domain.repositories.i_location_repository import ILocationRepository


class FindLocationsUsecase:
    def __init__(
            self, location_repository: ILocationRepository,
        ):
        self.location_repository = location_repository

    def execute(self, where: FindLocationDTO) -> list[LocationDTO]:
        return self.location_repository.get(where)