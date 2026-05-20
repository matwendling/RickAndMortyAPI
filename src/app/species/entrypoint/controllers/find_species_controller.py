from dataclasses import asdict

from app.species.domain.dtos.find_specie import FindSpecieDTO
from app.species.domain.usecases.find_species_usecase import FindSpeciesUsecase
from app.species.entrypoint.requests.find_specie_request import FindSpecieRequest
from framework.dependency_injector import DependencyInjector


class FindSpeciesController:
    def run(self, where: FindSpecieRequest) -> list[dict]:
        dependency_injector = DependencyInjector()
        usecase = FindSpeciesUsecase(
            dependency_injector.get_specie_repository_adapter()
        )
        res = usecase.execute(
            FindSpecieDTO(
                name=where.name
            )
        )
        return [asdict(s) for s in res]