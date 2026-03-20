from abc import ABC, abstractmethod

from app.species.domain.dtos.create_specie import CreateSpecieDTO
from app.species.domain.dtos.specie import SpecieDTO
from app.species.domain.dtos.find_specie import FindSpecieDTO
from app.species.domain.dtos.update_specie import UpdateSpecieDTO


class ISpecieRepository(ABC):
    @abstractmethod
    def create(self, create: CreateSpecieDTO) -> SpecieDTO:
        """
        Creates a new specie.

        Args:
            create: DTO containing the data of the specie that will be created.
        
        Returns:
            SpecieDTO: A new specie.
        """
    
    @abstractmethod
    def get(self, where: FindSpecieDTO) -> list[SpecieDTO]:
        """
        Searches for one or multiple species following specific filter criteria.

        Args:
            where: DTO containing filter criteria.

        Returns:
            list[SpecieDTO]: Returns a list of all the species matching the filter.
        """

    @abstractmethod
    def update(self, uuid: str, update: UpdateSpecieDTO) -> str:
        """
        Updates one or more data of a specie.

        Args:
            uuid: UUID of the specie to be updated.
            update: DTO containing which fields of the specie will be updated.

        Returns:
            str: Returns the UUID of the specie.
        """

    @abstractmethod
    def delete(self, uuid: str) -> None:
        """
        Deletes an specie.

        Args:
            uuid: UUID of the specie to be deleted.

        Returns:
            None: No return, since the specie doesn't exist anymore. 
        """