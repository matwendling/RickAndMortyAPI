from abc import ABC, abstractmethod

from app.origins.domain.dtos.create_origin import CreateOriginDTO
from app.origins.domain.dtos.origin import OriginDTO
from app.origins.domain.dtos.find_origin import FindOriginDTO
from app.origins.domain.dtos.update_origin import UpdateOriginDTO

class IOriginRepository(ABC):
    @abstractmethod
    def create(self, create: CreateOriginDTO) -> OriginDTO:
        """
        Creates a new origin.

        Args:
            create: DTO containing the data of the origin that will be created.
        
        Returns:
            OriginDTO: A new origin.
        """
    
    @abstractmethod
    def get(self, where: FindOriginDTO) -> list[OriginDTO]:
        """
        Searches for one or multiple origins following specific filter criteria.

        Args:
            where: DTO containing filter criteria.

        Returns:
            list[OriginDTO]: Returns a list of all the origins matching the filter.
        """

    @abstractmethod
    def update(self, uuid: str, update: UpdateOriginDTO) -> str:
        """
        Updates one or more data of a origin.

        Args:
            uuid: UUID of the origin to be updated.
            update: DTO containing which fields of the origin will be updated.

        Returns:
            str: Returns the UUID of the origin.
        """

    @abstractmethod
    def delete(self, uuid: str) -> None:
        """
        Deletes an origin.

        Args:
            uuid: UUID of the origin to be deleted.

        Returns:
            None: No return, since the origin doesn't exist anymore. 
        """