from abc import ABC, abstractmethod

from app.episodes.domain.dtos.create_episode import CreateEpisodeDTO
from app.episodes.domain.dtos.episode import EpisodeDTO
from app.episodes.domain.dtos.find_episode import FindEpisodeDTO
from app.episodes.domain.dtos.update_episode import UpdateEpisodeDTO


class IEpisodeRepository(ABC):
    @abstractmethod
    def create(self, create: CreateEpisodeDTO) -> EpisodeDTO:
        """
        Creates a new episode.

        Args:
            create: DTO containing the data of the episode that will be created.
        
        Returns:
            EpisodeDTO: A new episode.
        """
    
    @abstractmethod
    def create_many(self, create: list[CreateEpisodeDTO]) -> list[EpisodeDTO]:
        """
        """
    
    @abstractmethod
    def get(self, where: FindEpisodeDTO) -> list[EpisodeDTO]:
        """
        Searches for one or multiple episodes following specific filter criteria.

        Args:
            where: DTO containing filter criteria.

        Returns:
            list[EpisodeDTO]: Returns a list of all the episodes matching the filter.
        """

    @abstractmethod
    def update(self, uuid: str, update: UpdateEpisodeDTO) -> str:
        """
        Updates one or more data of an episode.

        Args:
            uuid: UUID of the episode to be updated.
            update: DTO containing which fields of the episode will be updated.

        Returns:
            str: Returns the UUID of the episode.
        """

    @abstractmethod
    def delete(self, uuid: str) -> None:
        """
        Deletes an episode.

        Args:
            uuid: UUID of the episode to be deleted.

        Returns:
            None: No return, since the episode doesn't exist anymore. 
        """