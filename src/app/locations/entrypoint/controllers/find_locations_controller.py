from dataclasses import asdict

from app.locations.domain.dtos.find_location import FindLocationDTO
from app.locations.domain.usecases.find_locations_usecase import FindLocationsUsecase
from app.locations.entrypoint.requests.find_locations_request import FindLocationsRequest
from framework.dependency_injector import DependencyInjector

class FindLocationsController:
    def run(self, where: FindLocationsRequest) -> list[dict]:
        dependency_injector = DependencyInjector()
        usecase = FindLocationsUsecase(
            dependency_injector.get_location_repository_adapter()
        )
        res = usecase.execute(
            FindLocationDTO(
                name=where.name
            )
        )
        return [asdict(c) for c in res]