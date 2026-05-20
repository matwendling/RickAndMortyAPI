from app.species.domain.dtos.find_specie import FindSpecieDTO
from app.species.domain.dtos.specie import SpecieDTO
from app.species.domain.repositories.i_specie_repository import ISpecieRepository


class FindSpeciesUsecase:
    def __init__(
            self, specie_repository: ISpecieRepository
        ):
            self.specie_repository = specie_repository

    def execute(self, where: FindSpecieDTO) -> list[SpecieDTO]:
          return self.specie_repository.get(where)