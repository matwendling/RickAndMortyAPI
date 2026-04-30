from abc import ABC, abstractmethod

from app.characters.domain.dtos.character_client.character_client_dto import CharacterClientDTO

class ICharacterClient(ABC):
    @abstractmethod
    def fetch_one(self, id: str) -> CharacterClientDTO:
        """
        ...

        Args:
            ...

        Returns:
            ...
        """
    

    @abstractmethod
    def fetch_all(self) -> list[CharacterClientDTO]:
        """
        ...

        Args:
            ...

        Returns:
            ...
        """
    

    @abstractmethod
    def fecth_many(self) -> list[CharacterClientDTO]:
        """
        ...

        Args:
            ...

        Returns:
            ...
        """