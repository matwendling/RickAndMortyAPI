from abc import ABC, abstractmethod

from app.characters.domain.dtos.character import CharacterDTO
from app.characters.domain.dtos.create_character import CreateCharacterDTO
from app.characters.domain.dtos.find_character import FindCharacterDTO
from app.characters.domain.dtos.update_character import UpdateCharacterDTO


class ICharacterRepository(ABC):
    @abstractmethod
    def create(self, create: CreateCharacterDTO) -> CharacterDTO:
        """
        Creates a new character.

        Args:
            create: DTO containing the data of the character that will be created.

        Returns:
            CharacterDTO: A new character.
        """
    
    @abstractmethod
    def get(self, where: FindCharacterDTO) -> list[CharacterDTO]:
        """
        Searches for one or multiple characters following specific filter criteria.

        Args:
            where: DTO containing filter criteria.

        Returns:
            list[CharacterDTO]: Returns a list of all the characters matching the filter.
        """
    
    @abstractmethod
    def update(self, uuid: str, update: UpdateCharacterDTO) -> str:
        """
        Updates one or more data of a character.

        Args:
            uuid: UUID of the character to be updated.
            update: DTO containing which fields of the character will be updated.

        Returns:
            str: Returns the UUID of the character. 
        """
    
    @abstractmethod
    def delete(self, uuid: str) -> None:
        """
        Deletes a character.

        Args:
            uuid: UUID of the character to be deleted.

        Returns:
            None: No return, since the character doesn't exist anymore. 
        """