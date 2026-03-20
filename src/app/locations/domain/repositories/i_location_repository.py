from abc import ABC, abstractmethod

from app.locations.domain.dtos.create_location import CreateLocationDTO
from app.locations.domain.dtos.location import LocationDTO
from app.locations.domain.dtos.find_location import FindLocationDTO
from app.locations.domain.dtos.update_location import UpdateLocationDTO


class ILocationRepository(ABC):
    @abstractmethod
    def create(self, create: CreateLocationDTO) -> LocationDTO:
        """
        Creates a new location.

        Args:
            create: DTO containing the data of the location that will be created.
        
        Returns:
            LocationDTO: A new location.
        """
    
    @abstractmethod
    def get(self, where: FindLocationDTO) -> list[LocationDTO]:
        """
        Searches for one or multiple locations following specific filter criteria.

        Args:
            where: DTO containing filter criteria.

        Returns:
            list[LocationDTO]: Returns a list of all the locations matching the filter.
        """

    @abstractmethod
    def update(self, uuid: str, update: UpdateLocationDTO) -> str:
        """
        Updates one or more data of a location.

        Args:
            uuid: UUID of the location to be updated.
            update: DTO containing which fields of the location will be updated.

        Returns:
            str: Returns the UUID of the location.
        """

    @abstractmethod
    def delete(self, uuid: str) -> None:
        """
        Deletes an location.

        Args:
            uuid: UUID of the location to be deleted.

        Returns:
            None: No return, since the location doesn't exist anymore. 
        """