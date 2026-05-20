from app.characters.domain.dtos.character import CharacterDTO
from app.characters.domain.dtos.find_character import FindCharacterDTO
from app.characters.domain.repositories.i_character_repository import ICharacterRepository

class FindCharactersUsecase:
    def __init__(
        self, character_repository: ICharacterRepository, 
    ):
        self.character_repository = character_repository

    def execute(self, where: FindCharacterDTO) -> list[CharacterDTO]:
        return self.character_repository.get(where)