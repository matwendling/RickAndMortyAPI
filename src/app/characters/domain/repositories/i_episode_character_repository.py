from abc import ABC, abstractmethod

from app.characters.domain.dtos.episodes.create_episode_character import CreateEpisodeCharacterDTO
from app.characters.domain.dtos.episodes.episode_character import EpisodeCharacterDTO
from app.characters.domain.dtos.episodes.find_episode_character import FindEpisodeCharacterDTO
from app.characters.domain.dtos.episodes.update_episode_character import UpdateEpisodeCharacterDTO

class IEpisodeCharacterRepository(ABC):
    @abstractmethod
    def create(self, create: CreateEpisodeCharacterDTO) -> EpisodeCharacterDTO:
        """
        Creates a new episode_character relation.

        Args:
            create: DTO containing the data of the episode_character relation that will be created.
        
        Returns:
            EpisodeCharacterDTO: A new episode_character relation relation.
        """
    
    @abstractmethod
    def get(self, where: FindEpisodeCharacterDTO) -> list[EpisodeCharacterDTO]:
        """
        Searches for one or multiple episode_character relation relations following specific filter criteria.

        Args:
            where: DTO containing filter criteria.

        Returns:
            list[EpisodeCharacterDTO]: Returns a list of all the episode_character relation relations matching the filter.
        """

    @abstractmethod
    def update(self, uuid: str, update: UpdateEpisodeCharacterDTO) -> str:
        """
        Updates one or more data of a episode_character relation relation.

        Args:
            uuid: UUID of the episode_character relation relation to be updated.
            update: DTO containing which fields of the episode_character relation relation will be updated.

        Returns:
            str: Returns the UUID of the episode_character relation relation.
        """

    @abstractmethod
    def delete(self, uuid: str) -> None:
        """
        Deletes an episode_character relation relation.

        Args:
            uuid: UUID of the episode_character relation relation to be deleted.

        Returns:
            None: No return, since the episode_character relation relation doesn't exist anymore. 
        """